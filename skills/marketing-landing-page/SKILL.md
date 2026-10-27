---
name: marketing-landing-page
description: >
  Use when the user asks for landing page, homepage CTA, inquiry form, popup,
  page audit, form redesign, 着陆页, 落地页, 询盘表单, 弹窗, 页面审计, or
  表单改版. Audit live homepage, product, and inquiry pages against competitor
  CTAs, forms, and trust signals; write a sourced page audit, form redesign,
  popup plan, and experiment queue under deliverables/marketing/05-cro/. Read
  the ledger product_context first; invent no conversion rates, field counts,
  or competitor URLs. Never paste skill examples into the output. Not for
  post-submit reply scripts, launch/referral/retention playbooks, paid-media
  plans, technical site rebuilds, or phase navigation.
---

# 着陆页

根据已读产品上下文与可抓取页面，审计首页、产品页与询盘页的主张、CTA、表单与信任信号，写出可执行的改写与实验队列，落到 `deliverables/marketing/05-cro/`。不定稿付费投放，不做整站技术重构。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若存在则读 `deliverables/marketing/01-foundation/` 与 `deliverables/marketing/02-seo/seo-audit.md`。列出品类、目标市场、买家角色、流量来源、询盘渠道、建站平台约束、漏斗已知转化率。完成：能指出各依据哪几条；原文不拷进本仓库。用户只给站点 URL 时先抓该站再补上下文；品类或市场仍不明则停并写缺口，不编造公司、转化率或竞品事实。
3. **范围**。本 skill 主责页面级转化：着陆页审计、CTA、表单字段、弹窗、实验队列。提交后询盘运营走 `marketing-inquiry-flow`；跨阶段合成走 `marketing-funnel-optimization`。用户只要询盘整条路径则打开 `skills/marketing-inquiry-flow/SKILL.md`；只要全链路优先级则打开 `skills/marketing-funnel-optimization/SKILL.md`；只要上市事件则打开 `skills/marketing-launch-strategy/SKILL.md`；只要转介绍或留存则打开对应方法 skill。需要隔离时 dispatch a subagent, else do it inline。完成：主责与他 skill 边界各写一句，不在本工作簿加上市/转介绍/留存表。
4. **采集**。用 Apify 搜索查证 B2B 着陆页与询盘表做法；需要原文时抓取指定 URL 的正文（本站首页、产品/服务页、询盘页、下单流程页；≥3 个竞品首页+产品页+询盘页）。默认一条能力，不并列多引擎。Apify 修复与替代取证后仍不可得则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；本站三页与竞品对照达到最低条数，或已把未达标项写入缺口。
5. **分析**。只从已采集证据给页面 1–5 分、表单字段对照、弹窗规格、实验假设。量表、漏斗与表列见 `references/methodology.md`。完成：每个 P0 能指到已抓取页面；P0 文案有 before → after；行业数字已标「行业参考值，实际以你的数据为准」。
6. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客标题、按钮、URL、字段名、文件名跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造询盘量或转化率。
- 这是制造/外贸询盘（询盘、报价、样品），不套用试用开通、加入购物车或限时秒杀。
- 数字、转化率、字段数、响应时长只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」。行业数字一律标「行业参考值，实际以你的数据为准」。
- 缺来源或Apify 修复与替代取证后仍不可得：停止并写缺口，不编造。

## 写法

- 先抓再改。没有已抓取正文，不写页面建议。
- 建站平台、主题、表单插件限制必须约束建议；上下文未写明则记缺口，不假设某一建站产品。
- 询盘表桌面 5–7 字段、移动端压到约 3–4 个；按钮写行动加结果，不用空的 Submit。
- 即时通讯入口是否启用、放在哪些页，以目标市场与产品上下文已出现频道为准。
- 角色从产品上下文取；上下文没有则在采购、承包、指定人、经销、质量/合规里选最贴近的一档，并标明「角色未在上下文出现，暂用」。
- `source` 写具体 URL，不写空的能力名。终稿不留未替换的占位符。
- 佣金或加售建议必须能对上产品上下文的毛利结构；对不上则记缺口，不写比例。

## 产出

路径：

- `deliverables/marketing/05-cro/landing-page.md`
- `deliverables/marketing/05-cro/cro-experiment-queue.xlsx`（从 `templates/cro-experiment-queue.xlsx` 复制后填；不能写表时改同目录 `cro-experiment-queue.json`）
- 按需同目录：`page-audit-findings.md`、`copy-rewrites.md`、`form-field-spec.md`、`popup-designs.md`、`ab-test-plan.md`

