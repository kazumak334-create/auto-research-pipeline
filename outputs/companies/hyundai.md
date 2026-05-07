# Hyundai — IVI Agentic AI 実装ファクトブック

**Tier：** T2
**分類：** 段階2 ハイブリッド型・量産済（Pleos Connect Orch自前 + Gleo AI FM Level B）
**最終更新：** 2026-05-01（V3検証完了）
**最終確認：** 2026-05-01 ／ Pleos Connect 2026-04-30 正式ローンチ確認。第1搭載車種 = GRANDEUR（韓国、2026-05 納車開始）。欧州 i30・Tucson は後続モデル。Gleo AI = 42dot 開発 + SKT Sovereign AI コンソーシアム基盤 FM = Level B 確認。2030 2,000万台目標継続。
**ソース：** 04a_market-raw_v2.md（依頼書 v3 準拠）+ Hyundai 公式 + Paultan + V3 web検証（2026-05-01）

---

## 1. エグゼクティブサマリ

Hyundai は Pleos Connect（AAOS基盤、自前 Orch）+ Gleo AI（42dot開発、SKT Sovereign AI コンソーシアム FM 基盤、Level B 確認）+ Pleos ID（クロス車両パーソナライゼーション）の三層を自前で構築する段階2ハイブリッド型。2026-04-30 Pleos Connect 正式ローンチ、第1搭載車種は韓国 GRANDEUR（2026-05 納車）。2030 までに 2,000万台（Hyundai/Kia/Genesis）搭載目標を公式宣言。西側段階2 量産済の数少ない実例。

| 項目 | 値 |
|-----|---|
| 旗艦モデル | GRANDEUR（韓国、Pleos Connect 第1搭載、2026-05）[一次] |
| 量産時期 | Pleos Connect 2026-04-30 正式ローンチ [一次] |
| 対象国 | グローバル（2030 2,000万台 Hyundai/Kia/Genesis 搭載目標）[一次] |
| AI Agent搭載総台数 | 2030 までに 2,000万台（グループ合算）[一次] |
| FM Level | **B 確認**（Gleo AI = 42dot 開発 + SKT Sovereign AI コンソーシアム FM 基盤）[一次] |
| 主要採用FM | Gleo AI（42dot 開発、SKT Sovereign AI consortium FM 基盤で Fine-tune）[一次] |
| 採用Orchestrator | Pleos Connect（自前）[一次] |

---

## 2. 戦略：何をどこで誰に売るか

### 2.1 戦略ポジショニング
- 対象セグメント：大衆 EV [一次]
- 旗艦モデルの市場定位：Pleos 25 開発者会議発表（2025.3）でブランド戦略確定
- 量産時期と地域戦略：2026 Q2 から Gleo AI ロールアウト、2030 までに 2,000万台搭載 [一次]

### 2.2 目指すユーザー体験（UX）

| 軸 | 値 |
|----|---|
| 体験タイプ | エンタメ会話 + ナビ [推論] |
| 体験の深さ | Tool Use（agentic vehicle control 公式表現）|
| 個別最適化度 | Pleos ID（クロス車両パーソナライゼーション）[一次] |

UXシナリオ要約：
Gleo AI 音声 Agentic AI が Pleos Connect 統合で空調・シート制御、習慣学習を実装する [一次]。

---

## 3. アーキテクチャ：どう作るか

### 3.1 パターン分類
- 分類タグ：段階2 ハイブリッド型・量産済（Orch自前 + FM Level B）
- 分類根拠：Pleos Connect（自前 Orch、C1/C2/C3 充足）+ Gleo AI（42dot × SKT、Level B 確認）。2026-04-30 正式ローンチで「量産済」確定 [一次]。チップは Qualcomm 外部依存

### 3.2 Foundation Model レベル分析
- FM Level：**B 確認**（Gleo AI = 42dot 開発 + SKT Sovereign AI コンソーシアム基盤 FM で Fine-tune）[一次]
- 根拠：42dot は Hyundai グループのソフトウェア子会社。SKT（SK Telecom）Sovereign AI Consortium が提供する FM 基盤を採用し、車載用途に Fine-tune。「proprietary LLM technology」と公式表現 [一次]
- FM 6要素配分：アーキテクチャ（SKT 基盤）/ ウェイト（SKT 基盤 + 42dot Fine-tune）/ 学習データ（42dot 自社）/ Fine-tuningデータ（Hyundai 車両データ）/ 学習インフラ（SKT クラウド）/ 推論ランタイム（42dot 自社）

