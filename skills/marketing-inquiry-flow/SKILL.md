---
name: marketing-inquiry-flow
description: >
  Use when the user asks for inquiry flow, RFQ process, quote request, lead
  qualification, inquiry abandonment, sample request conversion, WhatsApp
  inquiry handling, first-response SLA, 询盘流程, 报价流程, 询盘转化,
  首次回复, 样品转化, or 外贸获客流程. Audit the inquiry-to-quote path from
  submit through qualification, first response, and sample conversion; crawl
  the live site and competitor quote pages; write a sourced flow plan under
  deliverables/marketing/05-cro/. Read the ledger product_context first;
  invent no conversion rates, response times, or competitor URLs. Never paste
  skill examples into the output. Not for page layout or field redesign,
  paid-media plans, or phase navigation.
---

# 询盘流程

根据已读产品上下文与可抓取页面，审计从提交后到首次回复、资质判定与样品转化的询盘路径，写出可执行的摩擦修复与回复框架，落到 `deliverables/marketing/05-cro/`。页面字段与布局以 `marketing-landing-page` 为准，本 skill 不改页面。不定稿整页落地页，不做付费投放。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。读台账 `state/marketing-status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读同目录 `fact-base/`。上游若存在则读 `deliverables/marketing/01-foundation/`（定位、定价、样品政策）与 `deliverables/marketing/05-cro/landing-page.md`。页面字段与布局以 `marketing-landing-page` 为准，本 skill 不改页面。列出品类、买家角色、目标市场、贸易条款、MOQ/样品政策、询盘量、首次回复时长、询盘到报价/样品/订单比率、主要流失阶段、团队工时与语种、已用渠道与 CRM。完成：能指出各依据哪几条；原文不拷进本仓库。用户只给站点 URL 时先抓该站再补上下文；品类或市场仍不明则停并写缺口，不编造公司、转化率或竞品事实。
3. **采集**。用网页搜索查证询盘优化与回复时效基准；需要原文时抓取指定 URL 的正文（本站首页、产品页、询盘页、下单流程页；≥4 个竞品询盘/报价入口）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多页并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；本站四页与竞品入口达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据映射漏斗、摩擦、竞品对照、资质评分、分角色首次回复、样品桥接与 KPI。量表、漏斗与表列见 `references/methodology.md`。完成：每个 P0 摩擦能指到已抓取页面；评分七维与四档处理规则已写出；样品触发时机与至少 3 个跟进节点已定义。
5. **落盘**。写入下方路径。已有 `inquiry-flow.md` 则增量更新并在文首保留版本说明。完成：主文档与工作簿非空；表每行 `source` 非空且含 URL；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；面客回复、按钮、URL、字段名、文件名跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商或社交平台。上下文未列的频道记缺口，不编造询盘量或回复时长。
- 首次回复的方法默认目标：工作时间内 2 小时。行业数字一律标「行业参考值，实际以你的数据为准」。
- 跨阶段优先级打开 `marketing-funnel-optimization`；本文件停在提交后到样品。
- 数字、转化率、回复时长只写观察到的值或用户本轮提供的值；没有就写「公开源未找到」或「用户数据未知」，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 这是制造/外贸询盘（询盘、报价、样品），不套用试用开通或套餐升级话术。
- 页面字段与布局以 `marketing-landing-page` 为准，本 skill 不改页面。发现字段问题记缺口并指向已批准 `landing-page.md`，不写空的「简化表单」。
- 即时通讯入口是否启用、放在哪些产品页，以目标市场与产品上下文已出现频道为准。
- 角色从产品上下文取；上下文没有则在采购、承包、指定人、经销、质量/合规里选最贴近的一档，并标明「角色未在上下文出现，暂用」。不要用 C 端消费者口吻，也不对所有角色用同一封回复。
- 样品政策必须写触发时机、价格或运费规则、交期；禁止只写「欢迎索样」。
- `source` 写具体 URL，不写空的能力名。
- 终稿不留未替换的 `{{...}}` 占位；品类、市场、产地只引用产品上下文对应字段。

## 产出

路径：

- `deliverables/marketing/05-cro/inquiry-flow.md`
- `deliverables/marketing/05-cro/inquiry-flow-optimization.xlsx`（从 `templates/inquiry-flow-optimization.xlsx` 复制后填；不能写表时改同目录 `inquiry-flow-data.json`）
- 按需同目录：`inquiry-flow-spec.md`、`touchpoint-copy.md`、`multi-channel-setup.md`、`response-templates.md`、`friction-audit.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 询盘流程

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 询盘流程现状评估

## 竞品询盘入口对比

## 摩擦点优先级排序

## 渠道覆盖优化方案

## 首次回复框架

## 询盘资质评分系统

## 样品转化桥接

## KPI 追踪计划

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿：保留模板自带的 Steps、Forms 并填满；另补 Funnel Analysis（≥7 行）、Flow Improvements（≥10 行）、Competitor Benchmark（≥4 行）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「优化询盘表单」。输入写「必填从 11 项减到 6 项」。成稿应改成：先抓本站询盘页与 ≥4 个竞品入口，用对照表记下门的形状（公开目录+隐价登录 / 价格位换成询价按钮 / 宣传站无目录、销售回访后才发门户），再按删/留/改列出本站字段——留公司、税号（页上写清用途）、角色或业态下拉（表单兼做分群）、贸易证明上传；卸货条件、会计联系人不堆进首触，除非本站已在收。输入写「让访客马上看到净价」。成稿应改成：页上回答「为什么看不到价」——净价在审核开通后可见，不承诺即时见价；审批时长只写本站已声明的或「未声明」。竞品把门做成询价按钮，不等于本站也该询价，跟产品上下文商务规则。工作时间内 2 小时首次回复并问 1–2 个规格问题；样品触发另写。不把批发门户利益清单抄成询盘 CTA，不写无来源的「转化率提升 30%」，不把竞品原句或论坛等待时长当 SLA，也不把本节句子粘进交付物。

## 易错

- 没读产品上下文、也没抓本站询盘页，就套通用 CRO 清单。
- 用 Competitor A/B/C 占位，或不记录必填字段数与 CTA 原文。
- 编造转化率、回复时长或竞品 URL。
- 建议「简化表单」却改页面字段；页面字段与布局以 `marketing-landing-page` 为准。
- 所有买家用同一封首次回复。
- 跳过样品桥接。
- `source` 只写搜索、不附 URL。
- 把试用、套餐、激活等 SaaS 话术写进外贸询盘。
- 行业基准未标「行业参考值，实际以你的数据为准」。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 本站首页、产品页、询盘页已抓取；现状评估引用 ≥3 个不同页面 URL
- [ ] ≥4 个竞品询盘入口：必填字段数、CTA 原文、回复承诺（或「未声明」）
- [ ] 七维评分与 Hot / Warm / Cool / Low 处理规则已写出
- [ ] 首次回复覆盖上下文角色（不足则暂用默认方向）且 ≥3 个已出现渠道
- [ ] 样品触发时机、政策、≥3 个跟进节点已定义
- [ ] 主文档与工作簿在 `deliverables/marketing/05-cro/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
