# Changan — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-T→P1-T 移行（DeepSeek + Avatr Huawei・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Avatr + Deepal 統合（2026.4.21 Zhu Huarong 発表）**：mid-back-end 統合（R&D/SC/製造）でコスト 20-30% 削減、front-end ブランド独立維持。**Q1 2026 Avatr 11,703台 -41.6% YoY**（深刻減速）、Deepal 53,601台 +5.2%。2030 目標：Avatr 500K / Deepal 1M / Changan 2.6M / NEV 計 2.4M。今年以降 non-intelligent product 開発停止、3年で35新型 launch
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Carnewschina + Caixin Global

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Avatr（Huawei HIMA加盟）+ Qiyuan E07（DeepSeek搭載）[一次] |
| 量産時期 | NEV 789K台（+26.8%, 2025）、L3国家初認証取得（2025.12）[一次] |
| 対象国 | 中国 [一次] |
| AI Agent搭載総台数 | NEV 789K 台規模 [一次] |
| FM Level | A（DeepSeek + Huawei 経由）|
| 主要採用FM | DeepSeek（Qiyuan）+ Huawei FM（Avatr = HIMA）[一次] |
| 採用Orchestrator | Avatr = Huawei HMAF / Qiyuan = 自前 [一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-T→P1-T 移行（Avatr 経由で内製 ADAS 取り込み中）、Multi-Agent 空欄
- FM Level：A（外部API、ブランド別二極構造）
- L3 国家初認証取得（2025.12 Changan Deepal SL03）= 中国 L3 認証パイオニア [一次]

---

## 6. Honda 示唆（So What）

Changan は中国で L3 国家初認証取得（Deepal SL03）= 中国規制環境での先行事例。Honda の L3 戦略（北米・日本）を中国規制ペースと比較する基準点。Avatr の Huawei 依存と Qiyuan の自前路線の二段構えは、Honda がブランド別に戦略を分ける可能性を示唆。**Avatr Q1 2026 -41.6% YoY = Huawei HIMA 加盟ブランドでも市場で苦戦する事例**。**ブランド統合（Avatr + Deepal）でコスト20-30%削減狙い** = Honda 0 Series + Acura 戦略再構築の参照。

## 7. 2026 Q1-Q2 追加ファクト

- **Avatr + Deepal 統合発表（2026.4.21）：** Chairman Zhu Huarong が公表。mid-back-end（R&D / supply chain / 製造）統合で2026 年末までに完了 [二次]
- 「independent front-end, collaborative mid-to-back-end」モデル = ブランド identity / product / sales channel は分離維持、backend インフラ共有でリソースコスト 20-30% 削減 [二次]
- Q1 2026 販売：Avatr 11,703台（-41.6% YoY、深刻減速）、Deepal 53,601台（+5.2%）[二次]
- 2030 目標：Avatr 500K台 / Deepal 1M台 / Changan ブランド 2.6M台 / NEV 計 2.4M台 [二次]
- 「今年以降 non-intelligent 製品の新規開発を停止」、3年で 35 新型 smart vehicle launch [二次]
- Qiankun Intelligent Driving + HarmonyOS を Avatr / Deepal 製品で全面活用 [二次]
- マレーシア進出 Q3 2026（Nevo / Deepal / Avatr 三ブランド同時）[二次]

## 出典（2026 Q1追加）

- [Carnewschina — Changan to fuse Avatr and Deepal operations](https://carnewschina.com/2026/04/21/changan-to-fuse-avatr-and-deepal-operations-as-avatr-q1-sales-plunge-41-6/) [二次]
- [Caixin Global — Changan to Integrate EV Brands' Back-End Operations](https://www.caixinglobal.com/2026-04-24/changan-to-integrate-ev-brands-back-end-operations-to-cut-costs-102437277.html) [二次]
- [Paultan — Changan Auto coming to Malaysia by Q3 2026](https://paultan.org/2026/04/21/changan-auto-coming-to-malaysia-with-nevo-deepal-avatr-chinese-top-four-player-arriving-by-q3-2026/) [二次]
