# Renault — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** P3-T（Google Cloud・移行中）
**最終更新：** 2026-04-28
**最終確認：** 2026-04-28 ／ Q1 2026 売上 €12.5B +7.3% YoY、欧州 BEV 販売 +21%、電動化比率 17%（+4pt YoY）。Trafic E-Tech が Google AAOS SDV 第1号 launch、機能 90% を FOTA 更新可能。2026 op margin guidance 5.5%維持
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Renault Group 公式（2026.4）

---

## 1. エグゼクティブサマリ

Renault は現行 R5/R4 で Cerence Chat Pro（2024.9 量産）、2026下期 OTA で Google Gemini に切替予定。Ampere（EV ブランド）が Google Cloud AAOS SDV ベースで開発。Renault Software République + AAOS の Orchestrator、Gemini Code Assist + デジタルツインで SDV 加速。Honda P2-T と同じ Gemini 採用先行例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | R5 / R4（Reno 搭載済）[一次] |
| 量産時期 | Cerence Chat Pro 2024.9〜 / Gemini 2026下期 [一次] |
| 対象国 | 欧州 [一次] |
| AI Agent搭載総台数 | [未特定] |
| FM Level | A（Gemini API利用）|
| 主要採用FM | Cerence Chat Pro（現行）+ Google Gemini（OTA, 2026下期）[一次] |
| 採用Orchestrator | Google AAOS（外部）+ Cerence 補完 [一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆 EV（R5/R4）[一次]
- 旗艦モデルの市場定位：R5 が Reno 搭載済、Gemini OTA で機能拡張
- 量産時期と地域戦略：欧州中心、中国向け高度自動運転依存先 [未特定]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | エンタメ会話（Reno）→ Gemini 統合執事 [一次] |
| 体験の深さ | 表層対話 → Tool Use（Gemini OTA 後）|
| 個別最適化度 | 自然言語で空調・シート制御、習慣学習 [一次] |

UXシナリオ要約：
"Reno, find nearest charger" 程度から、2026下期で Gemini で複雑タスク化 [推論]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：P3-T、Multi-Agent 空欄（Gemini 単一）[一次]
- 分類根拠：AAOS（Google外部）+ Cerence 補完 + Gemini Code Assist 開発支援 [一次]

### 3.2 Foundation Model レベル分析
- FM Level：A（API利用、Gemini）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Cerence Chat Pro（現行）+ Google Gemini（OTA, 2026下期）[一次] |
| 採用Orchestrator | Google AAOS（外部）+ Cerence 補完 [一次] |
| 採用ミドルウェア（IVI OS）| Renault Software République + AAOS [一次] |
| 採用チップ（SoC）| Qualcomm [一次] |
| R&D投資規模（AI関連年額）| Google Gemini Code Assist + デジタルツインで SDV 加速 [一次] |

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | Google + Cerence |
| Orchestrator提供 | Google AAOS + Cerence |
| Chip提供 | Qualcomm |
| データ・地図提供 | Google Maps |
| ADAS提供 | 自前（Lvl 2）+ 中国向け [未特定] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 実装済（Reno 2024.9 R5）|
| a-2 ナビ・ルート | 実装済（Google Maps）|
| a-3 コックピット制御 | 部分実装 |
| a-4 乗員ケア | 無 |
| a-5 コマース | [未特定] |

- 2027予測：P3-E（Gemini 全車展開）
- 2030予測：P3-E 継続

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- Gemini 採用 OEM 群（GM, Honda, Renault, Ford）の中で Renault は Cerence Chat Pro → Gemini 切替の段階移行例。Honda が Gemini 採用後の「次の手」を Renault のロードマップから推察可能
- Software République + AAOS の組合せは Honda の ASIMO OS + Gemini と異なる「外部Orch 採用」型

### 6.2 警鐘 or 注意点
- Cerence Chat Pro → Gemini への切替コストは限定的（OEM 共通基盤）。Honda の Gemini 採用も同様の入替容易性を活用すべき

### 6.3 Honda の現在地との差分
Honda P2-T（ASIMO OS 自前 + Gemini 外部）と Renault P3-T（AAOS 外部 + Gemini 外部）の差は Orch の自前度。Honda が ASIMO OS で差別化を維持できるかが分岐点。

---

## 7. [未特定] 残課題

- Renault Gemini OTA 2026下期 量産モデル名（理由：全モデル一斉か特定モデル先行か未公開）
- 中国向け自動運転外部依存先（理由：[未特定]）
- Reno の Tool Use カバー範囲（理由：[未特定]）
