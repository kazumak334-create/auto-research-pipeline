#!/usr/bin/env bash
# create_pr.sh
# 週次リサーチ更新PRを作成する（手動実行用の雛形）。
#
# 前提:
#   - gh (GitHub CLI) がインストールされPATHに存在すること
#   - git remote origin が設定されていること
#   - 更新コミットが作成済みであること
#
# 実行方法:
#   bash scripts/create_pr.sh [YYYY-MM-DD]

set -euo pipefail

DATE=${1:-$(date +%F)}
BRANCH="weekly-research-update-${DATE}"
BASE_BRANCH="main"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
cd "${REPO_ROOT}"

echo "=== create_pr.sh | date=${DATE} | branch=${BRANCH} ==="

# ブランチ作成とpush
git checkout -b "${BRANCH}" 2>/dev/null || git checkout "${BRANCH}"
git add outputs/ data/diff/ data/normalized/
git commit -m "Weekly research update: ${DATE}" || echo "Nothing to commit"
git push -u origin "${BRANCH}"

# PR作成
gh pr create \
  --base "${BASE_BRANCH}" \
  --head "${BRANCH}" \
  --title "Weekly research update: ${DATE}" \
  --body "$(cat << 'EOF'
## 更新概要

中国OEM・Tier1・BigTech・関連プレイヤーの週次リサーチノートを更新しました。

## レビュー観点

- 出典URLは妥当か
- 公式情報と二次情報が混ざっていないか
- 推測が事実として書かれていないか
- 中国市場の情報をASEAN・日本へ過度に一般化していないか
- 既存仮説の更新理由が明確か

## 変更ファイル

- outputs/companies/*.md — 企業別リサーチノート
- outputs/themes/*.md — 論点別リサーチノート
- outputs/update_logs/*.md — 更新ログ
EOF
)"

echo "=== Done: PR created for branch ${BRANCH} ==="
