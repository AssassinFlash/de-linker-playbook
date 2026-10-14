---
name: marketing-profile
description: >
  Use when the user says profile, product context, product profile,
  positioning, target audience, ICP, describe my product, 产品档案,
  产品上下文, 产品定位, 目标受众, company profile, 公司档案, set
  up my product, or needs product facts confirmed before a marketing
  run. Read the ledger product_context path (default
  ~/Documents/New/CONTEXT.md); if a number, cert, or spec is missing,
  read fact-base/ under that same tree. Check coverage against the
  fifteen-section checklist; search only to judge coverage, never copy
  product facts into this repo, never write a second company dossier.
  Not for playbook init, phase navigation, or conversion copy.
---

# 营销档案（指路）

确认产品事实可从台账路径读到，对照十五节清单留下一份不含事实原文的指针。只指路，不在本仓库另写公司档案。

## 步骤

1. **定位**。读 `state/marketing-status.md` 的 `product_context`；缺省为 `~/Documents/New/CONTEXT.md`。读时把 `~` 展开为用户主目录，不要把 `~` 当相对路径。完成：能报出将读的绝对路径；文件不存在或不可读则停，指针里标 `status: missing`，不编造、不另建档案。
2. **读总览**。读该 `CONTEXT.md`。完成：本会话能口头指出买家是谁、卖什么、上下文里没有的数字或证据；原文不拷进本仓库。
3. **缺参数再读**。数字、证书、规格、证明点若总览没有，再读 `~/Documents/New/fact-base/`。文件多时 dispatch a subagent, else do it inline：只回报「哪几个文件覆盖了哪几个主题」，不把正文搬进本仓库。完成：每个缺的参数要么能指到 fact-base 里的文件名，要么列入缺口主题名。不访谈写档、不发明。
4. **覆盖核对**。按下方十五节给每个标「有」或「无」。公开信息尚未能判定时，可用网页搜索或抓取指定 URL，只用于判定覆盖；搜到的事实不得写入本仓库。搜索不可用则该节标无并列入缺口，不编造。已经在上下文里的不要再问用户。完成：15 行都有标记与指针；「无」只记主题名。
5. **确认**。把覆盖判断（有/无，不贴原文）交给用户过一眼，至少覆盖业务概览、ICP、差异化、证据点。完成：用户确认或列出要改的节。
6. **落盘指针** `deliverables/marketing/01-foundation/context-pointer.md`，用下方模板。完成：文件非空；只有路径、覆盖表、缺口主题名；无产品事实段落；教学支架原文零出现。用户若要改事实，改 `~/Documents/New`，不改本仓库。

## 默认

- 产品事实只存在 `~/Documents/New`（先 `CONTEXT.md`，需要参数再 `fact-base/`）。
- 本仓库只写指针，不写第二份公司档案，不写 `data/profile-*`，不改台账里的 `product_context` 路径（交接他机由人改）。
- 缺口保持缺口。下游 skill 同样读台账路径，不读本指针当事实源。
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

- source: （台账 product_context 路径，不粘贴原文）
- fact_base_opened: （相对 ~/Documents/New/ 的文件名，无则 none）
- status: readable | missing
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

本 skill 是产品上下文指路，例子教指针形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

读完后指针写 `source: ~/Documents/New/CONTEXT.md`、`ICP：有`、`证书编号：无`，不把沿革或参数表粘进 `deliverables/`。

## 易错

- 把 `CONTEXT.md` 或 fact-base 原文拷进本仓库。
- 档案缺失时现写一份公司简介顶上。
- 把 `~` 当成仓库内相对路径。
- 把补搜到的事实填进仓库；补搜只判定覆盖。
- 问用户「用几句话描述业务」然后开写档案；纠正应改 `~/Documents/New`。
- 把 ICP 和买家角色写成同一段，下游文案打不准决策人。
- 缺数时填价格、产能或交期。
- 把证据库、定位表或十五节正文写进本仓库，造成第二真相源。
- 跳过用户确认，直接进内容或广告。

## 清单

- [ ] 已按台账路径读过（或标 missing 并停止）
- [ ] 本会话能指出买家、所卖、缺口，且未把原文写入本仓库
- [ ] 15 主题均已标有/无；缺口只列主题名
- [ ] 用户已确认业务概览、ICP、差异化、证据点四项覆盖
- [ ] 文件在 `deliverables/marketing/01-foundation/context-pointer.md`
- [ ] 例子原文未进入交付物
