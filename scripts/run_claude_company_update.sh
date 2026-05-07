#!/usr/bin/env bash
# run_claude_company_update.sh
# 企業別リサーチノートをClaude Code headlessで更新する。
#
# 実行方法 (Windows Git Bash):
#   bash scripts/run_claude_company_update.sh [YYYY-MM-DD]
#
# 前提:
#   - claude コマンドがPATHに存在すること (Claude Code CLI)
#   - 作業ディレクトリがリポジトリルートであること
#   - data/diff/YYYY-MM-DD/ 配下にdiffファイルが存在すること

set -euo pipefail

DATE=${1:-$(date +%F)}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PROMPT_FILE="${REPO_ROOT}/prompts/update_company_research.md"

COMPANIES=(
  huawei
  xiaomi
  byd
  geely
  saic
  chery
  baidu
  tencent
  alibaba
  bytedance
  toyota
)

echo "=== run_claude_company_update.sh | date=${DATE} ==="
echo "Repo root: ${REPO_ROOT}"

cd "${REPO_ROOT}"

for COMPANY_ID in "${COMPANIES[@]}"; do
  DIFF_FILE="data/diff/${DATE}/${COMPANY_ID}.json"

  # diffファイルが存在しない場合はスキップ
  if [[ ! -f "${DIFF_FILE}" ]]; then
    echo "[SKIP] ${COMPANY_ID}: diff file not found (${DIFF_FILE})"
    continue
  fi

  # new_itemsが0件の場合はスキップ（差分なし）
  NEW_COUNT=$(python3 -c "
import json, sys
with open('${DIFF_FILE}') as f:
    d = json.load(f)
print(len(d.get('new_items', [])) + len(d.get('updated_items', [])))
" 2>/dev/null || echo "0")

  if [[ "${NEW_COUNT}" == "0" ]]; then
    echo "[SKIP] ${COMPANY_ID}: no new/updated items"
    continue
  fi

  echo ""
  echo "[UPDATE] ${COMPANY_ID} (${NEW_COUNT} new/updated items)"

  claude \
    --print \
    --allowedTools "Read,Write,Edit,Bash(git diff *)" \
    --output-format text \
    "$(cat << EOF
対象日: ${DATE}
対象企業ID: ${COMPANY_ID}

$(cat "${PROMPT_FILE}")
EOF
)"

done

echo ""
echo "=== Done: company update completed ==="
