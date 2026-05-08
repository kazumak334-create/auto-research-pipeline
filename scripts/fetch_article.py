#!/usr/bin/env python3
"""
fetch_article.py

URLからページを取得し、本文を抽出・要約JSONとして保存する。
CCRエージェントから Bash 経由で呼び出す。
コンテキストウィンドウには最小限の出力しか返さない。

使い方:
    python scripts/fetch_article.py <company_id> <url> <date>
    python scripts/fetch_article.py byd https://example.com/article 2026-05-08

出力:
    data/fetched/<date>/<company_id>.json
    標準出力: "Done: <company_id>" のみ（コンテキスト節約）
"""

import hashlib
import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

MAX_CHARS = 3000  # 本文の最大文字数（コンテキスト節約）
TIMEOUT = 15


def fetch_and_extract(url: str) -> dict:
    """URLからページを取得して本文テキストを抽出する。"""
    try:
        import requests
        from bs4 import BeautifulSoup

        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding or "utf-8"

        soup = BeautifulSoup(resp.content, "lxml")

        # タイトル抽出
        title = ""
        if soup.title:
            title = soup.title.get_text(strip=True)

        # 本文抽出: article > main > body の優先順
        body_el = (
            soup.find("article")
            or soup.find("main")
            or soup.find("div", class_=lambda c: c and "content" in c.lower())
            or soup.body
        )
        body_text = body_el.get_text(separator=" ", strip=True) if body_el else ""
        body_text = " ".join(body_text.split())  # 連続スペース除去
        body_text = body_text[:MAX_CHARS]

        # published_date: meta タグから取得試行
        published_date = ""
        for meta in soup.find_all("meta"):
            prop = meta.get("property", "") or meta.get("name", "")
            if prop in ("article:published_time", "datePublished", "pubdate"):
                published_date = meta.get("content", "")[:10]
                break

        return {
            "status": "ok",
            "title": title,
            "body_text": body_text,
            "published_date": published_date,
            "hash": hashlib.sha256(body_text.encode()).hexdigest(),
        }

    except Exception as e:
        return {
            "status": "error",
            "title": "",
            "body_text": "",
            "published_date": "",
            "hash": "",
            "error": str(e),
        }


def main():
    if len(sys.argv) < 4:
        print("Usage: fetch_article.py <company_id> <url> <date>", file=sys.stderr)
        sys.exit(1)

    company_id = sys.argv[1]
    url = sys.argv[2]
    date = sys.argv[3]

    out_dir = BASE_DIR / "data" / "fetched" / date
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{company_id}.json"

    result = fetch_and_extract(url)
    result.update(
        {
            "company_id": company_id,
            "source_url": url,
            "date_collected": date,
        }
    )

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # コンテキストウィンドウには最小限だけ返す
    if result["status"] == "ok":
        print(f"Done: {company_id} | {result['title'][:60]}")
    else:
        print(f"Error: {company_id} | {result.get('error', 'unknown')}")


if __name__ == "__main__":
    main()
