# 付费广告方法

读本文件前先确认 `SKILL.md` 已判定本 skill 适用。查询意图、最低条数、聚类、战役结构、表列与可验证断言以本文为准。

## 目录

- [输入](#输入)
- [采集](#采集)
- [分析](#分析)
- [交付](#交付)
- [反模式](#反模式)
- [质量闸门](#质量闸门)
- [可验证断言](#可验证断言)

品类、目标市场、产地、已开通平台一律取产品上下文对应字段，不在本文件填值。

## 输入

先读台账 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；需要参数再读同目录 `fact-base/`）。上游若已存在则读：

- `deliverables/marketing/01-foundation/` 定位、买家角色、竞品名单
- `deliverables/marketing/02-seo/seo-audit.md` 关键词优先级与已核 CPC 线索
- 用户本轮提供的广告账户导出或表现表

从上下文或用户本轮消息列出（缺则记缺口，不编造）：

- 品类、目标市场、所在地（仅用于信任文案，不锁产地话术）
- 战役目标：询盘量、报价请求、样品、品牌认知
- 月预算、目标询盘成本
- 落地页 URL、询盘表与转化追踪现状
- 已开通平台名单

产品事实不写进 skill，不另写公司档案。

## 采集

默认一条能力：用网页搜索查证。需要原文时抓取指定 URL 的正文（含动态广告透明页）。用户已配置网页采集服务时，才用它抓公开页。搜索不可用则停止并写缺口，不编造、不并列多引擎菜单。多页并行时 dispatch a subagent, else do it inline。

把产品上下文的品类与目标市场代入下列意图，至少 12 条查询，每条记下 URL、摘录、访问日期：

1. 品类 + Google Ads CPC B2B
2. 品类 + LinkedIn ads cost per lead
3. 品类 + Meta ads B2B
4. B2B 品类 paid search benchmarks + 当前或下一自然年
5. 目标市场 + 品类 + buyer keywords
6. Google Ads B2B landing page
7. B2B paid ads benchmark manufacturing + 当前或下一自然年
8. 品类 competitor ads
9. 目标市场 + procurement manager + 品类
10. B2B Google Ads negative keywords
11. 品类 + 目标渠道付费推广（渠道名取产品上下文，不在本文件填值）
12. LinkedIn ads + 品类 + ROI

### 竞品创意

- 在 Meta Ad Library 按竞品品牌或品类检索，抓取广告透明页正文。
- 抓取竞品落地页与可见广告文案。
- 用网页搜索查证广告创意案例、截图库或广告透明清单。

每条创意记录：竞品名、平台、格式、标题、正文、CTA、视觉风格、落地页 URL、`source_url`、访问日期。

### 关键词与 CPC

至少 50 条关键词，按意图分组。优先商业词与应用词。

每条记录：keyword、match_type、cpc_usd、monthly_volume、competition、intent、ad_group、`source`。

CPC、检索量、竞争度只填有来源的数字；没有则该列写「公开源未找到」，禁止估计。`source` 写查询串或页面 URL。

### 受众与市场信号

- 查目标市场的行业刊物、采购论坛、名录中的买家检索措辞。
- 用公开职位信息交叉核对目标角色（采购、项目、指定人、经销、质量/合规），角色以产品上下文为准；上下文没有则在上述五档中选最贴近的一档，并标明「角色未在上下文出现，暂用」。

### 最低条数

| 项 | 数量 | 引用 |
| --- | --- | --- |
| 带 CPC 或显式缺口的关键词 | ≥50 | 每行 `source` |
| 已分析竞品创意 | ≥10 | 每行 `source_url` |
| 竞品或行业落地页 | ≥5 | 每行 `source` 与评注 |
| 预算情景 | 3 档 | 每档引用已采集 CPC |
| 平台基准（CTR / CPC / CVR） | 每个拟投平台 ≥1 | 每条引来源 |

### 采集门

未满足则不准进入把预算当事实的分析结论（只写缺口）：

- [ ] ≥12 条查询，每条有 URL 与访问日期
- [ ] ≥50 条关键词，每条有 `source`；CPC 空值已标「公开源未找到」
- [ ] ≥10 条竞品创意，每条有 `source_url`；或已写「未找到公开创意」并改用已核行业基准
- [ ] ≥5 个落地页分析
- [ ] 每个拟投平台至少一条基准来源，或该平台已从推荐名单剔除并说明

## 分析

### 关键词按意图聚类

| 意图 | 检索形态 | 战役类型 |
| --- | --- | --- |
| 商业 | 品类 + supplier / buy / wholesale | Search — Core Product |
| 应用 | 品类 + 产品上下文中的应用或项目类型 | Search — Application |
| 地域 | 品类 + supplier + 目标市场 | Search — Geographic |
| 品牌 | 已核竞品品牌 + 品类 | Brand Protection |
| 信息 | how to choose / types of + 品类 | 排除或仅 Display |

意图必须能从查询措辞读出。信息类默认不进搜索核心组。

### 平台预算

对每个候选平台：

- 预计点击 = 月预算 ÷ 已采集 CPC
- 预计询盘 = 点击 × 已采集落地页 CVR（无 CVR 则询盘列写缺口，不发明转化率）
- CPI = 预算 ÷ 预计询盘（询盘为缺口则 CPI 为缺口）
- 按 CPI 与目标市场买家匹配度排序

三档情景（测试 / 增长 / 放量）的金额取用户本轮或产品上下文中的预算约束；上下文没有则只给计算式，不填无来源档位数字。每档引用 Phase 采集的 CPC 区间。

禁止：把 Google Ads 的 CPC 直接套到 LinkedIn 或 Meta；禁止在无 CPC 时输出可执行预算表。

### 战役结构

```
Account
├── Campaign 1: Search — Core Product
│   ├── Ad Group: 品类词
│   ├── Ad Group: 型号 / 规格词
│   └── Ad Group: 定制 / OEM 词
├── Campaign 2: Search — Application
│   ├── Ad Group: 应用类型 A（取上下文）
│   ├── Ad Group: 应用类型 B
│   └── Ad Group: 行业垂直
├── Campaign 3: Search — Geographic
│   ├── Ad Group: 目标市场英语词
│   └── Ad Group: 本地语言词（市场需要时）
├── Campaign 4: Remarketing — Display / Social
└── Campaign 5: Brand Protection
```

至少 5 个战役，且必须有 campaign → ad group 两级。每战役写命名、日预算、出价策略、地域。多市场分开战役，不混进同一战役。

### 落地页评分

对每个已抓落地页打：

- 标题与价值主张是否对上广告承诺
- CTA 位置、文案、对比
- 信任信号（认证、项目图、客户标识、证言——仅页面已出现的）
- 表单长度与阻力
- 移动端可读信号

P0 / P1 改进必须指回具体 URL，不写空的最佳实践。

### 创意角度

买家角色从产品上下文取；没有则在采购、承包、指定人、经销、质量/合规里选，并标明「角色未在上下文出现，暂用」。不要用 C 端消费者口吻。

每个角度标注：角色、漏斗阶段、主动机、视觉方向、CTA。至少 3 个角色 × 下列四阶段均有着落或显式缺口。

| 漏斗阶段 | 创意目标 | 角度优先 | CTA 方向 |
| --- | --- | --- | --- |
| 访问 | 展示能力与范围 | 项目组合、规格范围 | 看系列 / 要报价 |
| 询盘 | 建立信任 | 工厂资质、样品、目录 | 要样品 / 下目录 |
| 样品 / 报价 | 降低阻力 | 起订量、交期、直连工厂 | 联系工厂 / 约通话 |
| 订单 / 再营销 | 转化或复购 | 项目证据、复购激励 | 要报价 / 再下单 |

### A/B 变量

至少 3 个可测变量，且必须能回溯竞品审计：

1. 信息角度：能力 / 价格 / 社会证明 / 交期
2. 视觉类型：装机或项目现场 / 产品特写 / 工厂过程
3. CTA：要报价 / 要样品 / 下目录

### 数据缺口时

- 无 CPC：明确写出，推荐上线前在广告平台关键词规划工具复核；预算情景不填当作事实的数字。
- 无竞品创意：记缺口，建议按月回看广告透明页，分析改用已核行业基准并标注。
- 无平台基准：该平台不进入可执行推荐，或标「仅结构建议、数字待核」，禁止填无来源区间。

## 交付

主文档 `deliverables/marketing/04-acquisition/paid-advertising.md` 必含：执行摘要、关键词研究、竞品广告与创意审计、预算情景、落地页建议、战役结构、创意 brief、行动清单、缺口、可验证断言。每个数字引用采集来源。

否定词表写进关键词研究或战役结构，≥20 条。

UTM 规范与询盘表转化追踪写进行动清单。未核追踪则行动清单不得把「上线」标为 P0 完成项。

### 工作簿

从 `templates/paid-advertising-blueprint.xlsx` 复制到 `deliverables/marketing/04-acquisition/paid-advertising-blueprint.xlsx` 后填行。不能写表时改同目录 JSON，字段与下行一致，每对象有 `source`。

| 表 | 列 | 最低行数 |
| --- | --- | --- |
| Campaigns | campaign_name, platform, objective, budget_usd_daily, geo_target, audience, landing_page, bid_strategy, status, source | ≥5 |
| Audiences | audience_name, type, criteria, exclusion, estimated_reach, source | ≥3 |
| Creatives | creative_id, format, angle, headline, description, cta, visual_brief, source | ≥15 |
| Keywords | keyword, match_type, cpc_usd, volume, intent, ad_group, source | ≥50 |

可按平台加列（如 `ab_variant`、`budget_scenario`），但每行必须有 `source`。`estimated_reach` 无来源则写「公开源未找到」，禁止估计。

### JSON 字段（不能写表时）

```json
{
  "keyword": {
    "keyword": "string",
    "match_type": "exact|phrase|broad",
    "monthly_volume": "number|null",
    "cpc_usd": "number|null",
    "competition": "low|medium|high",
    "intent": "commercial|application|geographic|brand|informational",
    "priority": "P0|P1|P2",
    "ad_group": "string",
    "source": "string"
  },
  "competitor_ad": {
    "competitor": "string",
    "platform": "string",
    "ad_type": "image|video|carousel|text",
    "headline": "string",
    "body_copy": "string",
    "cta": "string",
    "visual_style": "string",
    "landing_page_url": "string",
    "source": "string"
  },
  "budget_scenario": {
    "scenario": "string",
    "platform": "string",
    "monthly_budget": "number",
    "expected_clicks": "number",
    "expected_cpc": "number",
    "expected_leads": "number",
    "cost_per_lead": "number",
    "source": "string"
  }
}
```

预算对象仅在对应数字均有采集来源时输出；否则省略该对象，改在缺口节写验证路径。

### 平台选择（须有采集证据才推荐）

| 平台 | 适用 | 启用条件 |
| --- | --- | --- |
| Google Ads | 高意图搜索 | 买家在搜品类 + supplier 一类词，且已有 CPC 来源 |
| Meta | 视觉展示、再营销、认知 | 已有项目或产品实拍，且有基准或显式缺口 |
| LinkedIn | 按职位 / 行业触达决策人 | 相对搜索 CPC 的成本理由已写清 |
| YouTube / Display | 认知与组合展示 | 已有过程或装机视频资产 |
| 目标渠道中的 B2B 平台付费位 | 有采购意图的询盘 | 产品上下文已列该渠道且有店铺或账号 |

未在产品上下文出现的平台：要推荐必须同时写机会、风险与证据缺口。

### 再营销窗口

| 阶段 | 受众 | 信息 | 窗口 |
| --- | --- | --- | --- |
| 访问 | 博客 / 图库访问、视频观看 | 组合、规格范围 | 30–90 天 |
| 访问 → 询盘 | 产品页访问、目录下载 | 工厂资质、认证、起订量 | 7–30 天 |
| 询盘 | 表单未完成、样品页访问 | 本周要报价 | 1–7 天 |

排除：现有客户、近 7–14 天已提交询盘者、停留过短的跳出、招聘页访问。窗口是结构默认，不是效果承诺。

### 指标定义

只写定义与已采集目标；数字目标取用户本轮、产品上下文或已核来源。没有则该格写「公开源未找到」。

| 指标 | 定义 |
| --- | --- |
| Cost per Inquiry (CPI) | 花费 ÷ 询盘数 |
| Inquiry ROAS | 订单收入 ÷ 广告花费 |
| Inquiry-to-Quote Rate | 收到正式报价的询盘占比 |
| Quote-to-Order Rate | 报价转订单占比 |
| Cost per Qualified Lead | 花费 ÷ 具备项目条件的询盘 |

优化目标是询盘提交（及合格询盘），不是点击。

## 反模式

- 无已采集 CPC 仍给预算。
- 猜测关键词 CPC。
- 否定词少于 20。
- 无匹配落地页策略仍写广告。
- 假定目标市场各区域 CPC 相同。
- 无成本理由把 LinkedIn 列为 P0。
- 跳过竞品创意分析。
- 无询盘表转化追踪仍建议上线。
- 多市场塞进同一战役。
- 优化点击而不是询盘。
- 小预算均分到四个平台。
- 学习期内周中大幅改预算。
- 有实拍仍用空的库存图。
- 使用注册或免费试用类 CTA。

## 质量闸门

- [ ] ≥50 关键词，CPC 有来源或显式缺口
- [ ] ≥10 竞品创意，含 `source_url`
- [ ] 3 档预算均回溯已采集 CPC，无编造数字
- [ ] ≥5 落地页分析与 P0/P1
- [ ] 否定词 ≥20
- [ ] 平台建议按证据区分，不一刀切
- [ ] 每个预算数字能指回采集来源
- [ ] 战役含 campaign → ad group
- [ ] 创意矩阵 ≥3 个买家角色
- [ ] UTM 与转化追踪已写
- [ ] 无占位文案、无未闭合待采集标记

## 可验证断言

交付物文末写 5–10 条，须能对照文件核对。最低可检项：

1. 关键词研究 ≥50 条，每条有 `source`。
2. 竞品创意 ≥10 条，每条有 `source_url`。
3. 预算情景恰好 3 档；有 CPC 来源时 `monthly_budget` 与 `expected_cpc` 为数字并引用采集数据，否则三档均在缺口节说明。
4. 落地页建议基于 ≥5 个已抓 URL。
5. 否定词 ≥20。
6. 战役结构 ≥5 个战役，含两级 hierarchy。
7. 创意 brief 每个角度标注角色与漏斗阶段。
8. 所有 CPC / 基准有来源；终稿无未闭合待采集标记。
9. 工作簿或 JSON 含 Campaigns、Audiences、Creatives、Keywords；Creatives ≥15、Keywords ≥50。
10. 行动清单含 UTM、询盘转化追踪与 P0 / P1 / P2 时间点。
