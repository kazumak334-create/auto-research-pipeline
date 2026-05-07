#!/usr/bin/env python3
"""
detect_diff.py

data/normalized/ 配下の全日付のハッシュと比較し、
当日分の新規・更新アイテムを data/diff/YYYY-MM-DD/{company_id}.json に保存する。
差分がなくても空のdiffファイルを作成する（スキップフラグ用）。
"""

import json
import sys
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
NORMALIZED_DIR = BASE_DIR / "data" / "normalized"
DIFF_DIR = BASE_DIR / "data" / "diff"


def load_json(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def build_past_hash_set(date: str) -> dict[str, dict]:
    """
    過去日付（当日より前）のnormalized dataをすべて読み込み、
    {hash: item} のマップを返す。
    """
    past_hashes: dict[str, dict] = {}
    if not NORMALIZED_DIR.exists():
        return past_hashes

    for date_dir in sorted(NORMALIZED_DIR.iterdir()):
        if not date_dir.is_dir():
            continue
        if date_dir.name >= date:
            continue  # 当日以降はスキップ
        for json_file in date_dir.glob("*.json"):
            items = load_json(json_file)
            for item in items:
                h = item.get("hash", "")
                if h:
                    past_hashes[h] = item
    return past_hashes


def build_past_url_set(date: str) -> dict[str, dict]:
    """
    過去日付のURLマップを返す: {source_url: item}
    """
    past_urls: dict[str, dict] = {}
    if not NORMALIZED_DIR.exists():
        return past_urls

    for date_dir in sorted(NORMALIZED_DIR.iterdir()):
        if not date_dir.is_dir():
            continue
        if date_dir.name >= date:
            continue
        for json_file in date_dir.glob("*.json"):
            items = load_json(json_file)
            for item in items:
                url = item.get("source_url", "")
                if url:
                    past_urls[url] = item
    return past_urls


def classify_items(
    today_items: list[dict],
    past_hashes: dict[str, dict],
    past_urls: dict[str, dict],
) -> tuple[list[dict], list[dict], list[dict]]:
    """
    today_items を new / updated / unchanged に分類する。
    - new: URLもhashも過去に存在しない
    - updated: URLは過去に存在するがhashが異なる（コンテンツ変更）
    - unchanged: hashが過去と同一
    """
    new_items = []
    updated_items = []

    for item in today_items:
        h = item.get("hash", "")
        url = item.get("source_url", "")

        if h in past_hashes:
            # 完全一致 → unchanged（スキップ）
            continue

        if url in past_urls:
            # URLは既知だがhashが変わった → updated
            updated_items.append(item)
        else:
            # 新規URL → new
            new_items.append(item)

    return new_items, updated_items, []


def build_diff_entry(
    company_id: str,
    date: str,
    new_items: list[dict],
    updated_items: list[dict],
) -> dict:
    """仕様書§8.3のdiff JSONフォーマットで返す。"""
    def slim(item: dict) -> dict:
        return {
            "source_url": item.get("source_url", ""),
            "publisher": item.get("publisher", ""),
            "published_date": item.get("published_date", ""),
            "title": item.get("title", ""),
            "summary_hint": item.get("body_text", "")[:300],
            "body_text": item.get("body_text", ""),
            "source_type": item.get("source_type", ""),
            "hash": item.get("hash", ""),
        }

    return {
        "company_id": company_id,
        "date": date,
        "new_items": [slim(i) for i in new_items],
        "updated_items": [slim(i) for i in updated_items],
        "removed_items": [],
    }


def main():
    if len(sys.argv) >= 2:
        date = sys.argv[1]
    else:
        date = datetime.now().strftime("%Y-%m-%d")

    today_norm_dir = NORMALIZED_DIR / date
    if not today_norm_dir.exists():
        print(
            f"ERROR: {today_norm_dir} が存在しません。"
            "先にnormalize_sources.pyを実行してください。"
        )
        sys.exit(1)

    print(f"=== detect_diff.py | date={date} ===")

    past_hashes = build_past_hash_set(date)
    past_urls = build_past_url_set(date)
    print(f"Past hashes loaded: {len(past_hashes)}")

    diff_date_dir = DIFF_DIR / date
    diff_date_dir.mkdir(parents=True, exist_ok=True)

    total_new = 0
    total_updated = 0

    for json_file in sorted(today_norm_dir.glob("*.json")):
        company_id = json_file.stem
        today_items = load_json(json_file)

        new_items, updated_items, _ = classify_items(today_items, past_hashes, past_urls)

        diff = build_diff_entry(company_id, date, new_items, updated_items)
        out_path = diff_date_dir / f"{company_id}.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(diff, f, ensure_ascii=False, indent=2)

        total_new += len(new_items)
        total_updated += len(updated_items)
        print(
            f"  {company_id}: new={len(new_items)} updated={len(updated_items)} "
            f"-> {out_path.name}"
        )

    print(
        f"\n=== Done: total new={total_new} updated={total_updated} | "
        f"diff dir -> {diff_date_dir} ==="
    )

    # 差分がゼロのcompanyについても空ファイルを作成（GitHubActionsのスキップ判定用）
    today_companies = {f.stem for f in today_norm_dir.glob("*.json")}
    written_companies = {f.stem for f in diff_date_dir.glob("*.json")}
    for company_id in today_companies - written_companies:
        out_path = diff_date_dir / f"{company_id}.json"
        diff = build_diff_entry(company_id, date, [], [])
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(diff, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
