# PEST分析: 半導体産業
**フレーム:** PEST × 地経学（輸出規制・供給鎖再編）  
**最終更新:** 初版（2026-05-11）  
**更新者:** auto-agent

---

## 概要・主要論点

半導体は「産業のコメ」から「地政学の兵器」へ転化した。
米国輸出規制（EAR）・中国の対抗措置（ガリウム/ゲルマニウム/黒鉛輸出規制）・CHIPS法投資が三つ巴で進行中。
AI需要が需要サイクルを塗り替え、先端ロジック（AI GPU / 推論チップ）と汎用ロジック・メモリの二極化が加速。

**2026年5月時点のキーナンバー:**

| 指標 | 数値 |
|------|------|
| 世界半導体市場規模 | ~$650B（2025年推計） |
| AI GPU市場（NVIDIA HGX系） | ~$120B（2025年推計） |
| TSMC 3nm/2nm量産 | N3量産中 / N2量産2025年後半開始 |
| 中国のガリウム輸出シェア | 世界の約80% |
| CHIPS法補助金決定額（米国） | $280B中 約$50B半導体向け |

---

## P: 政治・規制 (Political)

### 主要監視テーマ
- 米国輸出規制（BIS / EAR）：エンティティリスト追加・A100/H100/H200相当品規制強化
- CHIPS法実装：TSMC・Samsung・Intel補助金条件（中国生産制限10年）
- 中国の対抗措置：ガリウム・ゲルマニウム・黒鉛・希土類の輸出規制強化
- 蘭ASML EUV輸出規制：中国向けDUV制限の段階的強化
- EU半導体法（European Chips Act）：2030年世界シェア20%目標の実現可能性
- 日本半導体助成（ラピダス・TSMC熊本・マイクロン）進捗

