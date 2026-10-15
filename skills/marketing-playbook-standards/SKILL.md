---
name: marketing-playbook-standards
description: >
  Use when applying shared playbook rules, quality gates, 共用规则, 质量标准,
  数据锚定, citation rules, 引用规则, 营销策略, 调研, 文案, 创意, 评审, or 编排,
  or when acting as a marketing strategist, researcher, copywriter, reviewer,
  or orchestrator. Open this file as step 0 of a method skill by relative
  path; do not inject it at session-start. Anchor every claim to a real
  source, never paste skill examples into deliverables, write output only
  under deliverables/, and name tools as capabilities. Stop and record a
  gap when search is unavailable. Not for running a campaign phase, drafting
  copy, SEO audits, or navigating the ledger.
---

# 营销共用规则

所有营销方法 skill 动手前先读本文件。五条硬约束：数据锚定、证据闸、例子禁引用、产出只进 `deliverables/`、工具写能力。不注入会话开头，不锁产品。

## 步骤

1. **入口**。方法 skill 的步骤 0：读 `skills/marketing-playbook-standards/SKILL.md`。本文件被单独点开时，把下列规则应用到用户本轮任务。完成：能复述五条硬约束。禁止 session-start 预加载，禁止用 frontmatter 把本文件注入子代理。
2. **产品上下文**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。完成：能指出受众与约束各依据哪几条陈述。原文不拷进本仓库。文件不存在则停并写缺口，不另写公司档案。
3. **执行当前方法**。打开台账或用户点名的方法 skill，按其步骤做。需要隔离时 dispatch a subagent, else do it inline。完成：战役产出在 `deliverables/marketing/` 或 `deliverables/lead/` 下对应阶段小写目录；teach/eval 元产出在 `deliverables/marketing/00-system/`。简单任务不派子代理。
4. **出门检查（证据闸）**。对照下方清单与 `docs/feedback-rules.md` 第 9 节。完成：每条对外声明有来源或已标明缺口；教学例子原文零出现；过了的交付物 frontmatter 写 `status: approved` 与 `evidence_gate: <日期>`。

## 默认

**数据锚定**

- 数字、趋势、竞品判断必须能回溯到：产品上下文、用户本轮提供、网页搜索查证结果、或已抓取 URL 的正文。交付物写来源与访问日期。
- 引用的 URL：已抓取则记下摘录；未抓取则标明「未验证」及原因。
- 禁止：把模型记忆当来源、无出处的「普遍认为」、编造的地址或统计。
- 缺数据：写明缺口，不编造。搜索不可用则停止并写缺口。

**证据闸**

- 执行前的质量关由 AI 自查，清单是 `docs/feedback-rules.md` 第 9 节：引用的底表数据写明哪张表、哪个网址或登记编号、哪天、什么状态；阻断类网页动作先看过线上现状；要上线的每条产品或公司说法能追到事实源入口所指的三方之一；查不到的标〔未证实〕，不写成事实也不进对外文字；没用第 8 节列为不采用的数字；例子原文没进交付物。
- 过了才写 `status: approved`（意思就是「已过证据闸」）和 `evidence_gate: <日期>`。不请操作者审「写得好不好」；操作者只决定发不发、上不上。执行后的质量看反馈闸（底表 L1–L3）。

**例子禁引用**

- skill 内例子是教学支架。标注句固定为「仅供理解，禁止引用到输出。」交付物不得等于任何已标注例子原文。

**产出根**

- 只写 `deliverables/`。营销阶段目录小写（`00-research` … `07-measurement`）；获客写 `deliverables/lead/`。禁止把产出写到本仓库之外，禁止在配置里另写产出根。
- 表格式交付物每行有 `source` 或 `evidence`。策略类文档默认含：摘要、来源、分析、建议、交付物路径、可验证断言、下一步。方法 skill 自带产出模板时从其模板。
- 本文件不单独落盘。

**工具能力化**

- 查证用网页搜索；需要原文时抓取指定 URL；读/写只用本仓库相对路径。
- 不写工具 ID、不写 harness 变量。子代理句只用：dispatch a subagent, else do it inline。

**编排节奏**

- 多步工作默认 Collect → Validate → Analyze → Deliver → Review。进度只认本线台账（营销 `state/marketing-status.md`，获客 `state/lead-status.md`）。多步战役走 `skills/marketing-orchestrator/SKILL.md`（获客走 `skills/lead-generation/SKILL.md`），不另写一套流程。

**语种**

- 面客文案与内部说明分开；以用户本轮语言和产品上下文为准，同一段不混用。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是共用规则，例子教写法形状不教营销内容，无对应事实源材料可借，保留通用支架。

步骤写「用网页搜索查证竞品首页标题；把 URL 与摘录写入交付物来源栏」，不写某家搜索引擎的接线名。来源栏写日期与 URL，不把本节这句话粘进交付物。

## 易错

- 把本文件当会话必载。正确：方法 skill 步骤 0 用相对路径打开。
- 没读产品上下文就写策略。
- 把 skill 例子写进交付物。
- 缺口用自信措辞盖住。
- 断言写成「质量很高」，而不是可检查的句子。
- 为可 inline 完成的任务派子代理。

## 清单

- [ ] 方法 skill 步骤 0 已读本文件；未做 session-start 注入
- [ ] 已读 `product_context`，原文未拷进本仓库
- [ ] 每条外部声明有来源或已标明缺口
- [ ] 已过证据闸（`docs/feedback-rules.md` 第 9 节）；`approved` 只在过闸后写
- [ ] 产出在 `deliverables/marketing/` 或 `deliverables/lead/`（元产出在 `00-system/`）
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
