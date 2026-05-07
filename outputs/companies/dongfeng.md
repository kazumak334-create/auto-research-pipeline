# Dongfeng — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P3-T（DeepSeek 全ブランド・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Q1 2026 販売 528,000台 +12.3% YoY**、NEV 21万台 +52.3%、海外 96K台 +75.6%。**Voyah 香港上場（2026.3.19）= 中国国有企業初の高級NEV株**。Q1 Voyah 33,892台 +30%、3月単月 15K台。2026 通期目標 3.25M台（NEV 1.7M、輸出 600K）。**Voyah 4新型 launch 2026、全車 L3-level 知能運転 HW**
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Gasgoo + CnEVPost

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Voyah（Zhiyin等）/ eπ / Forthing / Nammi [一次] |
| 量産時期 | DeepSeek 完全統合 + Voyah Xiaoyao Cockpit [一次] |
| 対象国 | 中国（NEV 1M台達成 2025）[一次] |
| AI Agent搭載総台数 | NEV 1M 台規模 [一次] |
| FM Level | A（DeepSeek + Qwen API利用）|
| 主要採用FM | DeepSeek + Qwen（2026.4 北京）[一次] |
| 採用Orchestrator | Voyah Xiaoyao Cockpit（自前）[一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P3-T、Multi-Agent 空欄
- FM Level：A（外部API、多FM 並走）
- NEV 1M 台達成（2025）= 中国国有大手の NEV 量産達成水準

---

## 6. Honda 示唆（So What）

Dongfeng は Honda の中国合弁パートナー（東風本田）。Dongfeng の自社ブランド側で DeepSeek 全統合・Voyah Cockpit 自前という路線は、合弁外の独立路線として参照。Honda 中国合弁戦略の競合圧力を定量化する材料。**Voyah 香港上場（2026.3.19）= 中国国有企業初の高級NEV独立資金調達**。**Q1 2026 NEV +52.3%、海外 +75.6%** = Dongfeng 自社路線が東風本田を凌駕する勢い。Honda 中国合弁の処遇判断材料が増加。

## 7. 2026 Q1-Q2 追加ファクト

- **Q1 2026 グループ販売 528K台 +12.3% YoY**、NEV 21万台 +52.3%、海外 96K台 +75.6% [一次]
- Voyah Q1 納車 33,892台 +30% YoY、3月単月 15,019台（+50% YoY、+80% MoM）[一次]
- **Voyah 香港上場（2026.3.19）= 中国国有企業初の高級NEV株** [二次]
- 大型5座 SUV Taishan X8 が 2026.3.19 グローバル debut、4月末 pre-sale 開始 [二次]
- 2026 通期目標：3.25M台（NEV 1.7M、輸出 600K）[二次]
- Voyah：上場後戦略 = 価格競争回避、profit ある販売、cash flow 重視。年1-3新型 launch、2026年末までに 6-9車種展開 [二次]
- **Voyah 2026 年 4新型 launch、全車 L3-level 知能運転 HW 標準** [一次]
- DeepSeek + Qwen 採用継続、Voyah Xiaoyao Cockpit 自前 Orchestrator [一次]

## 出典（2026 Q1追加）

- [Gasgoo — Dongfeng Q1 Sales Rise 12.3%](https://autonews.gasgoo.com/articles/news/dongfeng-q1-sales-rise-123-new-energy-up-52-self-owned-brands-rise-joint-ventures-diverge-2041867583362347009) [二次]
- [CnEVPost — Voyah delivers 10,515 cars in Jan](https://cnevpost.com/2026/02/01/voyah-delivers-10515-cars-jan-plans-4-models-2026/) [二次]
- [CnEVPost — Dongfeng Voyah HK stock market debut](https://cnevpost.com/2026/03/19/dongfeng-voyah-makes-hk-stock-market-debut/) [二次]
- [China Daily — Dongfeng targets 3.25M vehicles in 2026](https://www.chinadaily.com.cn/a/202602/02/WS69803c8ea310d6866eb36f1f.html) [二次]
