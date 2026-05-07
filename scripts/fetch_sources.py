#!/usr/bin/env python3
"""
fetch_sources.py

config/sources.yaml を読み込み、各URLにHTTPリクエストを送信して
data/raw/YYYY-MM-DD/{company_id}/ 以下に保存する。
PDFリンクが見つかった場合はPDFも保存する。
失敗してもcontinueし、エラーはfetch_log.jsonに記録する。
"""

import hashlib
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
import yaml
from bs4 import BeautifulSoup

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_SOURCES = BASE_DIR / "config" / "sources.yaml"
RAW_DIR = BASE_DIR / "data" / "raw"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}
TIMEOUT = 20
REQUEST_INTERVAL = 1.5  # seconds between requests to avoid rate limiting


def load_sources() -> dict:
    with open(CONFIG_SOURCES, encoding="utf-8") as f:
        return yaml.safe_load(f)


def get_company_id_for_url(sources: dict, url: str, group_name: str) -> str:
    """URLに対応するcompany_idを返す。government_regulatorはregion名を使う。"""
    group = sources["source_groups"].get(group_name, {})
    for entry in group.get("sources", []):
        if isinstance(entry, dict):
            if "urls" in entry and url in entry["urls"]:
                return entry.get("company_id") or entry.get("region", "unknown")
        elif isinstance(entry, str):
            if entry == url:
                return "industry_media"
    return "unknown"


def fetch_url(url: str, session: requests.Session) -> tuple[bytes | None, str, int]:
    """URLをフェッチし (content, content_type, status_code) を返す。"""
    try:
        resp = session.get(url, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
        return resp.content, resp.headers.get("Content-Type", ""), resp.status_code
    except Exception as e:
        print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
        return None, "", 0


def save_file(dest_dir: Path, filename: str, content: bytes) -> Path:
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / filename
    dest.write_bytes(content)
    return dest


def extract_title(html: bytes) -> str:
    try:
        soup = BeautifulSoup(html, "lxml")
        tag = soup.find("title")
        return tag.get_text(strip=True) if tag else ""
    except Exception:
        return ""


def find_pdf_links(html: bytes, base_url: str) -> list[str]:
    """HTML内のPDFリンクを抽出する。"""
    try:
        soup = BeautifulSoup(html, "lxml")
        links = []
        for a in soup.find_all("a", href=True):
            href = a["href"]
            if href.lower().endswith(".pdf"):
                abs_url = urljoin(base_url, href)
                links.append(abs_url)
        return links[:5]  # 最大5件に制限
    except Exception:
        return []


def build_url_list(sources: dict) -> list[dict]:
    """全URLを (url, company_id, group_name) のリストに展開する。"""
    items = []
    for group_name, group in sources["source_groups"].items():
        for entry in group.get("sources", []):
            if isinstance(entry, dict):
                company_or_region = entry.get("company_id") or entry.get("region", "unknown")
                for url in entry.get("urls", []):
                    items.append({
                        "url": url,
                        "company_id": company_or_region,
                        "group": group_name,
                        "priority": group.get("priority", 2),
                    })
            elif isinstance(entry, str):
                items.append({
                    "url": entry,
                    "company_id": "industry_media",
                    "group": group_name,
                    "priority": group.get("priority", 2),
                })
    return items


def main():
    today = datetime.now().strftime("%Y-%m-%d")
    date_raw_dir = RAW_DIR / today

    sources = load_sources()
    url_list = build_url_list(sources)

    print(f"=== fetch_sources.py | date={today} | targets={len(url_list)} URLs ===")

    fetch_log = []
    session = requests.Session()

    for i, item in enumerate(url_list, 1):
        url = item["url"]
        company_id = item["company_id"]
        group = item["group"]

        print(f"[{i}/{len(url_list)}] {company_id} | {url}")

        content, content_type, status = fetch_url(url, session)
        log_entry = {
            "url": url,
            "company_id": company_id,
            "group": group,
            "status_code": status,
            "content_type": content_type,
            "timestamp": datetime.now().isoformat(),
            "title": "",
            "saved_path": "",
            "pdf_links_saved": [],
            "error": None,
        }

        if content is None or status == 0:
            log_entry["error"] = f"fetch failed (status={status})"
            fetch_log.append(log_entry)
            time.sleep(REQUEST_INTERVAL)
            continue

        if status >= 400:
            log_entry["error"] = f"HTTP {status}"
            fetch_log.append(log_entry)
            time.sleep(REQUEST_INTERVAL)
            continue

        dest_dir = date_raw_dir / company_id
        ext = ".pdf" if "pdf" in content_type.lower() else ".html"
        filename = f"source_{i:03d}{ext}"

        saved = save_file(dest_dir, filename, content)
        log_entry["saved_path"] = str(saved.relative_to(BASE_DIR))

        if ext == ".html":
            log_entry["title"] = extract_title(content)
            # PDFリンクを検索して保存
            pdf_urls = find_pdf_links(content, url)
            for j, pdf_url in enumerate(pdf_urls, 1):
                print(f"  -> PDF: {pdf_url}")
                pdf_content, _, pdf_status = fetch_url(pdf_url, session)
                if pdf_content and pdf_status < 400:
                    pdf_filename = f"source_{i:03d}_pdf_{j:02d}.pdf"
                    pdf_saved = save_file(dest_dir, pdf_filename, pdf_content)
                    log_entry["pdf_links_saved"].append(str(pdf_saved.relative_to(BASE_DIR)))
                time.sleep(REQUEST_INTERVAL)

        fetch_log.append(log_entry)
        time.sleep(REQUEST_INTERVAL)

    # ログ保存
    log_path = date_raw_dir / "fetch_log.json"
    date_raw_dir.mkdir(parents=True, exist_ok=True)
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(fetch_log, f, ensure_ascii=False, indent=2)

    success = sum(1 for e in fetch_log if not e["error"])
    print(f"\n=== Done: {success}/{len(fetch_log)} succeeded. Log -> {log_path} ===")


if __name__ == "__main__":
    main()
