# BYD — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3-E（DeepSeek + 自社 + Cerence・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026 グローバル販売 688,939台、海外比率 50%超（3月単月 海外 120,083台 +65% YoY）。**2026 海外目標 1.5M台**（前回 1.3M から上方修正、2025年 900K-1M の倍化）。欧州・中南米・東南アジア加速展開
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CnEVPost + Tridens + Bloomberg

---

## 1. エグゼクティブサマリ

BYD は Xuanji AI（自社、2024.1 発表）+ DeepSeek R1（2025.2 全21モデル一斉統合）+ Cerence xUI（ATTO 2 DM-i 2026春から海外モデル先行）の三層構成。God's Eye（DiPilot 100/300/600）を21モデルに無料展開。Midea 提携（2025.11）で Human-Car-Home 戦略開始。Qwen を 2026.4 北京モーターショーで発表（ホテル/観光/フード/荷物予約 = 商流統合）。中国OEM 最大の量産規模で Multi-Agent 化を進めた事例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | ATTO 2 DM-i（Cerence xUI 2026春）+ 全21モデル God's Eye [一次] |
| 量産時期 | DeepSeek 2025.2全展開、Cerence xUI ATTO 2 から 2026春 [一次] |
| 対象国 | 中国（God's Eye）+ グローバル（Cerence xUI 海外モデル先行）[一次] |
| AI Agent搭載総台数 | 全21モデル God's Eye 無料展開（数百万台規模）[推論] |
| FM Level | B+C（自社 Xuanji + DeepSeek 借用 + Cerence CaLLM）|
| 主要採用FM | DeepSeek R1 + Xuanji 自社 + Qwen + Cerence CaLLM [一次] |
| 採用Orchestrator | 自社 Xuanji AI + Cerence xUI（並走）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆〜高級（Yangwang U8 等）[一次]
- 旗艦モデルの市場定位：ATTO 2 DM-i が Cerence xUI 第1号（海外向け）、God's Eye 全21モデル無料展開
- 量産時期と地域戦略：中国 = DeepSeek + Xuanji、海外 = Cerence xUI 先行 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | コマース・家連結（Qwen + Midea 提携）+ ナビ強化 [一次] |
| 体験の深さ | Tool Use 300+ 車両シナリオ（Xuanji LLM）[一次] |
| 個別最適化度 | Midea 連携で家電・車内機能横断制御 [一次] |

