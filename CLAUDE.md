# CLAUDE.md

## プロジェクト概要

このプロジェクトは、中国OEM・Tier1・BigTech・関連プレイヤーの自動車産業進出情報を継続的に収集・整理・更新するためのリサーチ基盤である。

## 絶対遵守

- ハルシネーション禁止。
- 不明な点は不明と書く。
- 推測を事実として書かない。
- 事実・仮説・評価を分離する。
- 出典URL、発表主体、発表日を必ず残す。
- 一次情報を優先する。
- 二次情報のみの場合は確度を下げる。
- 中国市場の事例をASEAN・日本・欧米に安易に一般化しない。
- "採用"という表現は、技術採用、部品採用、OS採用、アプリ採用、クラウド採用、共同開発、実証実験、発表のみ等に分解する。
- 既存Markdownの重要情報を勝手に削除しない。
- 矛盾する情報がある場合は、削除ではなく「更新・訂正」として扱う。

## 編集方針

- outputs/companies/*.md は企業別のファクト・仮説管理ファイルである。
- outputs/themes/*.md は論点別の横比較ファイルである。
- outputs/update_logs/*.md は監査ログである。
- 更新時は必ず更新理由と出典を残す。
- 出典のない断定を追加しない。

## 主要論点

- 顧客接点を取られる
- 車両データを取られる
- 差別化領域を外部依存する
- OEM独自領域まで侵攻する
- InCar / OutCar / Cloud / Dataのレイヤー分解
- ASEAN展開
- トヨタ・既存OEMへの示唆

## ディレクトリ構成

```
auto-research-pipeline/
├── config/              # 監視対象・スコープ・情報源の設定
├── prompts/             # Claude Code headless実行用プロンプト
├── scripts/             # Python・シェルスクリプト
├── data/
│   ├── raw/             # 取得したHTML/PDFのそのまま保存
│   ├── normalized/      # 正規化済みJSON（本文・メタデータ）
│   └── diff/            # 新規・更新ありの差分JSON
├── outputs/
│   ├── companies/       # 企業別リサーチノート（Claude Codeが更新）
│   ├── themes/          # 論点別リサーチノート（Claude Codeが更新）
│   └── update_logs/     # 更新ログ（Claude Codeが作成）
└── .github/workflows/   # GitHub Actions（週次実行雛形）
```

## 実行フロー

```bash
python scripts/fetch_sources.py          # 情報収集
python scripts/normalize_sources.py     # 本文正規化
python scripts/detect_diff.py           # 差分検知
bash scripts/run_claude_company_update.sh  # 企業別MD更新
bash scripts/run_claude_theme_update.sh    # 論点別MD更新
```

## Claude Codeへの制約

- data/raw/ には書き込まない（fetch_sources.pyが管理）
- data/normalized/ には書き込まない（normalize_sources.pyが管理）
- data/diff/ には書き込まない（detect_diff.pyが管理）
- outputs/ 配下のみ書き込む
- 既存Markdownの構造を維持する
- 更新後は必ず更新ログを outputs/update_logs/ に作成する
