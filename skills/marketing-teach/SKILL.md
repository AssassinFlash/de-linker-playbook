---
name: marketing-teach
description: >
  Use when the user asks to learn marketing, marketing training,
  understand the playbook, 教我营销, 营销培训, 营销方法论, or how
  a marketing-* skill works. Run an interactive four-stage cycle
  (Teach, User Does, System Does, Compare) on one marketing-*
  method skill: explain the framework from that skill, coach a
  practice task without giving answers, independently produce
  the same deliverable, then compare. Ground examples in the ledger
  product context and cited URLs. Write learning notes to
  deliverables/marketing/00-system/. Not for campaign execution, SEO
  audits, phase navigation, or teaching lead-generation methods.
---

# 营销教学

用四阶段循环（教 → 用户做 → 系统做 → 对比）教一个 `marketing-*` 方法 skill。学习资产只进 `deliverables/marketing/00-system/`。

## 步骤

1. **输入**。开场先读 `deliverables/marketing/00-system/learning-state.md`（有则按 `current_skill` / `current_stage` 从下一阶段续，不重开；没有则待本轮落盘时初始化）。读用户本轮消息，取出目标 skill、知识水平（beginner / intermediate / advanced）、当前业务挑战。缺哪项问哪项，已给出的不重复问。读台账 `state/marketing-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；本会话还没读过就现在读）。在 `skills/` 下确认目标目录存在且含 `SKILL.md`；本 skill 只教 `marketing-*`。没有则提出最接近的 `marketing-*`，等用户选定再继续。完成：三要素齐；能指出受众与品类各依据上下文哪几条陈述；原文不拷进本仓库；学习状态已对照。

2. **采集**。读目标 `skills/<name>/SKILL.md`（有 `references/` 再按需读），抽出框架、反模式、最低数据、交付物形状。用网页搜索查证该方法论的公开案例；查询词从产品上下文的品类与市场字段拼，不在本 skill 里填值。需要原文时抓取指定 URL 的正文。搜索不可用则停止，在笔记标缺口，不编造。完成：至少一条带来源 URL 的真实案例；目标 skill 的步骤可复述。

3. **教（Stage 1）**。按用户水平用中文讲方法论（见「产出」Stage 1 模板）。深度：beginner 讲做什么、为什么、关键术语；intermediate 讲怎么套框架与常见错；advanced 讲边界、优化与跨 skill。完成：问题、步骤、理由、概念、反模式都有；案例带来源。

4. **用户做（Stage 2）**。出一道对准其挑战与产品上下文的练习（见「产出」Stage 2 模板）。只给提示和引导问题，不给答案、不代写。用户交卷后原样写入 `{skill-name}-user-output.md`。完成：练习有目标、步骤、评估项；用户稿已落盘。

5. **系统做（Stage 3）**。按目标 skill 全文步骤独立做同一交付物。需要隔离时 dispatch a subagent, else do it inline；此步不得读取 Stage 2 用户稿。完成：`{skill-name}-system-output.md` 非空，且能回溯目标 skill 的步骤。

6. **对比（Stage 4）**。按「产出」对比模板并陈两边，优点与差距都要落到证据和可执行改法。问反思问题，把用户自己的 3–5 条收获记下来。完成：至少两个维度表、一条具体优点、一条具体改进、一段差异原因。

7. **落盘**。写入下方产出列表，并更新 `learning-state.md` 与 `learning-roadmap.md`。推荐下一 skill 时：若有 `skills/marketing-orchestrator/references/dependency-graph.md` 则按其上游；否则只推荐已满足输入条件的方法 skill，缺上游先学上游。完成：主笔记七节齐全且每节有来源；状态文件与当前阶段一致。

## 默认

- 一次会话只教一个 skill；四阶段按序，不跳。
- 本 skill 只教 `marketing-*`。教获客方法走 `lead-teach`。
- 可跨会话续做：开场读 `deliverables/marketing/00-system/learning-state.md`，从下一阶段继续。
- 产品事实只读台账 `product_context`，练习可以引用其中字段，禁止把上下文整篇粘进交付物。
- 案例必须能打开的 URL 或「台账 product_context（不粘贴原文）」；没有就标 `待补真实来源` 并停，不编。
- Stage 2 教练口吻：「你已经有哪些数据？还缺什么？」指向 Stage 1 的对应步骤，不给成品。
- 进度与产物只进 `deliverables/marketing/00-system/`，不写 `.omc/`、不改战役台账的 `phase`。
- 对比建设性：差距是学习机会，不嘲讽。

## 写法

- 教学材料用通用方法句；品类、材质、产地以产品上下文为准，不写进本 skill。
- 水平与挑战只从用户消息或本轮问答来，不猜测。
- 系统版与用户版分文件；对比文件引用二者路径，不把某一边改成另一边。

## 产出

目录一律 `deliverables/marketing/00-system/`。`{skill-name}` 用目标目录名。

**Stage 1 讲解（写入 `{skill-name}-teaching-guide.md`，会话里先讲一遍）：**

```markdown
# {skill-name} 方法论

