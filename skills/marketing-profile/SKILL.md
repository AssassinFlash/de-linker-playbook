---
name: marketing-profile
description: >
  Use when the user says profile, product context, product profile,
  positioning, target audience, ICP, describe my product, 产品档案,
  产品上下文, 产品定位, 目标受众, company profile, 公司档案, set
  up my product, or needs product facts confirmed before a marketing
  run. Read the fact-source entry docs/fact-sources.md and follow it to
  the live site, the new-site repo, and competitor research. Check coverage against the
  fifteen-section checklist; search only to judge coverage, never copy
  product facts into this repo, never write a second company dossier.
  Not for playbook init, phase navigation, or conversion copy.
---

# 营销档案（指路）

确认产品事实可经事实源入口读到，对照十五节清单留下一份不含事实原文的指针。只指路，不在本仓库另写公司档案。

## 步骤

1. **定位**。读事实源入口 `docs/fact-sources.md`（台账 `product_context` 即指向它）。完成：能报出三个源（线上站点、新站仓库、竞品调研）各在哪、本机能否读到。入口本身读不到则停，指针里标 `status: missing`；某个源读不到，指针里记下，该源的内容按没有处理。不编造、不另建档案。
2. **读总览**。按入口「什么问题查哪个源」先读总览：线上站点首页与产品分类、新站仓库 `AGENTS.md` 的公司与用词两节。完成：本会话能口头指出买家是谁、卖什么、上下文里没有的数字或证据；原文不拷进本仓库。
3. **缺参数再读**。数字、证书、规格、证明点若总览没有，按入口的问题表去对应的源查，冲突按入口「谁为准」。要查的多时 dispatch a subagent, else do it inline：只回报「哪个源的哪几个 URL 或文件覆盖了哪几个主题」，不把正文搬进本仓库。完成：每个缺的参数要么能指到某个源里的 URL 或文件路径，要么列入缺口主题名（〔未证实〕）。不访谈写档、不发明。
4. **覆盖核对**。按下方十五节给每个标「有」或「无」。公开信息尚未能判定时，可用 Apify 搜索或抓取指定 URL，只用于判定覆盖；搜到的事实不得写入本仓库。Apify 修复与替代取证后仍不可得则该节标无并列入缺口，不编造。已经在上下文里的不要再问用户。完成：15 行都有标记与指针；「无」只记主题名。
5. **证据闸**。按 `docs/feedback-rules.md` 第 9 节自查覆盖判断（有/无，不贴原文），至少覆盖业务概览、ICP、差异化、证据点：每个「有」都能指到某个源的 URL 或文件路径。完成：四项都能指到出处，或把缺的列入缺口主题名。不请用户判断。
6. **落盘指针** `deliverables/marketing/01-foundation/context-pointer.md`，用下方模板。完成：文件非空；只有路径、覆盖表、缺口主题名；无产品事实段落；教学支架原文零出现。事实以线上站点与新站仓库为准，不改本仓库。

## 默认

- 产品事实只从事实源入口 `docs/fact-sources.md` 进：线上站点、新站仓库、竞品调研三方，冲突按入口「谁为准」。
- 本仓库只写指针，不写第二份公司档案，不写 `data/profile-*`，不改台账里的 `product_context`（换机只改入口）。
- 缺口保持缺口。下游 skill 同样读事实源入口，不读本指针当事实源。
- 补搜只用于判定覆盖，不得把搜到的事实填进仓库。

覆盖这十五节（只打勾，不把正文抄过来）：

1. 业务概览 — 名称、产地、成立年、模式（OEM/ODM/批发）、品类、一句价值主张
2. 产品规格 — 材质或组件与变体、尺寸容量、MOQ、交期、认证、包装运输
3. 价值链 — 上游、中游直接客户、下游终端
4. 目标市场 — 主市场、扩展市场、进入渠道（以产品上下文为准）
5. ICP — 客户类型优先级、决策人/指定人/采购人、规模信号
6. 买家角色 — 3–5 个；role、行业、规模、目标、痛点、决策标准、发现渠道
7. 问题与痛点 — 核心问题、替代方案为何不够、业务代价
8. 竞争格局 — 具名直接对手及来源、替代方案、进口与本地动态
9. 差异化 — 已核实卖点、自有 vs 外协、客户选择理由
10. 异议与回应 — 常见异议、回应策略、至少两类不适合的客户
11. 客户用语 — 买家原话、行业术语、避免用词
12. 品牌语气 — 语气、沟通风格、语言规则
13. 贸易与出口 — 目标渠道、付款、运输条款、认证
14. 证据点 — 项目案例、产能、质量证据、评价、履历
15. 目标与指标 — 业务目标、关键转化动作、已知指标、增长目标

## 写法

- ICP 是客户类型；买家角色是决策人。分开打勾。
- 数字、证书、案例：上下文有才算「有」。空泛的 quality / service 不算有。
- B2B 直说，不把工厂或贸易做成 SaaS 口吻。
- 价值链三个层级都要有判定，不能只写「有客户」。

## 产出

覆盖表三列：主题、有/无、指针（路径或「未在上下文出现」）。

```markdown
# 产品上下文指针

- source: docs/fact-sources.md
- sources_opened: （打开过的 URL 或文件路径，无则 none）
- status: readable | partial | missing
- facts_copied: no
- confirmed: 是 / 否

## 覆盖

| 主题 | 有/无 | 指针 |
| --- | --- | --- |
| 业务概览 | | |
| 产品规格 | | |
| 价值链 | | |
| 目标市场 | | |
| ICP | | |
| 买家角色 | | |
| 问题与痛点 | | |
| 竞争格局 | | |
| 差异化 | | |
| 异议与回应 | | |
| 客户用语 | | |
| 品牌语气 | | |
| 贸易与出口 | | |
| 证据点 | | |
| 目标与指标 | | |

## 缺口

（只列主题名）
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是产品上下文指路，例子教指针形状不教营销内容，无对应事实源材料可借，保留通用支架。

读完后指针写 `source: docs/fact-sources.md`、`ICP：有`、`证书编号：无`，不把沿革或参数表粘进 `deliverables/`。

## 易错

- 把线上页面、新站仓库或调研的原文拷进本仓库。
- 档案缺失时现写一份公司简介顶上。
- 把 `~` 当成仓库内相对路径。
- 把补搜到的事实填进仓库；补搜只判定覆盖。
- 问用户「用几句话描述业务」然后开写档案；纠正以线上站点与新站仓库为准。
- 把 ICP 和买家角色写成同一段，下游文案打不准决策人。
- 缺数时填价格、产能或交期。
- 把证据库、定位表或十五节正文写进本仓库，造成第二真相源。
- 没过证据闸（「有」指不到出处）就进内容或广告。

## 清单

- [ ] 已按事实源入口读过三方（入口读不到则标 missing 并停止）
- [ ] 本会话能指出买家、所卖、缺口，且未把原文写入本仓库
- [ ] 15 主题均已标有/无；缺口只列主题名
- [ ] 业务概览、ICP、差异化、证据点四项的覆盖判断都已过证据闸
- [ ] 文件在 `deliverables/marketing/01-foundation/context-pointer.md`
- [ ] 例子原文未进入交付物
