#!/usr/bin/env python3
"""
push_to_github.py

git push を使わず GitHub Contents API 経由でファイルをコミットする。
CCR環境でgit pushがブロックされる場合の代替手段。

使い方:
    python scripts/push_to_github.py <date> <token>
    例: python scripts/push_to_github.py 2026-05-08 ghp_xxxxx

対象ファイル（存在するもののみ）:
    outputs/reports/<date>.md
    outputs/companies/*.md
    outputs/themes/macro-industry.md
"""

import base64
import json
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
REPO = "kazumak334-create/auto-research-pipeline"
BRANCH = "main"
API_BASE = "https://api.github.com"


def github_request(method: str, path: str, token: str, data: dict = None) -> dict:
    """GitHub API へのリクエスト（requests ライブラリ使用）"""
    import requests

    url = f"{API_BASE}{path}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
    }
    resp = getattr(requests, method)(url, headers=headers, json=data, timeout=30)
    return resp.status_code, resp.json() if resp.content else {}


def get_file_sha(token: str, repo_path: str) -> str | None:
    """既存ファイルのSHAを取得（更新時に必要）"""
    status, data = github_request("get", f"/repos/{REPO}/contents/{repo_path}", token)
    if status == 200:
        return data.get("sha")
    return None


def push_file(token: str, local_path: Path, repo_path: str, commit_message: str) -> bool:
    """1ファイルをGitHub Contents APIでコミット"""
    try:
        content = base64.b64encode(local_path.read_bytes()).decode()
        sha = get_file_sha(token, repo_path)

        body = {
            "message": commit_message,
            "content": content,
            "branch": BRANCH,
        }
        if sha:
            body["sha"] = sha

        status, data = github_request(
            "put",
            f"/repos/{REPO}/contents/{repo_path}",
            token,
            body,
        )

        if status in (200, 201):
            print(f"  OK: {repo_path}")
            return True
        else:
            print(f"  NG: {repo_path} → HTTP {status}: {data.get('message', '')}")
            return False
    except Exception as e:
        print(f"  ERR: {repo_path} → {e}")
        return False


def collect_files(date: str) -> list[tuple[Path, str]]:
    """プッシュ対象ファイルを収集して (local_path, repo_path) のリストで返す"""
    files = []

    # ニュースレター
    report = BASE_DIR / "outputs" / "reports" / f"{date}.md"
    if report.exists():
        files.append((report, f"outputs/reports/{date}.md"))

    # 企業別ファクトブック
    companies_dir = BASE_DIR / "outputs" / "companies"
    if companies_dir.exists():
        for md in sorted(companies_dir.glob("*.md")):
            files.append((md, f"outputs/companies/{md.name}"))

    # テーマMD（macro-industry.md + pest-*.md）
    themes_dir = BASE_DIR / "outputs" / "themes"
    if themes_dir.exists():
        for md in sorted(themes_dir.glob("*.md")):
            files.append((md, f"outputs/themes/{md.name}"))

    return files


def main():
    if len(sys.argv) < 3:
        print("Usage: push_to_github.py <date> <github_token>")
        sys.exit(1)

    date = sys.argv[1]
    token = sys.argv[2]

    files = collect_files(date)
    if not files:
        print("No files to push.")
        sys.exit(0)

    print(f"Pushing {len(files)} files for {date}...")
    commit_message = f"Daily research update: {date}"

    ok = 0
    ng = 0
    for local_path, repo_path in files:
        success = push_file(token, local_path, repo_path, commit_message)
        if success:
            ok += 1
        else:
            ng += 1
        time.sleep(0.5)  # GitHub API レート制限対策

    print(f"\nDone: {ok} pushed, {ng} failed")
    if ng > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