章节与表列、最低行数见 `references/methodology.md`。询盘规格、回复模板、跨阶段优先级、上市时间线、转介绍设计、留存手册不在本 skill 落盘。

```markdown
# 着陆页

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 现状审计

## 竞品 Benchmark

## 着陆页优化方案

## 表单与询盘入口方案

## 弹窗与 Lead Capture 方案

## KPI 追踪计划

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿五表：Experiments（≥10 行）、Results（测试后填，可为 0 行）、Page Audit（≥5 行）、Form Redesign（≥8 行）、Popup Plan（≥6 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

形状借自光伏批发站公开页：店内一体（目录可逛、净价登录后可见）对宣传站+门户、一次注册墙、以及「看不见净价 / 注册等待」这类转化阻碍；语气对照目录批发交货后沉默 vs 工程 BOM、配对核验、调试与厂家质保协调。竞品原句、型号参数、价格、库存时效承诺、证言人名不进本段。

用户要「优化着陆页 CTA」。输入写：加强首屏号召。→ 成稿应改成：已抓首页首屏标题与按钮原文，P0 用「当前线上 | 建议替换」对照写 before → after，URL 写入 `source`；按钮写行动加结果（申请贸易价 / 提交项目拿 BOM），标题能回溯到工程伙伴而非卖完箱子就沉默。不是无来源的「转化率提升 30%」，不是 one-stop shop / skip the middleman / we are your bridge，也不把本节句子粘进交付物。

用户要「对标竞品首页」。输入写：照抄超级菜单和立即购买。→ 成稿应改成：先记两类结构再选——店内一体（品类×品牌、规格公开、套餐作独立类目）或宣传站零货架、交易全在门户；按已抓本站选型并写缺口。目录浅时不仿全市场超级菜单。不是抄竞品按钮原文，不是用规模数字撑首屏。

用户要「价格隐藏，弹窗逼注册」。输入写：进站即弹十二项注册。→ 成稿应改成：卡旁回答「为何无净价」（贸易价仅对核验账户开放，核验一次不是每单人工）；注册利益只写结构项（净价、登录后可用性状态、订单门户、货号再订、技术工单），不写开通秒数；弹窗有频率上限，研究页不打断。不是把证件与物流能力问塞进首屏。

用户要「首页通吃业主和安装商」。输入写：一个立即询价打所有人。→ 成稿应改成：贸易入口与业主分流，业主去找安装商、不进批发结账；角色从产品上下文取，没有则标明暂用。不是 C 端秒杀或试用开通。

用户要「加信任区块」。输入写：客户证言加几天发货。→ 成稿应改成：用已抓页可核验信号（配对核验、工程 BOM、调试/厂家质保协调）；案例形状是指标+范围+边界。不是证言人名，不是库存数量或到达天数当卖点，不是制造商 / 备件库 / 自有质保承保。

用户要「着陆页 FAQ 撑字数」。输入写：科普储能、劝升档。→ 成稿应改成：只拆下单前已有阻碍（看不见净价、账户要什么材料、套餐有没有独立入口）。不是种下新疑虑，也不是把询盘整条路径或上市表写进本工作簿。

## 易错

- 没读产品上下文、也没抓本站页面，就套通用 CRO 清单。
- 只审首页，跳过产品页和询盘页。
- 用 Competitor A/B/C 占位，或不记录必填字段数与 CTA 原文。
- 编造转化率、字段数或竞品 URL。
- 建议「优化 CTA」却不给 before → after。
- 表单字段只增不减，或移动端仍超过约 4 项必填。
- 弹窗无频率上限、无退出意图，对采购研究页无差别打断。
- 把试用、购物车、秒杀等 C 端话术写进外贸询盘页。
- 行业基准未标「行业参考值，实际以你的数据为准」。
- 在本工作簿加上市、转介绍或留存表。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 本站首页、产品/服务页、询盘页已抓取且可访问
- [ ] ≥3 个竞品页：CTA、信任信号、表单结构均有来源 URL
- [ ] ≥2 个竞品询盘表：字段数、必填、CTA 原文已摘录
- [ ] 每个 P0 有 before → after 并引用已抓取页
- [ ] Experiments ≥10 行、Page Audit ≥5、Form Redesign ≥8、Popup Plan ≥6；每行 `source` 非空
- [ ] 行业数字已标「行业参考值，实际以你的数据为准」
- [ ] 主文档与工作簿在 `deliverables/marketing/05-cro/`；无上市/转介绍/留存表
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
