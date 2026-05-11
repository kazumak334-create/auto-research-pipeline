# Geely — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-E（DeepSeek + Cerence + StepFun・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Zeekr 完全買収完了（2025.12.22 NYSE 上場廃止）**：Geely グループ内資産統合・重複投資抑制・コスト削減。海外50ヶ国進出・欧州生産拠点設立。DeepSeek + Xingrui 自社統合継続、2,000+ 車両インターフェース対応
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CnEVPost + PRNewswire

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Galaxy M9（Cerence xUI 2026.4）[一次] |
| 量産時期 | DeepSeek 2025.2 / Cerence xUI 2026.4 [一次] |
| 対象国 | 中国 + 海外（Galaxy）[一次] |
| AI Agent搭載総台数 | Galaxy / Geely / Lynk 全車 [推論] |
| FM Level | A+B（外部FM 多重 + Xingrui 自社）|
| 主要採用FM | DeepSeek + Xingrui（自社）+ Cerence CaLLM [一次] |
| 採用Orchestrator | WAM+1+2+N multi-agent framework + Cerence xUI [一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-E、Multi-Agent ◎（DeepSeek + Xingrui + Cerence 三層）
- FM Level：A+B（外部API + 自社一部）
- WAM（World Action Model）が Zeekr 8X で量産展開（2026年）[一次]
- Cerence xUI Galaxy M9 で 2026.4 量産（Cerence 公式 2社目顧客）[一次]

---

## 6. Honda 示唆（So What）

Geely の「DeepSeek + Xingrui 自社 + Cerence xUI」三層 Multi-Agent は、Honda の Gemini 単一から Multi-Agent 移行する際の中国実装パターン参照モデル。Cerence xUI は西側汎用 IVI Agent OS 化の象徴で、Honda が ASIMO OS で対抗する戦略の妥当性を浮き彫りにする。**Zeekr 完全子会社化（2025.12）= Geely グループのプレミアム戦略統合**。Honda が Acura ブランド（RSX 中止後）の処遇を考える上での参照モデル。

## 7. 2026 Q1-Q2 追加ファクト

- **Zeekr 完全買収完了（2025.12.22 NYSE 上場廃止）**：Keystone Mergersub Limited（Geely 完全子会社）と合併、Zeekr ADR 1株 = US$2.687 現金 or Geely 株1.23 株 [一次]
- 戦略目的：高級EV 領域でのリソース統合、cannibalization 抑制、シナジー強化、long-term value 構築 [二次]
- 海外戦略：Zeekr の海外チャネル + ローカル製造能力を統合し 50ヶ国進出、欧州にローカル生産拠点 [二次]
- DeepSeek R1 統合継続：Xingrui 車載 FunctionCall AI と distillation training、約 2,000 車両インターフェース対応 [二次]

## 出典（2026 Q1追加）

- [CnEVPost — Zeekr completes merger with Geely, delists from NYSE](https://cnevpost.com/2025/12/22/zeekr-completes-merger-with-geely-delists-from-nyse/) [一次]
- [PRNewswire — Zeekr Group Announces Completion of Merger](https://www.prnewswire.com/news-releases/zeekr-group-announces-completion-of-merger-302647823.html) [一次]


## 直近アップデート
- 2026-05-11: 4月販売23.5万台。Zeekr好調。 ([出典](https://autonews.gasgoo.com/articles/ev/geely-auto-april-sales-reach-235000-units-2052294977630134272))