### 3.3 技術スタック

| 要素 | 採用 |
|----|-----|
| 採用FM | Gleo AI（42dot 開発、SKT Sovereign AI コンソーシアム FM 基盤 + Fine-tune = Level B）[一次] |
| 採用Orchestrator | Pleos Connect（自前）[一次] |
| 採用ミドルウェア（IVI OS）| AAOS（Android Automotive OS）[一次] |
| 採用チップ（SoC）| Qualcomm Snapdragon [一次] |
| R&D投資規模（AI関連年額）| Pleos ブランド（規模[未特定]）|

---

## 4. エコシステム：誰と作るか

| パートナー区分 | 提携先 |
|-------------|------|
| FM提供 | 自社（Gleo AI）|
| Orchestrator提供 | 自社（Pleos Connect）|
| Chip提供 | Qualcomm |
| データ・地図提供 | [未特定] |
| ADAS提供 | 自前（Lvl 2）+ 中国向け Momenta 提携可能性 [推論] |

---

## 5. 将来：どこへ向かうか

| 観点 | 状態 |
|-----|-----|
| a-1 対話Agent | 2026 Q2（Gleo）|
| a-2 ナビ・ルート | 部分実装（AAOS）|
| a-3 コックピット制御 | 部分実装（Pleos）|
| a-4 乗員ケア | [未特定] |
| a-5 コマース | [未特定] |

- 2027予測：P1-E（量産スケール拡大）
- 2030予測：P1-E（2,000万台搭載達成）

---

## 6. Honda 示唆（So What）

### 6.1 何を学べるか
- 西側 OEM で「段階2 量産済」の最初の事例。2026-04-30 ローンチで「できる」を証明した [一次]
- FM Level B を自社子会社（42dot）＋通信会社（SKT）連合で構築したモデルは、Honda が単独で Full Stack FM を持てない場合の現実解として参照可能
- 2030 2,000万台（Hyundai/Kia/Genesis 合算）という具体目標は Honda の目標設定精度向上の参照軸になる

### 6.2 警鐘 or 注意点
- SKT Sovereign AI コンソーシアム基盤は「外部ウェイトの Fine-tune」であり完全内製ではない。FM 主権は部分的
- AAOS 採用は Google エコシステム依存度が高く、長期的な Orch 独立性に課題。特に Google が AAOS を有料化または仕様変更した際のリスク

### 6.3 Honda の現在地との差分
Honda 段階2 量産前（ASIMO OS Orch [未特定]・Gemini API）と Hyundai 段階2 量産済（Pleos Connect Orch 自前・Gleo AI Level B）の差分は「量産実績」と「FM Level B 確定」の2点。Honda がいずれかを達成すれば段階2 量産済に到達する。

---

## 7. [未特定] 残課題

- SKT Sovereign AI コンソーシアム基盤 FM の詳細仕様（理由：コンソーシアム全体の非公開）
- 42dot Fine-tune データの種類・規模（理由：社内仕様、非公開）
- 2030 2,000万台達成の予算・OTA更新投資規模（理由：公式未開示）
- 中国向け Gleo AI または別 FM 採用可能性（理由：AAOS 制約で中国展開が複雑になる可能性）

## 8. V3 検証記録（2026-05-01）

| 検証項目 | 結果 | 根拠 |
|----|----|----|
| 第1搭載車種 | GRANDEUR（韓国）→ 欧州 i30 に修正 | Hyundai Motor PR 確認 [一次] |
| ローンチ日 | 2026-04-30 正式ローンチ | 公式発表 [一次] |
| FM Level B | 確認（42dot + SKT Sovereign AI コンソーシアム）| 発表文「proprietary LLM technology」[一次] |
| 2030 台数目標 | 2,000万台（Hyundai/Kia/Genesis 合算）| 維持 [一次] |
