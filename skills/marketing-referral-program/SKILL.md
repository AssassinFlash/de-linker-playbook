---
name: marketing-referral-program
description: >
  Use when the user asks for referral program, partner program, agent
  recruitment, distributor incentives, commission structure, B2B channel
  partners, trade referrals, word of mouth manufacturing, 转介绍计划,
  合作伙伴计划, 代理招募, 分销激励, or 佣金结构. Research B2B incentive
  and agent-commission benchmarks, then write a sourced referral and
  partner program with implementation plan, agreement outline, outreach
  templates, and tracking log under deliverables/marketing/06-growth/.
  Read the ledger product_context first; invent no commission rates,
  competitor partner pages, or order values. Never paste skill examples
  into the output. Not for SaaS viral loops, paid ads, or phase
  navigation.
---

# 推荐与合作伙伴计划

根据已读产品上下文与可核验公开来源，设计 B2B 外贸推荐与代理计划（角色、佣金、归因、激活、赋能），落到 `deliverables/marketing/06-growth/`。不做 SaaS 裂变链接或付费投放。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具能力化四条。
2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。上游若存在则读 `deliverables/marketing/01-foundation/` 的定位与定价。用户本轮给出的历史订单/CRM、现行伙伴协议、口头佣金一并列入。完成：能指出品类、目标市场、买家角色、毛利与折扣权限各依据哪几条；原文不拷进本仓库。毛利缺到无法调和佣金则停并写缺口，不编造费率、订单额或竞品伙伴页。
3. **采集**。用网页搜索查证 B2B 推荐/代理结构、佣金基准、协议惯例；需要原文时抓取指定 URL 的正文（至少 2 个竞品伙伴/代理页，以及搜到的公开佣金表或 FAQ）。默认一条能力，不并列多引擎。搜索不可用则停止并写缺口。多站点并行时 dispatch a subagent, else do it inline。查询意图、最低条数与校验见 `references/methodology.md`。完成：每条证据有 URL、摘录、访问日期；结构、外贸案例、四类推荐人基准、竞品页达到最低条数，或已把未达标项写入缺口。
4. **分析**。只从已采集证据与已读毛利推导推荐人矩阵、偶发推荐人 vs 当地代理、佣金阶梯、归因规则、激活序列与赋能包。量表、起点费率与表列见 `references/methodology.md`。完成：四类推荐人各有 reward model 与 formality；每条费率有 `source` 或标明「行业参考值，需按产品上下文毛利调整」；佣金与毛利可调和或已写缺口；归因写清 first verified introduction wins。
5. **落盘**。写入下方路径。完成：主文档与工作簿非空；表每行 `source` 非空；协议大纲含 territory、rate、payment terms、exclusivity、termination；面客稿无未替换占位符；教学支架原文零出现；文末 5–10 条可验证断言。

## 默认

- 策略与分析用简体中文；URL、字段名、协议条款名、文件名用英文。面客 outreach 与协议跟产品上下文的面客语种，同一段不混用。
- 目标渠道以产品上下文为准，不预设某一电商、社交或即时通讯平台。未列出的频道记缺口，不编造互动或转介绍量。
- B2B 外贸推荐多是关系与线下介绍，不默认推荐链接、病毒循环或专用推荐软件。跟踪须能在邮件、即时通讯记录、表格或 CRM 备注里完成。
- 佣金在被推荐客户回款后按整单计提，不按发货、不按分期。同一终端客户的复购不计佣，除非代理主动再次促成。
- 数字、佣金率、订单额只写观察到的值或已标注的行业参考值；没有就写「公开源未找到」，禁止估计后写成事实。
- 缺来源或搜索不可用：停止并写缺口，不编造。

## 写法

