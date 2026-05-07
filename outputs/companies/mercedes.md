# Mercedes-Benz — IVI Agentic AI 実装ファクトブック

**Tier：** T1
**分類：** P2-E（B Orch自前 + FM外部・確立）/ Multi-Agent ◎
**最終更新：** 2026-05-01（V4検証完了）
**最終確認：** 2026-05-01 ／ Liquid AI = LFM（Liquid Foundation Models）技術確認。オンデバイス推論・クラウド非依存 = Level B [一次] 確定。コスト規模 = [未特定]。第1量産配備2026下期（北米、高度音声技術）。MB.OS 第3-4世代MBUX 全車 embedded 確認
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Mercedes / Liquid AI 公式（2026.4.23）+ V4 web検証（2026-05-01）

---

## 1. エグゼクティブサマリ

Mercedes は MB.OS を自前 Orchestrator として保有し、FM を Google AI Agent + ChatGPT 4o + Liquid AI（北米向け 2026下期 embedded）の三層 Multi-Agent で並走する。CLA は MMA platform の第1号、量産は欧州 2025・米国 2026 Q1。R&D $6.85B（2025、+13.46%）、AI再教育 $2.2B。Multi-Agent を公式採用宣言した最初のグローバル OEM で、Honda が ASIMO OS で目指す「Orch自前 + FM外部」の最も近い role model となる。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | CLA Sedan（MMA platform, MB.OS 第1号）[一次] |
| 量産時期 | CLA 2025（欧州）/ 2026 Q1（米国）[一次] |
| 対象国 | グローバル（CLA 中国は別仕様 Momenta搭載）[一次] |
| 旗艦年産 | CLA 年産 [未特定]（CLA 2025 旧型販売 約100K台 [推論]）|
| AI Agent搭載総台数 | MMA platform 全車（CLA + GLC EV + GLE EV）2027〜 [推論] |
| FM Level | A（Google/OpenAI API）+ **B 確認**（Liquid AI LFM on-device）[一次] |
| 主要採用FM | Google Cloud Automotive AI Agent (Gemini Vertex) + ChatGPT 4o + Liquid AI LFM [一次] |
| 採用Orchestrator | MB.OS 自前 [一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：高級（CLA 入門〜EQS）[一次]
- 旗艦モデルの市場定位：CLA は MMA platform 第1号、欧州 2025 量産、米国 2026 Q1
- 量産時期と地域戦略：欧米先行、中国は Momenta 搭載別仕様で並走 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事（ナビ+検索+一般会話 3エージェント）[一次] |
| 体験の深さ | Tool Use（POI検索深化、ChatGPT は表層対話）[一次] |
| 個別最適化度 | 履歴学習（MBUX プロファイル）[一次] |

UXシナリオ要約：
"Search what nearby Italian restaurants are good" を Google AI Agent で実行、その後 ChatGPT 4o で世間話に切替える。3エージェント並走を MB.OS が orchestration する [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P2-E × Multi-Agent ◎
- 分類根拠：Orchestrator MB.OS は完全自前、FM は3社並走外部依存。Liquid AI 北米向け embedded（2026下期）で部分内製化進行 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用型、Google + OpenAI）+ **B 確認**（Liquid AI LFM embedded、オンデバイス・クラウド非依存）[一次]
- **Liquid Foundation Models（LFM）の技術特性**（V4 検証確認）：
  - アーキテクチャ：LFM（Liquid Neural Networks ベース。Transformer とは異なる連続時間ダイナミクス系）
  - 特徴：低フットプリント・高効率・オンデバイス推論特化。クラウド接続不要で車内 latency 最小化
  - 用途：高度音声技術（advanced speech）を第1適用領域として北米向けに配備（2026下期）
  - プライバシー：ローカル推論によりユーザーデータのクラウド送信を回避 [一次]
- 6要素配分：
  - アーキテクチャ：外部（Google/OpenAI/Liquid AI LFM）
  - ウェイト：API（Google/OpenAI）+ on-device embedded（Liquid AI LFM）
  - 事前学習データ：外部依存
  - Fine-tuningデータ：[未特定]（Mercedes 車両向け Fine-tune 実施と推定）[推論]
  - 学習インフラ：クラウド（Google Vertex AI / OpenAI）+ Liquid AI 独自（LFM 学習）
  - 推論ランタイム：外部SDK + Liquid AI LFM on-device + MB.OS 内一部
- コスト：[未特定]（多年契約の総額・年額とも非公開）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Google Cloud Automotive AI Agent (Gemini Vertex) + ChatGPT 4o + Liquid AI（北米 2026下期）[一次] |
| 採用Orchestrator | MB.OS 自前 [一次] |
| 採用ミドルウェア（IVI OS） | MB.OS（chip-to-cloud architecture）[一次] |
| 採用チップ（SoC） | NVIDIA Drive AV（CLA Q1 2026 ローンチ）[一次] |
| R&D投資規模（AI関連年額） | 全社 R&D $6.85B（2025、+13.46%）[一次]、AI再教育 $2.2B [一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Google + OpenAI + Liquid AI（3社並走）[一次] |
| Orchestrator提供 | 自社（MB.OS）[一次] |
| Chip提供 | NVIDIA（Drive AV、CLA で初）[一次] |
| データ・地図提供 | Google Maps（Vertex AI 連携）[一次]、HERE 一部 [推論] |
| ADAS提供 | NVIDIA Drive AV + Wayve（Series D 出資）+ Momenta（中国 CLA）[一次] |
| 親グループ（P4のみ）| Mercedes-Benz Group AG（独立）[一次] |

---

## 5. 将来：どこへ向かうか

### 5.1 内製意志（戦略宣言ファクト）
- 公式宣言：MB.OS は「自社開発操作系」明示（CLA で初）[一次]。Liquid AI partnership 2026.4.23発表「embedded in-car intelligence、第1量産配備2026下期」[一次]
- 投資規模：R&D $6.85B（2025、+13.46%）[一次]、AI再教育 $2.2B [一次]、2025-26 で Capex/R&D ピーク後 2026 から減衰計画 [一次]
- 移行ロードマップ：MMA platform 全車（CLA→GLC EV→GLE EV）2025-2027、Multi-Agent Orchestration（Google + ChatGPT + Liquid AI 三層）[一次]
- 動機：差別化（高級ブランド体験）+ 部分データ主権（中国 Momenta 別ライン）

### 5.2 2027/2030 戦略パターン遷移予測
- 現在：P2-E（B Orch自前 + FM外部三層）
- 2027：P2-E（Liquid AI embedded 拡張、北米先行）（確度：中）
- 2030：P2-T or P3-T（Wayve ADAS が Orch 化拡大、Multi-Agent 増加でカオス化リスク）（確度：中）
- 分岐条件：Multi-Agent統合の品質低下→外部一社依存に逆戻り

### 5.3 in-Car 5観点 実装ステータス

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（CLA Q1 2026, ChatGPT 4o + Google Gemini 2 Agent）[一次] |
| a-2 ナビ・ルート | 実装済（Google AI Agent for POI/Navigation）[一次] |
| a-3 コックピット制御 | 部分実装（MBUX 既存制御 + AI連携拡大中）[推論] |
| a-4 乗員ケア | 2027以降（Liquid AI embedded 2026下期で拡張予定）[一次] |
| a-5 コマース | 2026予定（CLA で Google経由予約系拡張）[推論] |

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 「Orch自前 + FM外部三層」の Multi-Agent 構成が量産可能であると Mercedes が証明済み。Honda の ASIMO OS + Gemini は同型で、追従難度は中
- Liquid AI を embedded 化（北米向け、2026下期）する戦略は「外部依存からの段階的部分内製化」のロードマップ。Honda が Helm.ai を ADAS embedded に位置づけている構造と類似
- Wayve（Series D 出資）+ Momenta（中国向け）+ NVIDIA Drive AV の三段構え。地域別 ADAS 分散が Honda にとって参照可能

### 6.2 警鐘 or 注意点
- 3社FM 並走は Orchestration 品質次第でカオス化。Honda が単一FM（Gemini）でスタートする現状は短期的にリスク低だが、長期では Multi-Agent 化を強いられる
- R&D $6.85B 規模は Honda 単独の実行可能性に疑問符。提携で補う設計が前提

### 6.3 Honda の現在地との差分
Honda の P2-T（ASIMO OS + Gemini 単一）から Mercedes P2-E（Multi-Agent + Liquid AI embedded）への到達距離は中。MMA platform 全車展開（2027〜）の速度に追従するには Honda 0 Series 全モデルへの ASIMO OS 配備加速が必要。

---

## 7. [未特定] 残課題

- Liquid AI 多年契約のコスト規模（理由：双方とも開示せず。[未特定] 確定）
- Liquid AI LFM embedding 対象モデル名（理由：2026下期の第1配備モデルは「北米向け高度音声技術」と記述のみ、具体車種名未公開）
- Multi-Agent Orchestration の意思決定ロジック（理由：MB.OS 内部仕様非公開）
- Wayve への Series D 出資シェア（理由：三社合計 $1.5B のうち Mercedes 単独額未開示）
- LFM Fine-tuning 対象データの種類・規模（理由：社内仕様、非公開）

## 8. 2026 Q1-Q2 追加ファクト

- Liquid AI 多年契約正式発表（2026.4.23）：MB.OS 上で embedded on-device intelligence をスケール、北米第1量産配備2026下期 [一次]
- 対象モデル：第3・第4世代 MBUX 搭載車。2026 CLA EV ＋ 2027 CLA ICE 系も適用範囲 [一次]
- 北米先行（米国・カナダ）、Liquid AI ローカル推論で高速・プライバシー強化 [一次]

## 8. V4 検証記録（2026-05-01）

| 検証項目 | 結果 | 根拠 |
|----|----|----|
| Liquid AI 技術種別 | LFM（Liquid Foundation Models）確認 | 公式プレスリリース [一次] |
| オンデバイス推論 | 確認（クラウド非依存）| 公式「local inference」記述 [一次] |
| FM Level B | 確認（[推論]から[一次]に格上げ）| LFM = on-device Fine-tune 型 = Level B |
| コスト規模 | [未特定]（非公開確定）| 双方の公式情報に金額なし |
| 第1配備時期 | 2026下期 北米（advanced speech）| 公式 [一次] |

## 出典（2026 Q1追加）

- [Mercedes 公式 — Mercedes-Benz and Liquid AI Partner](https://media.mbusa.com/releases/mercedes-benz-and-liquid-ai-partner-to-scale-embedded-in-car-intelligence-in-north-america) [一次]
- [Businesswire — Mercedes-Benz Liquid AI Partner 2026.4.23](https://www.businesswire.com/news/home/20260423009970/en/Mercedes-Benz-and-Liquid-AI-Partner-to-Scale-Embedded-In-Car-Intelligence-in-North-America) [一次]