### 検索クエリテンプレート（{YYYY-MM}を当日年月に置換）
```
US semiconductor export control BIS Entity List update {YYYY-MM} site:reuters.com OR site:ft.com
CHIPS Act funding semiconductor factory update {YYYY-MM}
China gallium germanium graphite export restriction {YYYY-MM}
ASML EUV DUV export control Netherlands China {YYYY-MM}
Japan semiconductor subsidy Rapidus TSMC Kumamoto {YYYY-MM}
EU European Chips Act 2030 target {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: 米国BIS 2026年5月、対中半導体輸出規制追加検討。AI GPU需要急増で規制強化圧力継続。

---

## E: 経済 (Economic) ※マンキュー変数ベース

### マクロ変数→半導体産業への波及
| マンキュー変数 | 半導体産業への影響 |
|-------------|-----------------|
| 金利（高止まり） | 半導体工場建設の資本コスト増大（TSMC新工場IRR圧迫） |
| ドル高 | TSMCの台湾ファブ競争力↑、ただし米国工場コスト相対上昇 |
| AI投資ブーム | GPU・HBM・CoWoSパッケージング供給逼迫継続 |
| 中国GDP鈍化 | 汎用メモリ・コンシューマー向け需要回復遅延 |

### 産業固有経済指標
**監視ポイント:**
- DRAM / NAND価格サイクル（DDR5・232層NAND ASP推移）
- HBM3E/HBM4需給バランス（SK Hynix / Micron / Samsung生産能力）
- NVIDIA / AMD GPU ASP・粗利率（AIチッププレミアム持続性）
- TSMC 先端ノード稼働率・コスト/ウェーハ（3nm/2nm）
- 半導体装置市場：ASML/Applied Materials/LAM受注残

**検索クエリ:**
```
DRAM NAND memory price trend ASP {YYYY-MM} site:trendforce.com
HBM supply demand SK Hynix Micron Samsung {YYYY-MM}
NVIDIA AMD GPU revenue margin quarterly {YYYY-MM}
TSMC capacity utilization wafer cost 3nm {YYYY-MM}
semiconductor equipment orders ASML Applied Materials {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: NVIDIA Blackwell 2026年中頃完売。$500B予約パイプライン。GB200 NVL72が主力SKU。

---

## S: 社会・人材 (Social)

### 主要監視テーマ
- 米中半導体人材デカップリング：中国系エンジニアのビザ審査強化・米国大学院制限
- 台湾有事リスク認識の変化と製造拠点分散への圧力
- 半導体工場立地に伴う地域社会影響（水使用・電力消費・雇用）
- 日本半導体復活の人材確保課題（九州・北海道）

### 検索クエリテンプレート
```
semiconductor talent shortage engineer visa US China decoupling {YYYY-MM}
Taiwan semiconductor risk geopolitical diversification {YYYY-MM}
semiconductor factory water electricity community impact {YYYY-MM}
Japan semiconductor engineer shortage Kyushu Hokkaido {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: TSMC N2（2nm）月産10万枚、2026年ソールドアウト。Apple・NVIDIAが優先確保。

---

## T: 技術 (Technological)

### 主要監視テーマ
- プロセス技術：TSMC N2（2025年量産）/ Intel 18A（2025年後半）/ Samsung SF2
- AI特化チップ：NVIDIA Blackwell GB200 / AMD MI300X / Google TPU v5
- HBMメモリ：HBM3E量産→HBM4移行ロードマップ（2025-27年）
- パッケージング：CoWoS-S/L供給ボトルネック解消進捗
- 中国ファブ：SMIC N+2（7nm相当）量産規模拡大・HuaweiのAscend 910B/C自給化
- 化合物半導体：SiC/GaN（EV向けパワーデバイス）コスト曲線
- 次世代：Gate-All-Around（GAA）トランジスタ量産移行・光インターコネクト

### 検索クエリテンプレート
```
TSMC N2 2nm production yield {YYYY-MM}
NVIDIA Blackwell AI GPU supply shipment {YYYY-MM}
HBM4 roadmap SK Hynix Micron Samsung {YYYY-MM}
SMIC China advanced node production {YYYY-MM}
Huawei Ascend 910 chip performance benchmark {YYYY-MM}
SiC GaN power semiconductor EV cost {YYYY-MM}
```

### 最新動向（更新欄）
<!-- auto-agent が毎日追記 -->
- 2026-05-11: HBM3e需要急増。SK Hynix・Micronが供給拡大加速。2026年末まで需給タイト。

---

## 産業横断リスク・示唆

| リスク | 確率 | 産業インパクト |
|--------|------|--------------|
| 米中半導体輸出規制エスカレーション（ASML DUV全面禁止） | 30% | 中国自動車・AI産業への先端半導体供給断絶 |
| 台湾海峡危機（TSMC生産停止） | 10% | 世界半導体供給の60%超が停止→全産業麻痺 |
| AI需要バブル崩壊（GPU過剰在庫） | 25% | 2026-27年調整局面・NVIDIA株価急落 |
| 中国先端半導体自給化加速（2028年7nm自給） | 40% | 長期的に輸出規制の効果逓減 |

---

## 更新ログ

| 日付 | 更新内容 | 更新者 |
|------|---------|--------|
| 2026-05-11 | 初版作成。輸出規制・AI需要・中国自給化の3軸でPEST設計 | auto-agent |
| 2026-05-13 | 最新動向追記 | auto-agent |

## 最新動向

### 2026-05-13
- **[Political]** 米国の中国技術制限の執行に課題あり（Legis1報道）。制裁抜け穴問題が議会で論点化
- **[Technology]** NVIDIA Blackwell が分散型エッジAI推論グリッドに展開（Zero Latency）。データセンター集中から分散エッジへの需要分散が進行
- **[Technology]** AMD が Samsung 2nm プロセスとの提携交渉を「先進段階」と発表。TSMC の2nm ウェーハが2028年まで満杯のため代替確保が急務
- **[Economic]** Micron YTD +68%。HBM需要爆発でQ1 FY2026売上 $13.64B（+57% YoY）、粗利56%。HBM4量産ロードマップが次の焦点
- **[Technology]** TSMC 2nm 供給制約 → AMD/Tesla が Samsung Foundry（GAA 2nm）へ分散発注を検討。Samsung の歩留まり改善が鍵
