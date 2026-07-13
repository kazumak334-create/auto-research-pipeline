# Tesla — IVI Agentic AI 実装ファクトブック

**Tier：** T1
**分類：** P1-E（完全垂直統合・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026決算で AI5 を Optimus・データセンター用に再定義、Cybercab は AI4 で量産開始。Robotaxi Dallas/Houston 展開、Capex $25B 維持
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Tesla Q1 2026 決算（2026.4.22）

---

## 1. エグゼクティブサマリ

Tesla は xAI Grok を「外部FM」として接続するが、Elon Musk が両社CEO を兼務し実質的に内部資産化している。FSD・チップ（AI4/AI5）・Dojo・自社Fab（Terafab Austin）まで全層を内製する完全垂直型 P1-E。2026年 Capex は前年 $8.5B の3倍に当たる $25B。Cybercab 量産・Optimus 量産・AI5 小ロット投入が同年に集中し、自動車産業からAI ロボティクス企業への転身を公式宣言した。Honda の参照対象としては「内製の極端事例」であり、再現可能性は低い。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Model S/X/Y/3/Cybertruck（AMD搭載車に Grok 統合）[一次] |
| 量産時期 | Grok 2025.7〜 / "Hey Grok" ハンズフリー 2026春 [一次] |
| 対象国 | グローバル（AMD搭載車のみ）[一次] |
| 旗艦年産 | Model Y 全市場合計1.4M超（2024）[推論] |
| AI Agent搭載総台数 | 2027までに数百万台規模（AMD搭載車 OTA, 約4M+）[推論] |
| FM Level | C（Full Stack型、ただし Grok 部分は外部混合） |
| 主要採用FM | xAI Grok 3/4（OTAでバージョン進化）[一次] |
| 採用Orchestrator | Tesla 内製（FSD ラインから派生）[推論] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：全EV（高級〜中価格）。Cybertruck（高価格帯）+ Model 3/Y（量販）の二層構成 [一次]
- 旗艦モデルの市場定位：Model Y は世界最量販EV、Cybertruck は2026後半量産 [一次]
- 量産時期と地域戦略：Grok は AMD搭載車のみグローバル展開、HW3 認定機能不足を Musk 自ら 2026.4.23 認定 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | エンタメ会話 + ナビ強化 + コックピット部分制御（FSD は別系統）[一次] |
| 体験の深さ | Tool Use（位置リマインダー、複合検索）[一次]、自律タスク実行は開発中 |
| 個別最適化度 | 履歴学習（Tesla アカウント連結）[推論] |

