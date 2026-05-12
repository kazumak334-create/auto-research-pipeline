#!/usr/bin/env python3
"""
fetch_gnews.py

Google News RSS から当日トップ記事のタイトル・ソース・日付を取得する。
SKILL.md のエージェントは、このスクリプトが返すタイトルを WebSearch に渡して
実URLを解決し、fetch_article.py に渡す。

【設計思想】
  静的クエリ → WebSearch → fetch_article.py   （旧: 古い記事が多い）
  ↓
  GNews RSS → タイトル取得 → WebSearch(タイトル) → fetch_article.py （新: 今日の記事）

GNews は URL 解決を JavaScript リダイレクトで行うため Python からは取得困難。
そのため「何が今日のトップ記事か」の情報だけを提供し、URL 解決は WebSearch に委ねる。

使い方:
  # タイトル情報のみ取得（推奨: SKILL.md から呼び出す）
  python scripts/fetch_gnews.py --info honda "Honda automotive"
  → TITLE: Honda Never Lost Money... | SOURCE: carbuzz.com | DATE: Mon, 11 May 2026

  # デバッグ: 上位3件をリスト表示
  python scripts/fetch_gnews.py --list honda "Honda automotive"
"""

import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
}

GNEWS_BASE = "https://news.google.com/rss/search"
TIMEOUT = 20


def get_gnews_items(query: str, n: int = 5) -> list[dict]:
    """Google News RSS から上位n件を取得。{title, source_name, source_domain, pub_date}"""
    import requests

    params = {"q": query, "hl": "en", "gl": "US", "ceid": "US:en"}
    try:
        resp = requests.get(GNEWS_BASE, params=params, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
    except Exception as e:
        print(f"Error: RSS fetch failed — {e}", file=sys.stderr)
        return []

    try:
        root = ET.fromstring(resp.content)
    except ET.ParseError as e:
        print(f"Error: RSS parse failed — {e}", file=sys.stderr)
        return []

    items = []
    for item in root.findall(".//item")[:n]:
        title_el = item.find("title")
        pub_el = item.find("pubDate")
        src_el = item.find("source")
        if title_el is None:
            continue

        src_name = src_el.text.strip() if src_el is not None else ""
        src_url = src_el.get("url", "") if src_el is not None else ""
        try:
            src_domain = urlparse(src_url).netloc.lstrip("www.")
        except Exception:
            src_domain = ""

        # タイトルから出版社サフィックスを除去 ("Title - Publisher" → "Title")
        raw_title = title_el.text or ""
        clean_title = raw_title.rsplit(" - ", 1)[0].strip() if " - " in raw_title else raw_title

        items.append(
            {
                "title": clean_title,
                "source_name": src_name,
                "source_domain": src_domain,
                "pub_date": pub_el.text[:16] if pub_el is not None else "",
            }
        )
    return items


def main():
    args = sys.argv[1:]

    mode = "--info"  # default
    for flag in ("--info", "--list"):
        if flag in args:
            mode = flag
            args = [a for a in args if a != flag]

    if len(args) < 2:
        print(
            "Usage:\n"
            "  fetch_gnews.py --info <id> <query>    # 1件目のタイトル・ソース・日付を出力\n"
            "  fetch_gnews.py --list <id> <query>    # 上位5件をリスト表示",
            file=sys.stderr,
        )
        sys.exit(1)

    _company_id = args[0]
    query = args[1]

    items = get_gnews_items(query, n=5)
    if not items:
        print(f"Error: No results for '{query}'")
        sys.exit(1)

    if mode == "--list":
        for i, item in enumerate(items, 1):
            print(f"[{i}] {item['pub_date']} | {item['source_name']} | {item['title'][:80]}")
        return

    # --info モード: 1件目を出力
    top = items[0]
    print(
        f"TITLE: {top['title'][:120]} | "
        f"SOURCE: {top['source_domain']} | "
        f"DATE: {top['pub_date']}"
    )


if __name__ == "__main__":
    main()
