# 改进模式目录

## 目录

- [选用规则](#选用规则)
- [Search Depth](#search-depth)
- [Data Gates](#data-gates)
- [Specificity](#specificity)
- [Beginner Clarity](#beginner-clarity)
- [Brilliance](#brilliance)
- [Anti-Pattern Depth](#anti-pattern-depth)
- [Teaching Value](#teaching-value)
- [Deliverable Spec](#deliverable-spec)
- [优先级](#优先级)

## 选用规则

- 触发：该维低于 60，或它是综合分低于 70 时的最弱维。
- 一次 evolve 只用一条模式。
- 旧/新是改写形状，不是交付物原文。
- 补丁不得把产品名、城市、SKU 写进 skill；字段从产品上下文填。

## Search Depth

### SD-1 补查询形状

- 诊断：Collect 只有「搜索…」或条数不够。
- 修改：加 5–10 条查询形状，每条含字段名（品类、市场、年份），并写「用 Apify 搜索查证」。
- 旧：搜索竞品价格。
- 新：用 Apify 搜索查证 `{品类字段} {市场字段} wholesale price {年份}`；空结果则抓取指定 URL 的正文；仍空则记缺口。

### SD-2 来源标注

- 诊断：Analyze / 产出未要求 URL。
- 修改：清单加「每条核心建议后写来源 URL 或产品上下文路径（不粘贴原文）」。

## Data Gates

### GT-1 量化门槛

- 诊断：无最低数据或门槛不可检查。
- 修改：按阶段给数字。基础调研 ≥30 条可引用事实；SEO/内容/获客 ≥20；CRO/增长/测量 ≥15；元技能至少 2 个外部 URL 或明确离线。写不达标：补采或停，不编。

### GT-2 时效

- 诊断：数字无日期。
- 修改：价格类须采集日期间隔短于 6 个月；趋势短于 12 个月；否则标过期。

### GT-3 双源

- 诊断：关键价格/规模只有单源。
- 修改：清单加「每个关键数字 ≥2 个独立来源；渠道以产品上下文为准」。

## Specificity

### SP-1 上下文适配

- 诊断：不读 `product_context` 也能跑完。
- 修改：步骤 1 读台账路径；查询与产出绑定品类/市场/约束字段；清单禁止写死单一产品名。
- 旧：至少提及三种固定材质名。
- 新：交付物须出现产品上下文里的材质/工艺/竞品名，并标注出处；skill 只写「读这些字段」。

### SP-2 去掉订阅口吻

- 诊断：paywall、signup、freemium、免费试用当主 CTA。
- 修改：改成询盘/要规格/要样品。signup-flow → inquiry-flow；free trial → sample request。

### SP-3 市场差异

- 诊断：策略不区分目标市场。
- 修改：加「按市场调整」：从上下文的市场字段列 2–3 条差异（文化、气候、渠道），每条写改什么。

## Beginner Clarity

### BA-1 前置条件

- 诊断：默认用户已有账号或素材。
- 修改：步骤前加可勾选前置（哪类后台、最少素材件数、指到哪个上游 skill）。

### BA-2 失败分支

- 诊断：只有成功路径。
- 修改：关键步加「如果失败」。
- 旧：爬竞品站。
- 新：用 Apify 搜索查证。空则抓取指定 URL 的正文。仍失败：记 blocked，换下一条，不编造。

### BA-3 术语表

- 诊断：术语未解释。
- 修改：在 skill 末或 `references/` 加术语（MOQ、Incoterms、询盘）。不把工艺专名当全局必写项。

## Brilliance

### BR-1 跨行业查询

- 诊断：只搜本品类。
- 修改：Collect 加 2–3 条相邻行业查询形状（家具、建材、照明等），字段仍从上下文填。

### BR-2 反常识检查

- 诊断：全是最佳实践。
- 修改：Analyze 加三问：反过来做会怎样；这条常识是否有来源；`brilliance-patterns.md` 有无可用模式。

### BR-3 不对称优势

- 诊断：未区分小团队与大厂。
- 修改：Analyze 加响应速度、定制门槛、人格品牌、透明度四维，只写比较框架，不写死小时数。

## Anti-Pattern Depth

### AP-1 可操作反模式

- 诊断：易错少于 5，或全是「不要编造」。
- 修改：补到 ≥8，且至少 4 条是该 skill 独有（预算拆分、停手条件、禁止把例子写入交付物、禁止工具 ID）。
- 形状：不要把小预算均分到四个渠道；先验证一个渠道的询盘成本。

## Teaching Value

### TV-1 补 WHY

- 诊断：纯指令。
- 修改：每个核心建议后加两句原理（机制 + 若相反会怎样）。
- 旧：广告用精确匹配。
- 新：广告用精确匹配。原因：B2B 词搜索量小、意图强；宽匹配会接到无采购意图的浏览词，浪费预算。

### TV-2 原理旁注

- 诊断：无方法论提示。
- 修改：在关键步旁用引用块写一条机制名（社会证明、沉没成本、风险规避），并说明本步怎么用。禁止把教学旁注复制进交付物。

## Deliverable Spec

### DS-1 字段与 min_rows

- 诊断：未定义列名或完成条件。
- 修改：对照 dependency-graph 的 expected output 补字段名、min_rows、`source` 列。

### DS-2 产出路径

- 诊断：路径是仓外目录或未写。
- 修改：战役产出 `deliverables/marketing/<阶段小写>/` 或 `deliverables/lead/<阶段小写>/`；teach/eval 元产出 `deliverables/marketing/00-system/`。

## 优先级

多维都低时，evolve 仍只修最弱维。并列时按权重：Beginner Clarity → Search Depth / Specificity / Brilliance → Data Gates / Anti-Pattern Depth / Teaching Value → Deliverable Spec。