UXシナリオ要約：
"Hey Grok, 帰り道で評価高いコーヒーショップでスーパーチャージャー併設の店を" という指示で、ナビ + 充電計画を統合的に提案する [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P1-E × Multi-Agent ◎
- 分類根拠：Orchestrator・チップ・OS は完全自前。FM のみ xAI Grok を採用するが、Musk が両社CEO で実質統合運営 [一次/推論]

### 3.2 Foundation Model レベル分析
- FM Level：C（Full Stack型に近い。Grok を「外部資産」と見なすか「実質内部」と見なすかで A〜C 間を揺れる）
- 6要素配分：
  - アーキテクチャ：自前（FSD ニューラルネット派生）+ Grok（xAI 設計）
  - ウェイト：Full学習（自社FSD、約 1B+ miles のフリートデータで継続学習）
  - 事前学習データ：自社収集（FSD カメラフリート1B+ miles）[一次]
  - Fine-tuningデータ：自社（HW4 全車から OTA 収集）[一次]
  - 学習インフラ：Cortex（自社、2026 容量倍増）+ Dojo + 計画中の Dojo 3 [一次]
  - 推論ランタイム：完全自前（AI4 量産、AI5 2026末小ロット → 2027本格）[一次]

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | xAI Grok 3/4（OTAでバージョン進化）[一次] |
| 採用Orchestrator | Tesla 内製（FSD ラインから派生）[推論] |
| 採用ミドルウェア（IVI OS） | Tesla OS（Linux派生・自前）[一次] |
| 採用チップ（SoC） | AI4（HW4 量産中）/ AI5（HW5、2026末小ロット, 2027本格）[一次] |
| R&D投資規模（AI関連年額） | 2026 Capex $25B（うち AI compute 中核、Cortex 倍増、Terafab 構築）[一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | xAI（Elon直系、$2B出資）[一次] |
| Orchestrator提供 | 自社 [推論] |
| Chip提供 | 自社（AI4/AI5/Dojo/Terafab自製）[一次] |
| データ・地図提供 | 自社（FSDフリート1B+ miles）[一次]、Google Maps 連携 [推論] |
| ADAS提供 | 自社（FSD HW4稼働、Robotaxi Austin 2025.6開始/12月無人化）[一次] |
| 親グループ（P4のみ）| 該当なし（独立）[一次] |

---

## 5. 将来：どこへ向かうか

### 5.1 内製意志（戦略宣言ファクト）
- 公式宣言：Q1 2026 決算（2026.4.22-23）「Tesla はAI ロボティクス企業に転換」[一次]
- 投資規模：2026 Capex $25B超、AI infrastructure と6新工場、年内Free Cash Flow マイナス見通し [一次]
- **戦略変更（2026 Q1）：** AI5 を Optimus・データセンター用途に再定義し、Cybercab は AI4 で量産開始。AI4 で人類超えの Unsupervised FSD 達成可能と Musk 言明。AI5 の車両搭載は2027以降（必要時のみ）[一次]
- 移行ロードマップ：Cybercab 量産開始済（Q1 2026）→ Model Y 代替の最大量産モデル化を計画 / Optimus 第1世代量産ライン Q2 着工、Fremont Model S/X ライン置換、年産100万台規模 / 第3世代Optimus 2026年7-8月量産開始 [一次]
- Robotaxi Unsupervised：Dallas / Houston 展開（2026.4）、年末までに10数州目標。事故・負傷ゼロ実績 [一次]
- SpaceX 提携：史上最大級チップFab（Terafab）構築、ロジック・メモリ・先進パッケージング垂直統合 [一次]
- 動機：差別化 + データ主権（自社FSD フリート 1B+ miles）+ コスト（自社チップ Fab）

### 5.2 2027/2030 戦略パターン遷移予測
- 現在：P1-E（垂直完全 + xAI Grok 外部混合）
- 2027：P1-E（AI5 量産 + Cybercab + Optimus 同基盤）（確度：高）
- 2030：P1-E（Tesla AI 全社統合、Grok = 内部資産化）（確度：高）
- 分岐条件：xAI が Tesla に統合（Musk 単独支配化）or 完全独立し Grok 撤退

### 5.3 in-Car 5観点 実装ステータス

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（Grok "Hey Grok"、AMD搭載車）[一次] |
| a-2 ナビ・ルート | 実装済（Supercharger統合複合検索）[一次] |
| a-3 コックピット制御 | 部分実装（FSD は別系統、Grok→FSD 制御は開発中）[一次] |
| a-4 乗員ケア | 無（[未特定]、camera-based DMS あり）[推論] |
| a-5 コマース | 無（Tesla App 内決済のみ）[推論] |

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 「FM外部 + Orch自前」混合戦略でも、CEO レベルで両社を握れば実質垂直統合に近づく。Honda が外部FM（Gemini）+ 自前 ASIMO OS で進める場合、提携深度の確認軸として参照可能
- データフリート規模（1B+ miles）が FM のFine-tune 余地を支配する。Honda は車両走行データ収集規律の早期確立が必須

### 6.2 警鐘 or 注意点
- Capex $25B 規模の追従は不可能。Tesla を「目標」ではなく「外れ値」として位置づけるべき
- Grok 統合直後の認知負荷・安全性問題（NYC テスト 2026.4 CNBC 報道）[一次]。FM 接続だけで UX 品質が担保されない事例

### 6.3 Honda の現在地との差分
Honda の P2-T（ASIMO OS + Gemini）から Tesla P1-E への到達距離は超大（Fab・Dojo・FSD フリートすべて未保有）。再現対象外。

---

## 7. [未特定] 残課題

- Tesla Grok の Tool Use カバー範囲（FSD制御接続時期）（理由：Musk「FSD制御は開発中」発言のみ、量産時期非開示）
- AI5 量産後の Grok 性能向上幅（理由：xAI 側のロードマップ非開示）
- Robotaxi 商用展開（Austin/Dallas/Houston 以外）の収益モデル（理由：[未特定]）
- Cybercab AI4 量産で Robotaxi Unsupervised FSD が真に人類超え水準に達するか（理由：実績データ蓄積中）

## 出典（2026 Q1追加）

- [Tesla Q1 2026 Update PDF](https://assets-ir.tesla.com/tesla-contents/IR/TSLA-Q1-2026-Update.pdf) [一次]
- [Notateslaapp — Tesla Delays Next-Gen AI5 to Mid-2027](https://www.notateslaapp.com/news/3337/tesla-delays-next-gen-ai5-to-mid-2027-cybercab-will-launch-on-ai4-hardware) [二次]
- [BigGo Finance — Tesla Q1 2026 Earnings Call](https://finance.biggo.com/news/US_TSLA_2026-04-22) [二次]


## 直近アップデート
- 2026-05-11: Tesla FSD 中国での2026年初完全承認をMusk示唆（2025年末時点記事）。 ([出典](https://cnevpost.com/2025/11/07/china-to-fully-approve-tesla-fsd-early-2026/))

### 2026-05-13
- 事実：Tesla Optimus V3 公開を今年中に延期。FremontでOptimus Q2生産開始（年産100万台ライン）、Texas Gigaでも10M台目標の第2世代ライン整備中
- 出典：https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/
- 発表日：2026-04-23
- 確度：中（industry_media）
- 2026-07-14: Tesla-SpaceX合併観測——FSDとOptimusの評価を「テーブルに残す」リスクとしてアナリスト指摘。[StockTwits 2026-07] ([出典](https://stocktwits.com/news-articles/markets/equity/tesla-spacex-merger-rumors-fsd-optimus-valuation-gordon-johnson-jefferies/cZKwbLRR7aP))
