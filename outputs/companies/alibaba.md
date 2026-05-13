# Alibaba 自動車産業関連アップデート

## 1. 企業概要

| 項目 | 内容 |
|---|---|
| 企業名 | Alibaba Group Holding Limited（阿里巴巴集団） |
| 本社 | 杭州、中国 |
| カテゴリ | 中国テック / クラウド / OS |
| 自動車関連ブランド | Banma（斑馬）、AliOS、Alibaba Cloud |

## 2. 自動車産業への関与領域

| 領域 | 内容 | 確度 | 根拠 |
|---|---|---:|---|
| InCar | AliOS for Car（AliOS Drive）、Banmaコックピット | 高 | 公式発表 |
| OutCar | Alipay・Taobao連携（購買・決済接点） | 高 | 公式発表 |
| Cloud / Data | Alibaba Cloud for Automotive | 高 | 公式発表 |
| ADAS / 自動運転 | 自社ADASなし（クラウド基盤のみ） | 高 | 公式発表 |
| Cockpit / Infotainment | Banma Cockpit、Alipay車内決済 | 高 | 公式発表 |
| Sales / CRM / 顧客接点 | Tmall Automotive（天猫汽车）での車販売接点 | 高 | 公式発表 |
| After-sales / OTA | Alibaba Cloudを通じたOTAサポート（推定） | 中 | 推定 |

## 3. OEM侵食リスク評価

| 論点 | 評価 | 理由 | 根拠 | 確度 |
|---|---|---|---|---|
| 顧客接点を取るか | 高リスク | Tmall Automotive・Alipay車内決済で購買接点を取得 | 公式発表 | 高 |
| 車両データを取るか | 高リスク | AliOS経由の利用ログ・位置情報をAlibaba Cloudが収集しうる | 推定 | 中 |
| 差別化領域を外部依存させるか | 高リスク | AliOS採用OEMはOS・決済・コンテンツをAlibaba依存 | 公式発表 | 高 |
| OEM独自領域まで侵攻するか | 低リスク | 現時点でOEM製造への参入なし | — | 高 |

## 4. ASEAN・海外展開

| 地域 | 内容 | 根拠 | 確度 |
|---|---|---|---|
| Thailand | Alibaba Cloudのタイ展開あり | 公式発表 | 高 |
| Indonesia | Alibaba Cloud・Lazada（EC）展開 | 公式発表 | 高 |
| Malaysia | Alibaba Cloud展開 | 公式発表 | 高 |
| Singapore | Alibaba Cloud シンガポールリージョンあり | 公式発表 | 高 |
| Japan | Alibaba Cloud 日本リージョンあり | 公式発表 | 高 |
| Europe | GDPR対応で展開規模は限定的 | 推定 | 中 |
| United States | 安全保障規制リスク大 | 公式規制情報 | 高 |

## 5. トヨタ・既存OEMへの示唆

- Alibaba CloudのASEAN展開は、将来的にASEAN向けEVのコックピット・クラウド基盤として使われるリスクがある。
- Tmall Automotiveは中国市場の車購買ファネルをOEMから切り離す構造であり、日本OEMにとっても参照事例。

## 6. 直近アップデート

<!-- Claude Code が新規情報を追記する際はこのセクションに追記すること -->

## 7. 未確認・要追加調査

- AliOS DriveのASEAN向け展開計画
- Banmaの採用OEM一覧・採用範囲（OS採用か、アプリ採用か）
- Alibaba Cloud Automotiveの日本OEM向け提供状況

## 8. 更新ログ

| 日付 | 更新内容 | 更新者 |
|---|---|---|
| 2026-05-07 | 初期テンプレート作成 | system |


## 直近アップデート
- 2026-05-11: Auto China 2026：Qwen が複数OEMの車内AI基盤として展開。Xiaomi/HIMA連携。 ([出典](https://www.marklines.com/en/report/rep3006_202604))

### 2026-05-13
- 事実：Qwen AI が BYD・Geely・Li Auto・Changan・Dongfeng等の車内システムに統合、NVIDIA車載チップ上で動作し音声で食事注文・ホテル予約等が可能に
- 出典：https://www.cnbc.com/2026/04/24/alibaba-qwen-ai-integration-chinese-carmakers-beijing-auto-show.html
- 発表日：2026-04-24
- 確度：中（industry_media）
