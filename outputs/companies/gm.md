# GM — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P2→P3 hybrid（Gemini 2026 OTA・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026 業績Wall Street超過、2026 通期ガイダンス引上 ($13.5-15.5B)。**次世代EVトラックプログラム停止**（Factory Zero, Detroit）、HEV/ICE 回帰。Cruise を GM 本体に統合し AD/ADAS 共同開発。OnStar/Super Cruise が高利益貢献
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ GM Q1 2026 公式（2026.4.28）+ CNBC

---

## 1. エグゼクティブサマリ

GM は「GM Forward」イベント（2025.10.22）で Google Gemini AI Assistant を 2026 OTA で全車種展開する方針を発表。同時に「将来は自社カスタムAI を開発」と公式言明し、Gemini 一社依存から離脱する予兆あり。Eyes-off 自動運転は Cadillac ESCALADE IQ で2028年。Cruise 撤退（2024.12）の知見を ADAS に転用。短期は外部活用 + 中長期は自前カスタム AI への移行ロードマップを示す。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Cadillac ESCALADE IQ（Eyes-off 2028）/ 全車 Gemini 2026 OTA [一次] |
| 量産時期 | Gemini OTA 2026 [一次] |
| 対象国 | 北米中心 [一次] |
| AI Agent搭載総台数 | MY2015以降 OnStar 経由全車（数千万台規模）[推論] |
| FM Level | A（Google Gemini API利用、将来カスタムAI 計画）|
| 主要採用FM | Google Gemini [一次] |
| 採用Orchestrator | Google + 自社（カスタムAI 計画あり）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆〜高級（GMC/Cadillac 全車）[一次]
- 旗艦モデルの市場定位：Cadillac ESCALADE IQ で Eyes-off 自動運転 2028。全車 Gemini OTA
- 量産時期と地域戦略：北米中心、MY2015以降の OnStar 連結車に OTA で展開

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | 統合執事 [一次] |
| 体験の深さ | Tool Use（複合質問対応）[一次] |
| 個別最適化度 | パーソナライゼーション学習 [一次] |

UXシナリオ要約：
Gemini 統合で複合質問対応、Eyes-off 自動運転連携（2028）。Multi-stop route planning、習慣学習機能を訴求 [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P2→P3 hybrid、Multi-Agent 空欄（Gemini 単一）[一次]
- 分類根拠：Gemini 単一依存（P3寄り）+ 自社カスタムAI 計画（P2寄り）の中間移行 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用型、Gemini）→ 将来 B 移行計画あり

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Google Gemini [一次] |
| 採用Orchestrator | Google + 自社（カスタムAI 計画あり）[一次] |
| 採用ミドルウェア（IVI OS）| Ultifi（既存）→ 新統合プラットフォーム移行 [推論] |
| 採用チップ（SoC）| NVIDIA / Qualcomm（[未特定]）|
| R&D投資規模（AI関連年額）| Cruise 撤退（2024.12）の知見転用 [一次]、Cruise 内製化継続 [一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Google Cloud |
| Orchestrator提供 | Google + 自社 |
| Chip提供 | NVIDIA / Qualcomm SA8650P 等 [推論] |
| データ・地図提供 | Google Maps |
| ADAS提供 | Super Cruise（自前、Lvl 2+）+ Cruise 知見転用 [一次] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 2026予定（Gemini OTA）|
| a-2 ナビ・ルート | 実装済（Google Maps）|
| a-3 コックピット制御 | 部分実装（Ultifi）|
| a-4 乗員ケア | 無 |
| a-5 コマース | 2026予定（Google経由）|

- 2027予測：P2-T 移行（自社カスタムAI 開発加速）
- 2030予測：P2-E（自社カスタムAI 量産投入）
- 分岐条件：自社カスタムAI 完成度 / Google との関係維持

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 「Gemini 全車 OTA」と「将来カスタムAI」の二段構えは Honda 0 Series + ASIMO OS と同型構造。GM の 2027以降のカスタムAI 移行進度が Honda の指標になる
- OnStar による既存車（MY2015以降）への OTA 展開は数千万台規模。Honda の既存車 OTA 展開戦略の参照モデル
- Eyes-off 2028 の段階的ロードマップは Honda の L3 戦略にとって参照可能

### 6.2 警鐘 or 注意点
- Gemini 単一依存からの「将来離脱」を公式言明済み。Google 側の譲歩条件次第で Honda の Gemini 採用条件にも影響
- Cruise 撤退で Robotaxi 自社路線を断念。自前完全自動運転の難度を示す事例

### 6.3 Honda の現在地との差分
Honda P2-T と GM P2→P3 hybrid は近似。GM は Cruise 撤退で「自前ADAS 拡大」へ路線変更、Honda は Helm.ai 採用で「外部依存 + 部分内製」を維持。GM の自社カスタムAI 開発進度が Honda 同様の動きを正当化する根拠になる。

---

## 7. [未特定] 残課題

- GM Gemini 「将来カスタムAI」のロードマップ（理由：公式言明はあるが時期・範囲未公開）
- 自社カスタムAI の FM 規模・調達戦略（理由：[未特定]）
- Eyes-off 2028 後の Lvl 3 / Lvl 4 ロードマップ（理由：[未特定]）

## 8. 2026 Q1-Q2 追加ファクト

- **次世代EVトラックプログラム停止**（Factory Zero, Detroit）、HEV/ICE への投資re-allocation [二次]
- 2026 通期 Adjusted Earnings ガイダンス $13.5-15.5B（前回予想から +$500M / +50¢ EPS）[一次]
- 米最高裁の関税終結・還付決定で約 $500M ベネフィット [一次]
- 2026 通期 関税コスト粗 $3-4B 見通し（Q1 単期 $750M-1B）[一次]
- Q4 2025 EV gross margin が初めて variable-profit-positive 転換 [一次]
- Cruise 撤退の知見を GM AV/ADAS に統合 — Cruise Origin 無期限延期、AV ボランタリー停止継続 [一次]
- OnStar / Super Cruise が高利益サービス収益として貢献 [一次]

## 出典（2026 Q1追加）

- [CNBC — GM Q1 2026 earnings](https://www.cnbc.com/2026/04/28/general-motors-gm-earnings-q1-2026.html) [二次]
- [GM IR — Q1 2026 Earnings Deck](https://investor.gm.com/static-files/fa689555-e0aa-4c5c-be5c-fba9c1d9049f) [一次]
- [GM IR — Q1 2026 Letter to Shareholders](https://investor.gm.com/news-releases/news-release-details/q1-2026-letter-shareholders) [一次]