UXシナリオ要約：
"Hotel 予約・観光チケット・フードデリバリー・荷物追跡" を Qwen で車内完結 [一次]。Xuanji が 300以上の車両シナリオを音声指示で制御。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-E × Multi-Agent ◎
- 分類根拠：Xuanji（自社）+ DeepSeek（外部）+ Qwen（外部）+ Cerence xUI（外部）の三層四FM 並走 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：B+C（自社 Xuanji LLM + DeepSeek 借用 Fine-tune）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | DeepSeek R1 + Xuanji 自社 + Qwen + Cerence CaLLM [一次] |
| 採用Orchestrator | 自社 Xuanji AI + Cerence xUI（並走）[一次] |
| 採用ミドルウェア（IVI OS）| DiLink + HarmonyOS（一部）+ Cerence xUI [推論] |
| 採用チップ（SoC）| BYD9000（自社、4nm 開発中）+ Horizon Journey 6 [一次/推論] |
| R&D投資規模（AI関連年額）| Hesai LiDAR + 自社チップ Xuanji 全社共通基盤 [一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | DeepSeek + Alibaba Qwen + Cerence + 自社 Xuanji |
| Orchestrator提供 | 自社 Xuanji + Cerence xUI |
| Chip提供 | 自社 BYD9000（開発中）+ NVIDIA Orin-X + Horizon Journey 6 |
| データ・地図提供 | Amap / Baidu Maps [推論] |
| ADAS提供 | God's Eye（DiPilot 100/300/600、自前）[一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（DeepSeek + Cerence xUI 2026春）|
| a-2 ナビ・ルート | 実装済（God's Eye）|
| a-3 コックピット制御 | 実装済（Xuanji 全社基盤）|
| a-4 乗員ケア | [未特定] |
| a-5 コマース | 実装済（Qwen 2026.4：ホテル/観光/フード/荷物）[一次] |

- 2027予測：P3-E 継続（God's Eye L3 認証取得後の量産）
- 2030予測：P1-E（自社チップ BYD9000 量産後、垂直統合度上昇）

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 「自社FM + 外部FM 多重」の Multi-Agent 量産事例。Honda の Gemini 単一からの Multi-Agent 移行設計の参照
- Cerence xUI 海外モデル先行は「中国OEM の海外展開時の汎用 IVI 基盤」として現実解。Honda が中国 OEM の海外進出ペースを見極める指標
- God's Eye 無料展開は ADAS の標準装備化を加速。Honda が Helm.ai を全車標準化する戦略の正当性を補強

### 6.2 警鐘 or 注意点
- BYD は中国OEM 最大規模（21モデル）で Agentic AI 量産化。Honda 0 Series 単独では規模で対抗困難
- Midea 提携で Human-Car-Home 戦略を BYD が実装。Honda が日系家電（Sony/Panasonic 等）と組まない限り、エコシステム差で劣後

### 6.3 Honda の現在地との差分
Honda P2-T（ASIMO OS + Gemini）と BYD P3-E（Multi-Agent）の差は Multi-Agent 化と量産規模。Honda は単一FM・量産規模ともに劣後。

---

## 7. [未特定] 残課題

- BYD Cerence xUI と DeepSeek の役割分担（理由：両者並存は確認、機能分担は不明）
- BYD9000 自社チップ量産時期（理由：4nm 開発中、量産年未公表）
- 乗員ケア機能（DMS / 健康モニタ）（理由：Xuanji 公開仕様に明示なし）

## 8. 2026 Q1-Q2 追加ファクト

- **Q1 2026 グローバル販売 688,939台**（海外比率 50%超）[二次]
- 3月単月 海外 120,083台、前年同月比 +65.12%（月間記録更新）[二次]
- **2026 海外目標 1.5M台**（前回 1.3M から上方修正、2025 900K-1M の倍化）[二次]
- 海外販売地域構成：欧州・北米・東南アジアが各約1/3（2025）[二次]
- 欧州強化、ラテンアメリカ・東南アジア加速展開 [二次]

## 出典（2026 Q1追加）

- [CnEVPost — BYD aims for 1.3 million overseas sales in 2026](https://cnevpost.com/2026/01/24/byd-aims-for-1-3-million-overseas-sales-2026/) [二次]
- [Bloomberg / Automotive World — BYD 1.5 million overseas sales](https://www.automotiveworld.com/news/bloomberg-byd-tells-analysts-1-5-million-overseas-sales-in-2026/) [二次]
- [Tridens — BYD Sales by Model and Country (Mar 2026)](https://tridenstechnology.com/byd-sales-statistics/) [二次]


## 直近アップデート
- 2026-05-11: 4月乗用EV31.4万台 (-15.7% YoY) 8ヶ月連続前年比減。輸出13.5万台 (+70%)は過去最高。競合激化。 ([出典](https://www.cnbc.com/2026/05/05/byd-april-sales-exports-china-ev-rivals-leapmotor-zeekr.html))

### 2026-05-13
- 事実：ハンガリー工場（年産30万台予定）での労働問題。China Labor Watchが7日連勤・12-14時間労働・ビザ違反等を告発
- 出典：https://www.visiontimes.com/2026/04/26/chinese-ev-giant-byd-faces-forced-labor-allegations-across-brazil-and-hungary.html
- 発表日：2026-04-26
- 確度：中（industry_media）
- 2026-07-14: Dolphin G PHEV（グローバル初モデル）発表——欧州Bセグメント向け、1.5L+195hp電動、総航続1,000km、$25-30K。[SupercarBlondie 2026-07-12] ([出典](https://supercarblondie.com/byd-dolphin-g-first-global-car-phev/))
