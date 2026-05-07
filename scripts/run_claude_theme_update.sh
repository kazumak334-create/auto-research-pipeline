#!/usr/bin/env bash
# run_claude_theme_update.sh
# 論点別リサーチノートをClaude Code headlessで更新する。
#
# 実行方法 (Windows Git Bash):
#   bash scripts/run_claude_theme_update.sh [YYYY-MM-DD]
#
# 前提:
#   - claude コマンドがPATHに存在すること (Claude Code CLI)
#   - 作業ディレクトリがリポジトリルートであること
#   - run_claude_company_update.sh が完了していること

set -euo pipefail

DATE=${1:-$(date +%F)}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
PROMPT_FILE="${REPO_ROOT}/prompts/update_theme_research.md"

echo "=== run_claude_theme_update.sh | date=${DATE} ==="
echo "Repo root: ${REPO_ROOT}"

cd "${REPO_ROOT}"

claude \
  --print \
  --allowedTools "Read,Write,Edit,Bash(git diff *)" \
  --output-format text \
  "$(cat << EOF
対象日: ${DATE}

$(cat "${PROMPT_FILE}")
EOF
)"

echo ""
echo "=== Done: theme update completed ==="