- 推荐人类型从产品上下文取；上下文没有则在指定人/设计师、承包/施工、经销/代理、既有客户里选最贴近的一档，并标明「角色未在上下文出现，暂用」。
- 费率必须能对照已读毛利与折扣权限；对不齐则下调或写缺口，禁止亏损推荐。
- 协议必须写明 territory、commission rate、payment schedule、exclusivity、termination，禁止只写「合作共赢」。
- 赋能包列出具体物料与成本约束（目录、样品政策、报价指引），不把做不到的印刷件或样品海运标成 P0。
- `source` 写具体 URL 或「行业参考值」加调整说明，不写空的工具名。
- 外展按产品上下文的目标渠道写；即时通讯是否写入以目标市场为准，不默认只走邮件。

## 产出

路径：

- `deliverables/marketing/06-growth/referral-program.md`
- `deliverables/marketing/06-growth/referral-program-design.xlsx`（从 `templates/referral-program-design.xlsx` 复制后填；不能写表时改同目录 `referral-program-design.json`）
- 按需同目录：`referral-program-design.md`、`partner-outreach-templates.md`、`partner-agreement-template.md`、`referral-tracking-guide.md`

章节与表列、最低行数见 `references/methodology.md`。

```markdown
# 推荐与合作伙伴计划

- source: 台账 product_context（不粘贴原文）
- accessed:
- collected:

## 计划目标

## 推荐人类型优先级

## 佣金结构

## 激活序列

## 跟踪与归因

## 伙伴赋能

## 首批名单框架

## 行动清单（P0 / P1 / P2）

## 缺口

## 可验证断言
```

工作簿三表：Program Design（≥4 行）、Implementation Plan（≥5 行）、Referral Log Template（表头 10 列）。每行 `source` 非空。禁止只交空模板。

## 例子

> 仅供理解，禁止引用到输出。

用户要「厂家也直销大 EPC，分销介绍过来的安装商算谁的客户」。写成：推荐人从产品上下文取（指定人/施工、既有安装商或 EPC 介绍同行）；归属用 first verified introduction wins；协议写明 territory、exclusivity、termination（解约后能否再接触被介绍账户）。本层是分销层时不把分销商写成客户受众，也不写成厂家招募经销商。不写无来源的「行业惯例一律 5%」。

用户要「用配额优先当伙伴激励，少发现金佣金」。写成：现金部分仍回款后按整单计提、每条费率有 source 或行业参考值并对照毛利；配额/供货排序只作为渠道关系形状写入待核条款或缺口，不当库存或时效承诺。不编造配额表或竞品伙伴页。

用户要「指定人和施工方都说这个工地是自己介绍的」。写成：同一终端客户只认先核实的介绍；复购不计佣，除非代理主动再次促成。不把转介绍写成整户换商（首单更像备线开口）。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文或毛利就套通用佣金表。
- 把 SaaS 推荐链接、病毒循环或自动看板套到外贸场景。
- 编造佣金基准、竞品伙伴 URL 或订单额。
- 协议不写 territory、付款节点、排他与终止。
- 忽略样品包、印刷目录和物流成本，赋能包无法执行。
- 复购自动计佣，未约定须代理主动再次促成。
- `source` 只写搜索、不附 URL 或参考值说明。
- 面客稿未按角色分写，或留下未替换占位符。
- 只交 Markdown、工作簿仍是空模板。

## 清单

- [ ] 已读共用规则与 `product_context`，原文未拷进本仓库
- [ ] 结构 ≥5、外贸案例 ≥3、四类推荐人各有基准、竞品伙伴页 ≥2，或已写缺口
- [ ] 每条佣金率有 `source` 或行业参考值标注；与毛利可调和
- [ ] 归因规则已写入文档与工作簿（first verified introduction wins）
- [ ] 激活序列含 timing、action、owner、deliverable；赋能包有具体物料
- [ ] 协议大纲五条款齐全；outreach 覆盖四类角色或已映射并标明暂用
- [ ] 主文档与工作簿在 `deliverables/marketing/06-growth/`；`source` 无空值
- [ ] 文末 5–10 条可验证断言；教学例子原文未进入交付物
