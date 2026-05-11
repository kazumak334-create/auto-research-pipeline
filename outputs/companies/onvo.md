# Onvo（NIO傘下） — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P1-E（親NIO 流用・確立）/ Multi-Agent ◎
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **Q1 2026 納車 6,879台**（うち3月 6,877台 +131% MoM、+42.7% YoY）、L60+L90 累計 140K台超え。**L80 launch 2026.5 確定**（pure-vision + LiDAR 両仕様）、Onvo史上最大 volume 期待。NIO ES9 と並ぶ Q2 重点
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Eletric-vehicles + StockTitan

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | L90（Shenji NX9031搭載、2026.5 deliveries）+ L80（2026.4.28予約開始）[一次] |
| 量産時期 | 2026.5〜 [一次] |
| 対象国 | 中国 [一次] |
| AI Agent搭載総台数 | L90/L80 全車 [推論] |
| FM Level | C（NIO 系資産流用、Shenji NX9031 自社チップ）|
| 主要採用FM | NIO 系 NWM + NOMI Agents 流用 [推論] |
| 採用Orchestrator | NIO SkyOS 流用 [推論] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P1-E、Multi-Agent ◎（NIO 系資産流用）
- FM Level：C（親 NIO 系流用、Shenji NX9031 1,000 TOPS超 5nm）
- ファミリー EV（25-40万元）セグメント [推論]

---

## 6. Honda 示唆（So What）

Onvo は親 NIO の Shenji NX9031 自社チップを大衆価格帯（25-40万元）に展開する戦略。Honda が 0 Series 大衆価格帯にも上位機能を流用する戦略の参照。**ただし Q1 2026 L90 納車 6,179台**（過去ピーク月 10K+ から減速）、Q1 全体ではブランド初期勢いの鈍化兆候。**L80 launch 2026.5 で再加速狙い**。

## 7. 2026 Q1-Q2 追加ファクト

- Q1 2026 Onvo 全体納車 約6,800台（NIO Group 全体 83,465台の一部）[一次]
- 3月単月 6,877台（+131% MoM、+42.7% YoY）[一次]
- L90 3月 3,360台（+155% MoM）、L60 3月 3,517台（-27% YoY、減速）[一次]
- L60+L90 累計納車 140K台超（2024.9 launch 以来）[二次]
- **L80 launch 2026.5 確定**：5座版 L90、pure-vision + LiDAR 両仕様、L60/L90 boost 期待 [二次]

## 出典（2026 Q1追加）

- [Eletric-vehicles — Onvo's EV Deliveries Jump YoY in March](https://eletric-vehicles.com/nio/onvo/onvos-ev-deliveries-jump-yoy-in-march-more-than-double-sequentially/) [二次]
- [Eletric-vehicles — Nio CEO Tells Staff to 'Seize' Q2 With ES9, Onvo L80 Launches](https://eletric-vehicles.com/nio/nio-ceo-tells-staff-to-seize-q2-with-es9-onvo-l80-launches/) [二次]


## 直近アップデート
- 2026-05-11: NIO Onvo 2026 L90 SUV配達開始。 ([出典](https://cnevpost.com/2026/05/09/nio-onvo-starts-deliveries-2026-l90/))
