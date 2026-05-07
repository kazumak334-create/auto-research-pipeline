# Chery — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-T（DeepSeek + Horizon・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Q1 2026 販売 601,712台、輸出 393,311台（+53.9% YoY）**、3月単月 輸出約15万台で中国ブランド月次過去最高。**香港IPO 完了（2025.9.25 上場、HK$9.14B/$1.17B 調達）**= 香港今年最大の自動車IPO。「scale拡張」→「quality深耕」へ戦略シフト
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Gasgoo + Yahoo Finance

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Luxeed（Huawei HIMA 加盟）/ Tiggo 系 [一次] |
| 量産時期 | DeepSeek + Horizon Journey 6 採用 [一次] |
| 対象国 | 中国 + 輸出首位（1.34M台）[一次] |
| AI Agent搭載総台数 | 全社 1.34M 台規模 [一次] |
| FM Level | A（DeepSeek API利用 + Huawei FM 経由）|
| 主要採用FM | DeepSeek + Huawei（Luxeed = HIMA 加盟）[一次] |
| 採用Orchestrator | Huawei HMAF（Luxeed）+ Chery 自前（Tiggo）[推論] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-T（多重外部依存）、Multi-Agent 空欄
- FM Level：A（外部API、Luxeed は Huawei 経由）
- 採用チップ：Horizon Journey 6（中国製 ADAS チップ）[一次]
- 中国輸出首位（1.34M 台）= 中国OEM の海外進出最大手

---

## 6. Honda 示唆（So What）

Chery は中国輸出首位 1.34M 台で、中国OEM の海外展開リーダー。Honda が中国 OEM の海外侵食ペースを定量化する基準点。Luxeed が Huawei HIMA 加盟、Tiggo 系は自社路線の二段構え。**香港IPO 完了（2025.9）+ Q1 2026 輸出 +53.9% YoY** = 中国OEM 海外展開資金調達と実績が同時加速。Honda グローバル戦略への直接圧力。

## 7. 2026 Q1-Q2 追加ファクト

- **Q1 2026 グループ販売 601,712台**、輸出 393,311台（+53.9% YoY）[一次]
- 3月単月 輸出 約15万台 = 中国ブランド月次過去最高 [一次]
- **香港IPO 完了（2025.9.25 上場、HK$9.14B = $1.17B 調達）**= 香港今年最大の自動車IPO [二次]
- 戦略シフト：「scale拡張」→「quality深耕」へ [一次]
- IPO 調達金は (1) R&D（NEV / intelligent tech / 製品 premium 化）+ (2) 海外展開加速 [一次]
- DeepSeek との直接統合は確認できず（業界全般の DeepSeek 採用ペースは継続）[未特定]

## 出典（2026 Q1追加）

- [Gasgoo — Chery Group March 2026 sales](https://autonews.gasgoo.com/articles/market-industry/chery-group-scores-121-yoy-growth-in-march-2026-sales-2039587112943267841) [二次]
- [Yahoo Finance — Chery planning Hong Kong IPO](https://finance.yahoo.com/news/chery-planning-hong-kong-ipo-101943887.html) [二次]
- [Chery International — Global Expansion Accelerates](https://www.cheryinternational.com/pc/news/news1/20260420/detail-2576.shtml) [一次]
