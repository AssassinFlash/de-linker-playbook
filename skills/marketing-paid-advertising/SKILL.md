---
name: marketing-paid-advertising
description: >
  Use when the user asks for paid ads, Google Ads, Meta ads, LinkedIn ads,
  PPC, SEM, ad creative, campaign planning, media buying, B2B advertising,
  付费广告, 广告投放, CPC research, or a B2B paid acquisition plan, including
  phase 4 acquisition work. Collect keyword CPC, competitor creatives, and
  platform benchmarks, then write sourced budget scenarios, campaign
  structure, and creative briefs under deliverables/marketing/04-acquisition/.
  Read the ledger product_context first; invent no CPC or conversion rates.
  Never paste skill examples into the output. Not for organic social, email
  sequences, or phase navigation.
---

# 付费广告

根据已读产品上下文与可验证公开来源，做平台选择、关键词与 CPC、竞品创意审计、预算情景与战役结构，写出创意 brief，落到 `deliverables/marketing/04-acquisition/`。不写自然社媒日历，不代发广告。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若存在则读 `deliverables/marketing/01-foundation/` 竞品稿、`deliverables/marketing/02-seo/seo-audit.md` 关键词与 CPC 线索。用户本轮给出的广告账户导出一并列入。完成：能指出品类、目标市场、战役目标、月预算或目标询盘成本、落地页 URL、转化追踪状态、已开通平台各依据哪几条；原文不拷进本仓库。品类、目标市场或落地页缺到无法圈定投放则停并写缺口，不编造公司、CPC、转化率或竞品创意。
3. **采集**。用 Apify 搜索查证关键词 CPC、平台基准、竞品创意与落地页；需要原文时抓取指定 URL 的正文（含 Meta Ad Library 等广告透明页）。默认一条能力，不并列多引擎。Apify 修复与替代取证后仍不可得则停止并写缺口。多站点或多创意并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；关键词、创意、落地页达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据推导意图聚类、平台预算、战役结构、落地页缺口、创意角度与 A/B 变量。量表、结构与表列见 `references/methodology.md`。完成：每个预算情景能回溯已采集 CPC 区间；每个推荐平台有基准来源或显式缺口；创意角度覆盖 ≥3 个买家角色与四个漏斗阶段。
5. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL 或查询串；否定词 ≥20；UTM 与询盘表转化追踪已写清；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；广告文案、关键词、字段名、文件名用英文或产品上下文的面客语种，同一段不混用。
- 目标渠道与平台名单以产品上下文为准。本方法可写 Google Ads、Meta、LinkedIn、YouTube / Display 及上下文中的 B2B 平台付费位，但排序必须按已采集 CPI 与买家检索证据，不按运营偏好。
- CPC、CTR、CVR、覆盖人数只写观察到的值；没有就写「公开源未找到」，并给出到广告平台关键词规划工具复核的路径。禁止估计后写成事实，禁止用无来源行业区间填预算。
- 缺 CPC：不准把预算情景当可执行数字输出，只写缺口与验证路径。
- 小预算不拆到四个平台；同一战役不混多个目标市场。
- 表格式交付物每行有 `source`。终稿禁止占位 URL 与未闭合的待采集标记。
- 缺来源或Apify 修复与替代取证后仍不可得：停止并写缺口，不编造。

## 写法

- 意图只从查询措辞归类（商业 / 应用 / 地域 / 品牌 / 信息），不凭印象。
- 信息类词默认排除或只进展示，不进搜索核心战役。
- 否定词至少 20 条，覆盖通用信息词与无关品类，不只加竞品品牌。
- 每条广告必须对应已分析的落地页策略；未核询盘表转化追踪则不写「可上线」。
- CTA 写询盘结果（要报价 / 要样品 / 下目录），不用注册或免费试用口吻。
- 有真实项目或工厂图时不用空的库存图。
- LinkedIn 必须相对搜索 CPC 写出成本理由，否则不列为 P0。
- 学习期内不建议周中大幅改预算。

## 产出

路径：

- `deliverables/marketing/04-acquisition/paid-advertising.md`
- `deliverables/marketing/04-acquisition/paid-advertising-blueprint.xlsx`（从 `templates/paid-advertising-blueprint.xlsx` 复制后填；不能写表时改同目录 `paid-advertising-blueprint.json`）
- 按需同目录：`paid-advertising.json`

章节、表列、JSON 字段与最低行数见 `references/methodology.md`。

```markdown
# 付费广告

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 执行摘要

## 关键词研究

## 竞品广告与创意审计

## 预算情景

## 落地页建议

## 战役结构

## 创意 brief

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿四表：Campaigns（≥5 行）、Audiences（≥3 行）、Creatives（≥15 行）、Keywords（≥50 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

竞品调研无广告账户导出、CPC 或创意库；本节只借批发货架品类树与行业词当关键词结构，账户数字仍须本轮采集。

用户要「三档月预算」。每档用已采集 CPC 算 clicks → inquiries → CPI，并在 `source` 放 URL；缺 CPC 时只写缺口与「到广告平台关键词规划工具复核」，不写无来源的测试档金额。

输入把搜索战役按自造品类（arena / energy infrastructure）或内部标签开组。成稿按已核验货架分战役：Heimspeicher 与 Gewerbespeicher 不合一战役；工商业侧按货架类型（All-in-One、Container、Modular mit WR / ohne WR）或耦合（DC / AC 后装）分广告组。Container 是类型不是容量，不按容量档开组。词用行业名（Heimspeicher / Gewerbespeicher / Containerspeicher / Hybridwechselrichter 或其面客语种对译），不用自造复合词。规模错位词进否定词，不进核心搜索。

输入把学院 / Wiki / 知识世界整站词塞进搜索核心。成稿：信息类默认排除或只进展示；商业意图对齐货架类型与应用（自用、削峰、备电），不要用百科词扛询盘战役。

输入要「一套广告打安装商和 EPC」。成稿分角色与漏斗阶段，不合一条；CTA 写询盘结果（要报价 / 要样品 / 下目录），不用注册或免费试用。禁止把库存或时效承诺当卖点。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文就套通用投放结构。
- 无 CPC 来源仍输出预算数字，或把一平台 CPC 套到另一平台。
- 编造 CPC、CTR、CVR 或竞品创意原文。
- 跳过竞品创意审计，或用 Competitor A/B/C 占位。
- 把 B2C 搜索结构套到 B2B，忽视采购角色与项目型查询。
- 只收英文词，忽略目标市场本地语言检索。
- 否定词不足 20，或只加竞品品牌。
- 广告与落地页不匹配，或未核询盘转化追踪与 UTM 仍写可上线。
- 小预算均分到四个平台；多市场塞进同一战役。
- 优化点击而不是询盘提交。
- 把教学例子或无来源假设当事实。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 关键词 ≥50 且每条有 CPC 或显式缺口与 `source`；竞品创意 ≥10（含 `source_url`）；落地页 ≥5
- [ ] 恰好 3 档预算情景，均回溯已采集 CPC；否则只写缺口
- [ ] 否定词 ≥20；战役含 campaign → ad group 两级且 ≥5 个战役
- [ ] 创意 brief 覆盖 ≥3 个买家角色与四个漏斗阶段
- [ ] 主文档与工作簿在 `deliverables/marketing/04-acquisition/`；`source` 无空值
- [ ] 已写 UTM 规范与询盘表转化追踪；未核追踪不标可上线
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
