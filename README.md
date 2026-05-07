# auto-research-pipeline

中国OEM・Tier1・BigTech各社の自動車産業進出情報を継続的に収集・差分検知・Markdown更新するパイプライン。

Claude Code hooksを使わず、Python（収集・差分検知）→ Claude Code headless（Markdown更新）→ GitHub PR（人間レビュー）のアーキテクチャ。

---

## セットアップ

### 前提

- Python 3.11+
- Git
- Claude Code CLI（`claude` コマンドがPATHに存在すること）
- Git Bash（Windows環境でシェルスクリプトを実行する場合）

### インストール

```bash
cd auto-research-pipeline
pip install -r requirements.txt
```

---

## ローカル実行手順（MVP）

```bash
# 1. 情報収集（config/sources.yaml に定義されたURLをフェッチ）
python scripts/fetch_sources.py

# 2. 本文正規化
python scripts/normalize_sources.py

# 3. 差分検知
python scripts/detect_diff.py

# 4. 企業別Markdown更新（Claude Code headless）
bash scripts/run_claude_company_update.sh

# 5. 論点別Markdown更新（Claude Code headless）
bash scripts/run_claude_theme_update.sh
```

特定日付を指定する場合：

```bash
python scripts/fetch_sources.py
python scripts/normalize_sources.py 2026-05-07
python scripts/detect_diff.py 2026-05-07
bash scripts/run_claude_company_update.sh 2026-05-07
bash scripts/run_claude_theme_update.sh 2026-05-07
```

---

## ディレクトリ構成

```
auto-research-pipeline/
├── README.md
├── CLAUDE.md                    # Claude Code向け方針・制約
├── requirements.txt
├── config/
│   ├── companies.yaml           # 監視対象企業（11社）
│   ├── research_scope.yaml      # 調査スコープ・論点・出力原則
│   └── sources.yaml             # 情報源URL一覧
├── prompts/
│   ├── update_company_research.md   # 企業別更新プロンプト
│   └── update_theme_research.md     # 論点別更新プロンプト
├── scripts/
│   ├── fetch_sources.py         # URLからHTMLを収集
│   ├── normalize_sources.py     # HTML→正規化JSON
│   ├── detect_diff.py           # 差分検知
│   ├── run_claude_company_update.sh  # 企業別MD更新（claude CLI）
│   ├── run_claude_theme_update.sh    # 論点別MD更新（claude CLI）
│   └── create_pr.sh             # PR作成（手動実行用）
├── data/
│   ├── raw/YYYY-MM-DD/{company_id}/  # 収集したHTML/PDF
│   ├── normalized/YYYY-MM-DD/        # 正規化JSON
│   └── diff/YYYY-MM-DD/             # 差分JSON
├── outputs/
│   ├── companies/               # 企業別リサーチノート（Claude Codeが更新）
│   ├── themes/                  # 論点別リサーチノート（Claude Codeが更新）
│   └── update_logs/             # 更新ログ（Claude Codeが作成）
└── .github/
    └── workflows/
        └── weekly-research-update.yml  # 週次自動実行（雛形）
```

---

## 監視対象企業

| ID | 企業名 | カテゴリ |
|---|---|---|
| huawei | Huawei | 中国テック・Tier1-like |
| xiaomi | Xiaomi | 中国テック・中国OEM |
| byd | BYD | 中国OEM・バッテリー |
| geely | Geely | 中国OEM・モビリティグループ |
| saic | SAIC | 中国OEM・国有企業 |
| chery | Chery | 中国OEM |
| baidu | Baidu | 中国テック・自動運転・AI |
| tencent | Tencent | 中国テック・クラウド |
| alibaba | Alibaba | 中国テック・クラウド・OS |
| bytedance | ByteDance | 中国テック・コンテンツ |
| toyota | Toyota | 日本OEM（ベンチマーク） |

---

## 主要論点

- 顧客接点を取られる（customer_touchpoint）
- 車両データを取られる（vehicle_data）
- 差別化領域を外部依存する（differentiation_dependency）
- OEM独自領域まで侵攻する（oem_domain_invasion）
- InCar / OutCar / Cloud レイヤー分解（incar_outcar_cloud）
- ASEAN展開・規制（asean_regulation）
- 中国BigTechの進出パターン（china_bigtech_auto_entry）

---

## GitHub Actions（週次自動実行）

`.github/workflows/weekly-research-update.yml` に雛形あり。

利用するには以下のSecretsをGitHub Repositoryに設定する：

- `ANTHROPIC_API_KEY` : Claude Code CLI用のAnthropicAPIキー

---

## 設計方針

- Claude Code hooksは使わない
- PythonがWebを収集し、差分のみをClaude Codeに渡す
- Claude Codeは分析・編集エンジンとして使う（クローリング制御・Git管理はPython・shell側）
- 出典URL・発表主体・発表日を必ず保持する
- 公式情報と二次情報を区別する
- 既存Markdownを壊さず、追記・更新ログ方式を維持する
