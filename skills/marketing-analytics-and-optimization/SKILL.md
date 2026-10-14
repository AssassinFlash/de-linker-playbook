---
name: marketing-analytics-and-optimization
description: >
  Use when the user asks for analytics setup, GA4/GTM tracking, conversion
  tracking, event taxonomy, inquiry attribution, A/B testing plans,
  low-traffic testing, CRM pipeline, lead scoring, sales operations,
  RevOps, measurement framework, 数据追踪, 实验框架, 收入运营, 询盘归因,
  or 测量策略. Audit site forms and tags, define events and UTM rules,
  prioritize low-traffic-safe experiments, and write a sourced measurement
  system under deliverables/marketing/07-measurement/. Read the ledger
  product_context first; invent no traffic, conversion values, or pipeline
  rates. Never paste skill examples into the output. Not for standalone ad
  plans, landing-page rewrites without measurement, or phase navigation.
---

# 分析与优化

根据已读产品上下文与可验证公开来源，审计站点表单与现有追踪，定义事件分级、UTM 与销售管道，排出低流量可执行的实验队列，落到 `deliverables/marketing/07-measurement/`。不写独立投放计划，不定稿整页落地页。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/marketing-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/02-seo/site-and-schema.md`、`deliverables/marketing/04-acquisition/`、`deliverables/marketing/05-cro/`。列出站点 URL、表单、GA4/GTM 状态、已用渠道、月访问量、询盘/样品基线、销售工具、团队规模、销售周期、卡点阶段。完成：能指出品类、目标市场、转化目标、追踪现状各依据哪几条；原文不拷进本仓库。品类、站点或渠道缺到无法圈定测量面则停并写缺口，不编造公司、流量、转化价值或管道比率。
3. **采集**。用网页搜索查证 GA4/GTM 事件模式、低流量实验方法与询盘管道基准；需要原文时抓取指定 URL 的正文（首页、询盘/联系表、高意向资产页，查现有标签与提交触发）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；表单清单与渠道名单达到最低项，或已把未达标项写入缺口。
4. **分析**。只从已采集证据推导事件分级、UTM/渠道规则、漏斗阶段、线索评分、实验优先级与 CRM 选型。量表、分档与表列见 `references/methodology.md`。完成：每个事件能映射到本站已确认的页面元素或用户动作；UTM 只覆盖已确认在用的渠道；实验方法与已观测（或显式未知的）月访问量分档一致。
5. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空；转化价值与管道目标无观测值时标明待填，不写成事实；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；事件名、UTM、字段名、文件名用英文。面客短句跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道不写 UTM、不编造流量。
- 数字、访问量、转化率、客单价只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」，禁止估计后写成事实。无观测的转化价值、管道目标、评分阈值用 `[YOUR_VALUE]` / `[YOUR_TARGET]` 标明待填。
- 主转化等价于询盘提交（`inquiry_form_submitted`），不是零售下单，除非产品上下文确认站点有直销成交。
- 低流量优先定性与贝叶斯、90% 置信、最少 4 周、50/50 分流；月访问量未知则先按定性档，不承诺统计功效。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 事件名用 `object_action`、小写加下划线；参数不含 PII。
- 每个事件必须能指到本站已确认的元素或动作，禁止为未使用渠道或未上线页面造事件。
- 假设句用 Because → believe → will cause → for → We'll know；每条实验写 primary / secondary / guardrail。
- ICE 在低流量站加重 Ease；高影响但需数月才出结果的实验不标 P0。
- CRM 建议匹配团队规模与月询盘量，不把企业套件推荐给 1–5 人团队。
- `source` 写具体 URL 或用户本轮给出的账户/导出，不写空的能力名。
- 终稿不留未替换的 `{{...}}` 占位；品类、市场、展会名只引用产品上下文对应字段。

## 产出

路径：

- `deliverables/marketing/07-measurement/analytics-and-optimization.md`
- `deliverables/marketing/07-measurement/analytics-and-optimization.xlsx`（从 `templates/analytics-and-optimization.xlsx` 复制后填；不能写表时改同目录 `analytics-and-optimization.json`）
- 按需同目录：`event-taxonomy.md`、`utm-parameter-system.md`、`tag-manager-config.md`、`test-queue.md`、`test-specs.md`、`pipeline-stages.md`、`lead-scoring-model.md`、`crm-setup-guide.md`、`dashboard-specs.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 分析与优化

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 现状审查结论

## 事件分级方案

## UTM 参数体系

## GA4 配置清单

## GTM 配置清单

## A/B 测试优先级队列

## 统计方案

## RevOps 管道定义

## 线索评分与路由规则

## 指标看板规格

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿五表：Event Taxonomy（≥15 行）、Experiment Queue（≥8 行）、Pipeline Stages（≥8 行）、Lead Scoring（≥12 行）、KPIs（≥10 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「低流量站也能测」。输入写「买家看不见净价」。成稿应改成：先抓本站产品卡与注册入口，记下价格门形状（公开目录、净价位换成登录或询价 / 宣传站无货架、交易全在门户）。只为已确认元素写事件；没有价格位或注册表就写缺口，不从竞品店补事件。主转化仍是询盘提交，不是零售购买。月访问量按已观测分档选定性或贝叶斯，假设用 Because → believe → will cause → for → We'll know；`source` 放已抓页面 URL。无观测流量或转化价值标待填。不要把本节句子粘进交付物。

输入写「注册转化率要上去」。成稿应改成：把注册当一次资格门来测（申请提交、审核开通、开通后回访），不是即时开通也不是购物车成交；审批时长只写本站已声明的或「未声明」。UTM 只覆盖已确认在用渠道。

## 易错

- 没读产品上下文就套通用埋点清单。
- 为未使用渠道写 UTM，或为未确认页面元素写事件。
- 编造月访问量、转化价值、管道转化率或行业询盘率后写成事实。
- 低流量站做 3+ 变体或 95% 置信的短测，并承诺统计显著。
- 数据好看就提前停测；或在假期、展会周开测。
- 把所有询盘同等处理，跳过资质评分。
- 阶段定义尚未手工跑通就上自动化。
- 只追踪单一市场渠道询盘，看不到全渠道来源。
- 未确认有无直销成交就关掉电商追踪。
- `source` 只写搜索、不附 URL。
- 把教学例子或无来源假设当事实。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 表单、渠道、GA4/GTM 状态已确认或已写缺口；每个事件映射到本站元素
- [ ] UTM 只覆盖已确认在用渠道；转化价值无观测则标待填
- [ ] 实验方法与月访问量分档一致；每条假设含 ICE、样本量、≥4 周、三层指标
- [ ] 管道覆盖 New Inquiry 到 Closed Lost（含交付后跟进）；每阶段有进出条件与负责人
- [ ] 主文档与工作簿在 `deliverables/marketing/07-measurement/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
