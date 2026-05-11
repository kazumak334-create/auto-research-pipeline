# PEST分析: ロボティクス産業（産業用・ヒューマノイド・自律移動体）
**フレーム:** PEST × 少子高齢化 × 製造業代替需要  
**最終更新:** 初版（2026-05-11）  
**更新者:** auto-agent

---

## 概要・主要論点

ロボティクスは「産業用アーム」から「ヒューマノイド汎用労働機械」へのパラダイム転換期（2024-2030年）。
Tesla Optimus / Figure AI / Unitree（中国）が価格競争を先導し、BOM $20,000以下を目標に量産化競争が始まった。
少子高齢化による労働力不足が需要サイドを構造的に押し上げる。

**2026年5月時点のキーナンバー:**

| 指標 | 数値 |
|------|------|
| 産業用ロボット年間設置台数 | ~590,000台（2024年、IFR） |
| ヒューマノイドロボット市場 | ~$1.5B（2025年推計）→$38B（2035年予測） |
| Tesla Optimus 生産計画 | 2025年1,000台→2026年10,000台 |
| Figure AI 評価額 | $2.6B（2024年） |
| Unitree G1 価格 | ~$16,000 |
| 日本製造業ロボット密度 | 世界3位（397台/1万人） |

---

## P: 政治・規制 (Political)

### 主要監視テーマ
- 中国ロボティクス産業政策：「ロボット＋」行動計画・ヒューマノイド補助金
- 日本ロボット安全規制：ISO 10218改訂・協働ロボット（コボット）認定
- 米国対中ロボット輸出規制：AI搭載ロボットへの技術移転制限検討
- EU AIアクト高リスク分類：ロボット自律行動への適用範囲
- 軍事用途：自律型戦闘ロボット（UGV）の国際規制論議
- 公共空間ロボット：配送ドローン・自律走行車の道路使用許可制度

### 検索クエリテンプレート（{YYYY-MM}を当日年月に置換）
```
China robotics policy humanoid subsidy plan {YYYY-MM} site:reuters.com OR site:ft.com
Japan robot safety standard ISO collaborative robot {YYYY-MM}
US China robotics export control AI robot {YYYY-MM}
EU AI Act autonomous robot high risk classification {YYYY-MM}
autonomous delivery drone regulation {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## E: 経済 (Economic) ※マンキュー変数ベース

### マクロ変数→ロボティクス産業への波及
| マンキュー変数 | ロボティクスへの影響 |
|-------------|------------------|
| 労働コスト上昇 | ロボット導入ROI改善→普及加速の主ドライバー |
| 金利高止まり | 設備投資判断の割引率上昇→CapExサイクル抑制 |
| 中国製造業コスト上昇 | ロボット代替需要増加（人件費逃げ場喪失） |
| 円安 | 日本ロボットメーカー輸出競争力→Fanuc / Yaskawa有利 |

### 産業固有経済指標
**監視ポイント:**
- 産業用ロボット受注：Fanuc / Yaskawa / KUKA / ABB 四半期受注動向
- ヒューマノイドBOM：主要部品コスト（アクチュエーター / センサー / バッテリー）
- 自動化投資：製造業・物流・小売の設備投資内訳
- ロボット普及率：国別ロボット密度（IFR年次）
- Teslaロボット：Optimus量産コスト公表値の推移

**検索クエリ:**
```
industrial robot orders Fanuc Yaskawa KUKA quarterly {YYYY-MM}
humanoid robot BOM cost actuator sensor {YYYY-MM}
Tesla Optimus production cost update {YYYY-MM}
manufacturing automation investment CapEx {YYYY-MM}
robot density IFR annual report 2026
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## S: 社会・労働市場 (Social)

### 主要監視テーマ
- 少子高齢化：日本・韓国・中国での製造業労働力不足の実態データ
- ロボット置換不安：製造業労働者の雇用不安・組合の対応
- 技能転換：ロボット監視・プログラミング人材需要の急増
- 高齢者介護：介護ロボット普及（日本の介護離職問題への対応）
- 教育：STEM教育・ロボットプログラミング（小学生から）

### 検索クエリテンプレート
```
labor shortage manufacturing aging population Japan Korea China {YYYY-MM}
robot job displacement manufacturing union response {YYYY-MM}
care robot elderly nursing Japan {YYYY-MM}
robot programming STEM education {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## T: 技術 (Technological)

### 主要監視テーマ

**ヒューマノイドロボット:**
- Tesla Optimus：量産進捗・Tesla工場内作業実績・市販計画
- Figure AI（Figure 02）：BMW工場実証→商業展開
- Boston Dynamics Atlas（電動版）：商用提供開始
- Unitree G1/H1：低価格戦略・開発者エコシステム構築
- Agility Robotics Digit：Amazonとの物流協業実績
- 中国勢：UBTECH Walker X / Fourier GR-1

**産業用ロボット進化:**
- AIビジョン統合：2D→3D → 4D（時系列予測）で汎用ピッキング実現
- ソフトロボティクス：把持力可変アクチュエーター（FESTO / Soft Robotics）
- 協働ロボット（コボット）普及：Universal Robots / FANUC CRX

**自律移動（AMR・AGV）:**
- 物流AMR：Amazon Proteus / Boston Dynamics Stretch
- 建設ロボット：自律建機（Caterpillar / KOMATSU ICT建機）
- 農業ロボット：自律収穫機・農薬散布ドローン

### 検索クエリテンプレート
```
Tesla Optimus humanoid robot production update {YYYY-MM}
Figure AI robot BMW factory deployment {YYYY-MM}
Boston Dynamics Atlas commercial availability {YYYY-MM}
Unitree robot price developer ecosystem {YYYY-MM}
UBTECH Fourier humanoid robot China {YYYY-MM}
collaborative robot cobot industrial AMR {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->

---

## 競争ポジション概観

| 企業 / グループ | 強み | 主要リスク |
|--------------|------|-----------|
| Tesla Optimus | AI/FSD転用・垂直統合・大量生産経験 | 規制・品質・ユースケース実証 |
| 日本勢（Fanuc / Yaskawa） | 産業用精度・信頼性・アフターサービス | ヒューマノイド移行遅れ |
| 中国勢（Unitree / UBTECH） | 低価格・政策支援・量産速度 | 輸出規制リスク |
| Boston Dynamics（Hyundai） | 運動性能・ブランド | コスト高・商業展開遅れ |
| Figure / Agility / 1X | 特定産業実証 | 資金調達依存・スケール未達 |

---

## 更新ログ

| 日付 | 更新内容 | 更新者 |
|------|---------|--------|
| 2026-05-11 | 初版作成。ヒューマノイド×産業用×AMRの3カテゴリでPEST設計 | auto-agent |