## 这个 skill 解决什么问题？
（1–2 句，对齐用户挑战；品类取自产品上下文，不编）

## 核心方法论
（目标 skill 的步骤）

## 为什么这样做？
（理由 + 采集来源）

## 关键概念
1.
2.

## 常见错误
1. 错法 → 做法
```

**Stage 2 练习（写入主笔记「练习任务」；用户稿另存）：**

```markdown
# 练习任务

## 目标
## 步骤
## 评估标准
- [ ]
## 提示
- 先看 Stage 1
- 卡住时要提示，不要答案
```

**Stage 4 对比（`{skill-name}-comparison.md`）：**

```markdown
# 对比分析

## 维度 1: 数据支撑
| 指标 | 用户版 | 系统版 |
| --- | --- | --- |
| 来源条数 | | |
| 引用 URL | | |

## 维度 2: 可执行性
| 指标 | 用户版 | 系统版 |
| --- | --- | --- |
| 可直接落地的动作 | | |

## 做得好的地方
1.

## 可以改进的地方
1. （差距 + 怎么改）

## 关键差异
（漏了或改了哪步）
```

**主笔记 `{skill-name}-notes.md` 必含七节，每节至少一条来源：** 学习目标；方法论摘要；真实案例（含 URL）；练习任务；对比总结；关键收获；下次改进。

**同批还要写：**

| 文件 | 内容 |
| --- | --- |
| `{skill-name}-user-output.md` | Stage 2 用户原文 |
| `{skill-name}-system-output.md` | Stage 3 独立产物 |
| `learning-roadmap.md` | 已学清单、下一步、上游是否满足 |
| `learning-tracker.md` | 下方三张表，每行有 `source` |
| `learning-state.md` | `current_skill`、`current_stage`、`skills_completed`、`total_skills_learned` |

`learning-tracker.md` 三表字段：

- Skills Learned：`skill_name`，`date_started`，`date_completed`，`knowledge_level`，`business_challenge`，`source_skill_md`，`source_dependency_graph`，`status`，`source`
- Learning Notes：`skill_name`，`stage`，`insight`，`user_example`，`system_example`，`gap`，`source_url`，`source_context`，`source`
- Practice Log：`skill_name`，`exercise`，`user_output_path`，`system_output_path`，`completion_date`，`score_self`，`score_system`，`source_references`，`source`

本轮至少追加 1 条 Skills Learned、每完成阶段 1 条 Learning Notes、1 条 Practice Log。已有文件则追加，不覆盖历史行。

**`learning-state.md` 形状：**

```markdown
# learning-state

- current_skill:
- current_stage:
- total_skills_learned:

## skills_completed

| skill | date | stages_completed | knowledge_level | source |
| --- | --- | --- | --- | --- |
```

每结束一个阶段就改 `current_stage`；四阶段都完才写入 `skills_completed`。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是营销教学，例子教四阶段循环形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

用户说「教我定位，我是初学者，询盘转化差」。先确认 `skills/marketing-positioning/SKILL.md` 存在并读产品上下文。Stage 1 用该 skill 的步骤讲定位，并引用一条带 URL 的公开案例。Stage 2 只出「写出一句谁、得到什么、凭什么信」的练习和提示，不代写。Stage 3 dispatch a subagent, else do it inline，不看用户稿。Stage 4 用数据支撑与可执行性两表对比，笔记写到 `deliverables/marketing/00-system/marketing-positioning-notes.md`。

## 易错

- 跳过 Stage 1 直接练。
- Stage 2 代写或给成品答案。
- Stage 3 读了用户稿，对比作废。
- 案例无 URL、无上下文出处，或编造数字。
- 水平不匹配：初学者上优化，或熟练者重复术语表。
- Stage 4 只说好坏，不说差异原因和改法。
- 不更新 `learning-state.md`，或把教学进度写进战役台账 `phase`。
- 追踪表缺 `source` 列。
- 推荐下一 skill 时忽略上游未完成。
- 把本节例子原文写入任何交付物。

## 清单

- [ ] 目标 skill 为 `marketing-*` 且存在；水平与挑战已确认；已读 `product_context` 与 `learning-state.md`
- [ ] Stage 1 有真实来源案例；深度匹配水平
- [ ] Stage 2 只教练、不代写；用户稿已存
- [ ] Stage 3 独立产出（dispatch a subagent, else do it inline），未读用户稿
- [ ] Stage 4 有两维度、一优点、一改进、一原因
- [ ] `deliverables/marketing/00-system/` 下七类文件齐；主笔记七节每节有来源
- [ ] `learning-tracker.md` 每行有 `source`；`learning-state.md` 已更新
- [ ] 下一 skill 尊重上游；例子原文未进交付物
