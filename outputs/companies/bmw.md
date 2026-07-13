# BMW — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3-T（Alexa+ ・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ iX3 欧州量産進行（Debrecen工場）、初顧客納車 2026.3 開始、欧州50K受注超。米国生産 Q1 2026開始、夏配備。Alexa+ ロールアウトは 2026下期独・米から（OS9/Xスマートな車）
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ BMW 公式（2026.1.26）+ Press release

---

## 1. エグゼクティブサマリ

BMW は Amazon Alexa+（70+LLM 背後の Bedrock 構成）を iX3（Neue Klasse 第1号）で 2026下期量産投入。独・米先行。BMW IPA（Intelligent Personal Assistant）と Alexa+ のハイブリッド構成。AWS との戦略提携で Bedrock 基盤を共同構築。iX3 は2026.1 出荷時点で50K 受注超。Alexa+ は唯一の OEM 採用 FM プラットフォームで、Honda にとって「Alexa+ vs Gemini vs Cerence xUI」の比較材料。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | iX3（Neue Klasse 第1号、2026.1出荷50K受注超）[一次] |
| 量産時期 | Alexa+ 2026下期（独・米）[一次] |
| 対象国 | 独・米先行、グローバル順次 [一次] |
| AI Agent搭載総台数 | Neue Klasse 全車（数百万台規模）[推論] |
| FM Level | A（Alexa+ Bedrock 70+LLM、API利用）|
| 主要採用FM | Amazon Alexa+（70+LLM背後、Bedrock構成）[一次] |
| 採用Orchestrator | BMW IPA + Alexa+ ハイブリッド [一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：高級 EV/Premium [一次]
- 旗艦モデルの市場定位：iX3 が Neue Klasse 第1号、2026.1 出荷時点 50K 受注超
- 量産時期と地域戦略：独・米先行、ガソリン車・中国向けは順次 [推論]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事 + 家連結（Alexa+ 70+LLM 活用）[一次] |
| 体験の深さ | Tool Use + 多段階対話 [一次] |
| 個別最適化度 | 家のスマートデバイス連結（Amazon Echo 連携）[一次] |

UXシナリオ要約：
家での会話を車で継続、音楽/ナビ/家セキュリティ操作を一括で行う。LLMベースで複雑質問対応、vehicle function + general knowledge 統合 [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-T、Multi-Agent 空欄（Alexa+ 単一、ただし背後で 70+LLM）[一次]
- 分類根拠：Alexa+ + Bedrock 外部依存。BMW IPA は独自継続するが補完的位置づけ [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用型、Alexa+ Bedrock 経由）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Amazon Alexa+（70+LLM背後、Bedrock構成）[一次] |
| 採用Orchestrator | BMW IPA + Alexa+ ハイブリッド [一次] |
| 採用ミドルウェア（IVI OS）| BMW Operating System 9（QNX系、Android Automotive OS 9 採用）[推論] |
| 採用チップ（SoC）| Qualcomm Snapdragon Cockpit Elite [一次] |
| R&D投資規模（AI関連年額）| AWS との戦略提携（Bedrock基盤、Alexa+ 共同）[一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Amazon（Alexa+, Bedrock 70+LLM）|
| Orchestrator提供 | BMW IPA（自社）+ Alexa+（外部）|
| Chip提供 | Qualcomm Snapdragon Cockpit Elite |
| データ・地図提供 | [未特定] |
| ADAS提供 | Momenta（iX3 China、End-to-End、2026年末量産）+ NVIDIA Orin系 [一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 2026下期（Alexa+ iX3）|
| a-2 ナビ・ルート | 実装済 |
| a-3 コックピット制御 | 部分実装 |
| a-4 乗員ケア | 無 |
| a-5 コマース | 2026下期（Alexa+ Home連結）|

- 2027予測：P3-T 継続（Neue Klasse 全車展開）
- 2030予測：P3-E（Alexa+ 多地域量産確立）

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- Alexa+（70+LLM 背後の Bedrock 構成）は「単一プラットフォーマー経由で多LLM を横串使い」する戦略。Honda が Gemini 単一依存から Multi-LLM へ移行する際の参照モデル
- BMW IPA + Alexa+ のハイブリッドは「自前Orch + 外部Orch」の二段構え。Honda の ASIMO OS + Gemini と異なる発想

### 6.2 警鐘 or 注意点
- Alexa+ は唯一の OEM 採用で、Amazon側の戦略変更時に代替手段が乏しい。Cerence xUI の汎用化路線とは対照的

### 6.3 Honda の現在地との差分
Honda P2-T と BMW P3-T の差は Orch 内製度合い。BMW は IPA を残しつつ Alexa+ に依存度高、Honda は ASIMO OS で Orch 自前を堅持。Multi-LLM 化の方向では BMW（70+LLM 背後）が先行。

---

## 7. [未特定] 残課題

- BMW Alexa+ の Tool Use 数 / 70+LLM の構成（理由：Bedrock基盤は確認、各LLM の役割分担は非公開）
- iX3 China（2026年末 Momenta 量産）と独・米向け（Alexa+）の機能差（理由：[未特定]）
- Alexa+ の他 BMW モデル展開時期（理由：iX3 のみ確認）


## 直近アップデート
- 2026-05-11: Neue Klasse Auto China 2026でお披露目。新世代EV/ソフトウェアプラットフォーム。 ([出典](https://electriccarsreport.com/2026/04/bmw-ix3-long-wheelbase-and-i3-long-wheelbase-unveiled-in-beijing/))

### 2026-05-13
- 事実：BMW CEO Zipse が iX3（Neue Klasse第1弾）を発表。ソフトウェア中心「Superbrain Architecture」で現行比20倍の演算能力。中国EV・Tesla対抗策
- 出典：https://www.cnbc.com/2025/09/05/bmw-doubles-down-on-software-to-take-on-tesla-chinese-ev-rivals.html
- 発表日：2025-09-05
- 確度：中（industry_media）
- 2026-07-14: 米国販売増加もEVは苦戦。[InsideEVs 2026-07-12] ([出典](https://www.cnbc.com/2025/09/05/bmw-doubles-down-on-software-to-take-on-tesla-chinese-ev-rivals.html))
