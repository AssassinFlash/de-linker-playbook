# 自适应产品品类分类

## 目录

- [分类逻辑](#分类逻辑)
- [预定义品类](#预定义品类)
- [新建品类](#新建品类)
- [跨品类产品](#跨品类产品)

本文件是分类脚手架，不是事实库。表内「先验区间」禁止无 `source_hint` 写入任何交付物；查不到则写 Unknown。产品参数只来自台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`），需要时再读 `~/Documents/New/fact-base/`。不要把本表数字或标准编号当成用户已持有的认证。

## 分类逻辑

1. 从产品描述判定 `primary_family`。
2. 跨品类产品再判定可选的 `secondary_family`。
3. 加载对应品类的 KPI 与合规查证清单。
4. 对不上任何预定义品类：新建，列出 5–7 个 KPI 与合规需求。

## 预定义品类

### 1. Packaging（金属 / 塑料 / 纸 / 玻璃）

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Coating adhesion | 划格/附着力方法（常查 ASTM D3359） | 4B–5B |
| Food-contact safety | 食品接触法规 | Pass/Fail |
| Sealing strength | 热封强度 | 3–8 N/15mm |
| Thickness uniformity | 表面厚度偏差 | +/- 5% |
| Print quality | 分辨率、色差 | Delta E < 2 |

**合规查证：** FDA（US）、EU 1935/2004 + EU 10/2011（EU）、GB 4806（CN）、JFSL 370（JP）  
**实验室方向：** SGS、Intertek、TUV、Bureau Veritas（是否已出报告以产品上下文为准）

### 2. Textiles & Apparel

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Fiber composition | 成分偏差 | +/- 3% |
| GSM | 克重 | 按织物类型查 |
| Color fastness | 耐洗/耐光/耐磨 | Grade 3–5 |
| Tensile strength | 断裂强力 | 按织物类型查 |
| Shrinkage | 洗涤后尺寸变化 | < 3–5% |

**合规查证：** REACH（EU）、CPSIA（US）、OEKO-TEX Standard 100、GOTS（有机）  
**实验室方向：** SGS、Intertek、BV、Hohenstein

### 3. Electronics & Lighting

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Luminous efficacy (lm/W) | 光效 | 80–200 lm/W |
| CRI | 显色指数 | > 80（可接受），> 90（更好） |
| CCT | 相关色温 | 2700–6500K |
| IP rating | 防护等级 | IP20–IP68 |
| Lifespan | 标称寿命 | 25,000–50,000 hrs |

**合规查证：** UL（US）、CE + RoHS（EU）、CCC（CN）、PSE（JP）、KC（KR）  
**实验室方向：** UL、TUV、SGS、Intertek

### 4. Mechanical Parts

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Material grade | 牌号以产品上下文为准 | 按牌号查 |
| Hardness | Rockwell / Brinell / Vickers | 按材料查 |
| Tolerance | 尺寸公差 | +/- 0.01 至 +/- 0.1 mm |
| Load rating | 许用载荷 | 按工况查 |
| Surface finish | Ra | 0.4–6.3 um |

**合规查证：** ISO 9001、IATF 16949（汽车）、AS9100（航空）、ABEC（轴承）  
**实验室方向：** SGS、Bureau Veritas、DNV、Lloyd's

### 5. Machinery & Equipment

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Throughput | 产能/节拍 | 按机型查 |
| Duty cycle | 连续运转能力 | 60–100% |
| Power consumption | 单位产出能耗 | 按机型查 |
| Noise level | 运行噪声 | < 75–85 dB |
| MTBF | 平均无故障间隔 | > 5,000 hrs |

**合规查证：** 目标市场现行机械安全法规（写入时核实施行文本，勿直接抄指令号）、UL（US）、OSHA（US）、CSA（CA）  
**实验室方向：** TUV、SGS、Bureau Veritas、UL

### 6. Chemicals / Coatings

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| SDS completeness | GHS 安全数据表 | 16 sections |
| VOC content | 挥发性有机物 | < 50 g/L（低 VOC 口径须查证） |
| Viscosity | 流变 | 按类型查 |
| Adhesion | 拉开/划格 | ASTM D3359 4B+ |
| Coverage rate | 单位面积用量 | 按类型查 |

**合规查证：** REACH + CLP（EU）、Prop 65（California）、RoHS、TSCA（US）  
**实验室方向：** SGS、Intertek、Eurofins、NSF

### 7. Furniture / Office

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Static load | 静载 | 100–200 kg |
| Dynamic load | 循环载荷 | 50,000–100,000 cycles |
| Finish durability | 耐划 | ASTM D3363 |
| Formaldehyde emission | 甲醛释放 | E0/E1/CARB2 |
| Stability | 倾翻 | EN 1022 pass |

**合规查证：** BIFMA（US）、EN 527/1335（EU）、CARB2（California）、FSC（木材来源）  
**实验室方向：** SGS、TUV、UL、FIRA

### 8. Plastics & Molding

| KPI | 查证方向 | 先验区间（须查证） |
| --- | --- | --- |
| Resin type | 树脂牌号以产品上下文为准 | PP、ABS、PC、PA 等须核对 |
| Melt flow index | MFI（常查 ASTM D1238） | 按树脂查 |
| Shrinkage rate | 成型后收缩 | 0.3–2.5% |
| Tooling life | 模具寿命 | 100K–1M shots |
| Impact strength | Izod/Charpy（常查 ASTM D256） | 按材料查 |

**合规查证：** FDA（食品接触）、RoHS（电子）、REACH（EU）、UL 94（阻燃）  
**实验室方向：** SGS、Intertek、UL、TUV

## 新建品类

对不上预定义品类时，新建一条：

1. **Family name** — 可检索的品类名
2. **5–7 KPIs** — 该类最关键的可测量参数
3. **Compliance needs** — 按目标地区列出待查认证与标准
4. **Recommended testing labs** — 该类常见的第三方实验室方向
5. **Typical spec ranges** — 行业通行区间，写入交付物时必须带 `source_hint`

## 跨品类产品

产品跨两个品类时：

- `primary_family`：核心功能所属品类
- `secondary_family`：结构/外壳等从属品类
- KPI 合并，主品类指标优先
- 合规必须覆盖两个品类，缺一不可
