# Zeekr — IVI Agentic AI 実装ファクトブック

**Tier：** T3
**分類：** P1-E（NVIDIA Thor + WAM 自前・確立）/ Multi-Agent ◎ → **Geely 完全子会社化で再評価**
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ **2025.12.22 Geely と合併完了、NYSE 上場廃止、Geely 100% 子会社化**。独立EV ブランド戦略 → Geely グループ内ハイエンド EV 統合へ。技術資産（Eva Super Agent / WAM / NVIDIA Thor 採用）は Geely グループ内で継続活用
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ CnEVPost + PRNewswire

---

## 1. エグゼクティブサマリ

| 項目 | 値 |
|-----|---|
| 旗艦モデル | Zeekr 8X（Eva 統合 2025末）/ RT（Waymo向け）[一次] |
| 量産時期 | DRIVE Thor ADCU MAX 2025初（世界初OEM）[一次] |
| 対象国 | 中国 + 海外 [一次] |
| AI Agent搭載総台数 | Zeekr 全車 + Waymo 提供分 [推論] |
| FM Level | B+C（Eva Super Agent 自社 + WAM）|
| 主要採用FM | Eva Super Agent（自社、Geely WAM 流用）[一次] |
| 採用Orchestrator | Eva Super Agent + WAM 自前 [一次] |

---

## 3. アーキテクチャ：どう作るか

- パターン分類：P1-E、Multi-Agent ◎（Eva Super Agent + WAM）
- FM Level：B+C（Eva は Geely グループ WAM を流用）
- 採用チップ：NVIDIA DRIVE Thor ADCU MAX（2025初、世界初OEM）[一次]

---

## 6. Honda 示唆（So What）

Zeekr は NVIDIA DRIVE Thor を世界初 OEM 採用。Honda が Helm.ai/NVIDIA でチップロードマップを構築する際の参照。Waymo 向け RT 供給は「中国OEM が西側 Robotaxi に車両を供給」する象徴的取引。**2025.12.22 Geely 完全子会社化** = 中国EV 業界における「独立 → グループ統合」局面の象徴。Honda の Acura ブランド処遇を考える上での参照（RSX 中止後の独立性議論）。

## 7. 2026 Q1-Q2 追加ファクト

- **2025.12.22 Geely 完全合併完了、NYSE 上場廃止**（Keystone Mergersub Limited と合併）[一次]
- 各 Zeekr 普通株を US$2.687 現金 or Geely 普通株 1.23 株と交換 [一次]
- Geely Holding が中国EV ブランド全体の重複投資抑制・リソース統合のため再編 [二次]

## 出典（2026 Q1追加）

- [CnEVPost — Zeekr completes merger with Geely, delists from NYSE](https://cnevpost.com/2025/12/22/zeekr-completes-merger-with-geely-delists-from-nyse/) [一次]
