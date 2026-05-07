#!/usr/bin/env python3
"""
normalize_sources.py

data/raw/YYYY-MM-DD/ 配下のHTMLファイルを走査し、
本文・タイトル・published_date・publisher を抽出して正規化JSONに変換する。
出力: data/normalized/YYYY-MM-DD/{company_id}.json
"""

import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
NORMALIZED_DIR = BASE_DIR / "data" / "normalized"
CONFIG_SOURCES = BASE_DIR / "config" / "sources.yaml"


def load_fetch_log(date_dir: Path) -> dict:
    """fetch_log.jsonを読み込み、saved_path -> log_entryのマップを返す。"""
    log_path = date_dir / "fetch_log.json"
    if not log_path.exists():
        return {}
    with open(log_path, encoding="utf-8") as f:
        entries = json.load(f)
    return {e["saved_path"]: e for e in entries}


def extract_title(soup: BeautifulSoup) -> str:
    tag = soup.find("title")
    return tag.get_text(strip=True) if tag else ""


def extract_body_text(soup: BeautifulSoup) -> str:
    """article > main > body の優先順で本文を抽出する。"""
    for selector in ["article", "main", "[role='main']", "body"]:
        tag = soup.select_one(selector)
        if tag:
            # script/style を除去
            for s in tag(["script", "style", "nav", "footer", "header"]):
                s.decompose()
            text = tag.get_text(separator="\n", strip=True)
            if len(text) > 100:
                return text
    return soup.get_text(separator="\n", strip=True)


def extract_published_date(soup: BeautifulSoup) -> str:
    """metaタグ・time要素・よくある日付パターンからpublished_dateを探す。"""
    # metaタグ
    for meta_name in ["article:published_time", "pubdate", "date", "DC.date"]:
        meta = soup.find("meta", attrs={"property": meta_name}) or \
               soup.find("meta", attrs={"name": meta_name})
        if meta and meta.get("content"):
            return meta["content"][:10]

    # time要素
    time_tag = soup.find("time")
    if time_tag:
        dt = time_tag.get("datetime") or time_tag.get_text(strip=True)
        if dt:
            return dt[:10]

    # テキスト内の日付パターン (YYYY-MM-DD / YYYY/MM/DD / Month DD, YYYY)
    text = soup.get_text()
    patterns = [
        r"\b(\d{4}[-/]\d{2}[-/]\d{2})\b",
        r"\b(\w+ \d{1,2},? \d{4})\b",
    ]
    for pat in patterns:
        m = re.search(pat, text)
        if m:
            return m.group(1)

    return ""


def extract_publisher(soup: BeautifulSoup, source_url: str) -> str:
    """metaタグ・OGP・ドメインからpublisherを推定する。"""
    for meta_name in ["og:site_name", "publisher", "author"]:
        meta = soup.find("meta", attrs={"property": meta_name}) or \
               soup.find("meta", attrs={"name": meta_name})
        if meta and meta.get("content"):
            return meta["content"]

    # ドメインをフォールバックとして使用
    from urllib.parse import urlparse
    parsed = urlparse(source_url)
    return parsed.netloc


def sha256_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def detect_language(text: str) -> str:
    """テキストの言語を簡易判定する（中国語・日本語・英語）。"""
    cjk_count = sum(1 for c in text if "一" <= c <= "鿿")
    hiragana = sum(1 for c in text if "぀" <= c <= "ゟ")
    katakana = sum(1 for c in text if "゠" <= c <= "ヿ")
    if hiragana + katakana > 50:
        return "ja"
    if cjk_count > 100:
        return "zh"
    return "en"


def normalize_html_file(
    html_path: Path, log_entry: dict, date: str
) -> dict | None:
    """1つのHTMLファイルを正規化してdictを返す。"""
    try:
        content = html_path.read_bytes()
        soup = BeautifulSoup(content, "lxml")
    except Exception as e:
        print(f"  WARN: cannot parse {html_path}: {e}", file=sys.stderr)
        return None

    body_text = extract_body_text(soup)
    if not body_text.strip():
        return None

    return {
        "company_id": log_entry.get("company_id", "unknown"),
        "date_collected": date,
        "source_url": log_entry.get("url", ""),
        "source_type": log_entry.get("group", ""),
        "publisher": extract_publisher(soup, log_entry.get("url", "")),
        "published_date": extract_published_date(soup),
        "title": extract_title(soup) or log_entry.get("title", ""),
        "body_text": body_text,
        "language": detect_language(body_text),
        "hash": sha256_hash(body_text),
    }


def load_existing_normalized(out_path: Path) -> list[dict]:
    if out_path.exists():
        with open(out_path, encoding="utf-8") as f:
            return json.load(f)
    return []


def main():
    # 処理対象日: 引数があれば使用、なければ今日
    if len(sys.argv) >= 2:
        date = sys.argv[1]
    else:
        date = datetime.now().strftime("%Y-%m-%d")

    date_raw_dir = RAW_DIR / date
    if not date_raw_dir.exists():
        print(f"ERROR: {date_raw_dir} が存在しません。先にfetch_sources.pyを実行してください。")
        sys.exit(1)

    print(f"=== normalize_sources.py | date={date} ===")

    fetch_log = load_fetch_log(date_raw_dir)
    # key: relative path (str) -> log entry

    # company_id ごとに正規化データをまとめる
    results_by_company: dict[str, list[dict]] = {}

    html_files = sorted(date_raw_dir.rglob("*.html"))
    print(f"HTML files found: {len(html_files)}")

    for html_path in html_files:
        rel_path = str(html_path.relative_to(BASE_DIR))
        log_entry = fetch_log.get(rel_path, {})
        if not log_entry:
            # fetch_logにないファイルはディレクトリ名をcompany_idに使う
            company_id = html_path.parent.name
            log_entry = {"company_id": company_id, "url": "", "group": "unknown"}

        company_id = log_entry.get("company_id", html_path.parent.name)
        print(f"  Normalizing: {rel_path} ({company_id})")

        normalized = normalize_html_file(html_path, log_entry, date)
        if normalized:
            results_by_company.setdefault(company_id, []).append(normalized)

    # 保存
    date_norm_dir = NORMALIZED_DIR / date
    date_norm_dir.mkdir(parents=True, exist_ok=True)

    for company_id, items in results_by_company.items():
        out_path = date_norm_dir / f"{company_id}.json"
        existing = load_existing_normalized(out_path)
        # 重複排除: hashが既存にあるものはスキップ
        existing_hashes = {e["hash"] for e in existing}
        new_items = [it for it in items if it["hash"] not in existing_hashes]
        merged = existing + new_items
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(merged, f, ensure_ascii=False, indent=2)
        print(f"  -> {out_path.name}: {len(new_items)} new items (total {len(merged)})")

    print(f"\n=== Done: {sum(len(v) for v in results_by_company.values())} items normalized ===")


if __name__ == "__main__":
    main()
