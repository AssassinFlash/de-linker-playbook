---
name: lead-teach
description: >
  Use when the user says teach, learn, 学习, 教我, 双轨学习, 教我获客,
  how lead generation works, 学习模式, or 获客培训, or wants to
  understand HOW a pipeline skill works before seeing results. Run a
  dual-track four-stage loop on one lead method skill: teach methodology
  with everyday analogies and a task card, coach the user without giving
  answers, score coverage then independently execute the same skill, then
  compare and have the user write notes. Assumes zero B2B knowledge.
  Persist across sessions. Write user work, system output, and notes to
  deliverables/lead/00-system/. Not for campaign execution, outreach
  sending, or phase navigation.
---

# 获客教学

用四阶段双轨循环（教 → 用户做 → 评分并系统做 → 对比）教一个获客方法 skill。学习资产只进 `deliverables/lead/00-system/`。

## 步骤

1. **输入**。读用户本轮消息，取出目标学习单元、是否「跳过学习」。未点名则取 `references/stage-templates.md` 学习顺序里第一个未完成且未跳过的单元。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；本会话还没读过就现在读）。读或初始化 `deliverables/lead/00-system/learning-state.md`。在 `skills/` 下确认目标 `SKILL.md`；没有则改读 `references/skill-teaching-guide.md` 对应节，不发明 skill。完成：单元名确定；能指出受众与品类各依据上下文哪几条陈述；原文不拷进本仓库；状态文件已有该单元行。

2. **跳过或定范围**。用户说「跳过学习」：该单元 `skipped: true`，`stage` 保持 0，学习顺序里标「已跳过」（不是「完成」），进入步骤 7。否则读 `references/skill-teaching-guide.md` 该节与 `references/stage-templates.md` 的任务卡范围表。缩减或聚焦时，先向用户说明范围和理由。完成：要么已标记跳过；要么范围类型（概念型 / 搜索型 / 工具依赖型 / 数据密集型）和手工量已告知。

3. **教（Stage 1）**。按 `references/stage-templates.md` 的 Stage 1 模板生成三层，概念以教学指南该节为准，示范只用产品上下文已有事实：① 方法论（流程位置图、场景化问题、概念 + 日常类比、新手错、与前后步关系）；② 任务卡（一步一个动作，写清在哪做、预期看到什么、卡住怎么办）；③ 示范（用当前产品上下文走完任务卡，缺的数字写「未在上下文出现」）。讲完写入 `{skill}-teaching-guide.md`，状态改 `current_stage: 1` 完成后置 2。提示：「教学部分完成。按照任务卡去操作，完成后把结果发给我。格式随意，没有时间限制。」完成：三层都有；每个 B2B 术语首次出现附英文原词；任务卡无复合动作。

4. **用户做（Stage 2）**。等用户交卷，不催「做完了吗」。问具体问题就直接答；方向不清给提示不给答案；完全卡住再示范一步；未问不插手。接受任意格式。交卷后原样写入 `my-work-{skill}.md`（frontmatter 见「产出」），不润色。状态：`user_work` 已有路径，`current_stage: 3`。完成：用户原文已落盘；`coverage` 仍为空。

5. **评分 + 系统做（Stage 3）**。先按教学指南的覆盖率信号写定性反馈（优点要引用具体条目并说明为什么好；遗漏做根因；误区才纠正；意外发现要确认）；改进点每轮 1–2 条。覆盖率写入 my-work 的 `coverage`。然后 **独立** 做同一交付物：目标 `SKILL.md` 存在则按其全文步骤；不存在则按任务卡范围做。需要隔离时 dispatch a subagent, else do it inline。此步不得读取 Stage 2 用户稿。默认用网页搜索查证；需要原文时抓取指定 URL 的正文；搜索不可用则停止，在系统稿标缺口，不编造。只叙述关键决策（选词、筛选、验证），不报工具清单。系统稿写入 `{skill}-system-output.md`，不写战役阶段目录、不改台账 `phase`。清单未满足则补做到可勾，学习环停在 Stage 3。完成：反馈含覆盖率；系统稿非空且能回溯目标步骤；未读用户稿。

6. **对比与笔记（Stage 4）**。按 Stage 4 模板并陈：用户独有、系统独有、同项不同深度、过程对比。给框架「这一步做什么 / 怎么做 / 常见陷阱 / 学到的技巧」，用户用自己的话写，不代写。用户稿写入 `my-notes-{skill}.md`。对比写入 `{skill}-comparison.md`。用户可把系统稿当作该方法的参考草稿；要当战役交付物须另开对应方法 skill，本 skill 不代写战役目录。四阶段齐、笔记已写、用户已看过系统稿，才算该单元 **完成**。完成：对比四块都有；笔记是用户原话；状态 `current_stage` 对该单元为 4。

7. **落盘与下一单元**。更新 `learning-state.md`。推荐学习顺序中下一个未完成、未跳过的单元；顺序外的 `lead-*` 仅当用户点名才教。完成：状态与当前阶段一致；下一单元已说出或用户宣布结束。

## 默认

- 一次会话只教一个单元；四阶段按序。可跨会话续做：读 `learning-state.md`，从下一阶段继续。
- 预设零 B2B 知识。教学、提示、对比全程中文；每个术语首次出现附英文原词。
- 产品事实只读台账 `product_context`，禁止把上下文整篇粘进交付物。
- 进度与产物只进 `deliverables/lead/00-system/`，不写 `.omc/`，不改战役台账 `phase`。
- Stage 3 当用户稿不存在。差距是学习机会。
- 默认课程见 `references/stage-templates.md` 学习顺序（10 个单元）。用户点名其他已存在的 `lead-*` 时同样走四阶段；教学内容从该 `SKILL.md` 抽，任务卡范围默认概念型全量，除非该 skill 依赖联系人发现服务（缩减）或明显数据密集（聚焦）。

## 写法

- 概念用日常类比，不用行话开场。任务卡一步一动作。
- 覆盖率只报事实比例，不做价值判断。
- 系统执行解说只讲决策理由。
- 鼓励看进步，不嘲讽缺口。

## 产出

目录一律 `deliverables/lead/00-system/`。`{skill}` 用学习单元名（有目标目录时用目录名）。

| 文件 | 何时写 |
| --- | --- |
| `{skill}-teaching-guide.md` | Stage 1 |
| `my-work-{skill}.md` | Stage 2 交卷 |
| `{skill}-system-output.md` | Stage 3 |
| `{skill}-comparison.md` | Stage 4 |
| `my-notes-{skill}.md` | 用户自己写完 |
| `learning-state.md` | 每阶段结束 |

各阶段正文模板用 `references/stage-templates.md` 对应节。

**`my-work-{skill}.md` frontmatter：**

```yaml
  ---
  type: user-work
  skill: "{skill}"
  created: "YYYY-MM-DD"
  coverage: null
  ---
```

`coverage` 在 Stage 3 填成如 `6/10`；此前保持空。正文保留用户原文，仅在无结构时加标题，不改写。

**`learning-state.md` 形状：**

```markdown
# learning-state

- active: true
- current_skill:
- current_stage:
- total_units_completed:

## units

| skill | stage | skipped | user_work | system_output | notes_written | coverage | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
```

每结束一个阶段改 `current_stage`；跳过行 `skipped` 为 true 且不计入 `total_units_completed`。已有文件则更新对应行，不删历史。

## 例子

> 仅供理解，禁止引用到输出。

用户说「教我客户画像，我零基础」。确认 `skills/lead-icp-analysis/SKILL.md`（尚未迁入则用 `references/skill-teaching-guide.md` 该节）。Stage 1 用「相亲条件」类比讲 ICP，并出写 3–5 个画像的任务卡。Stage 2 只提示、不代写。Stage 3 dispatch a subagent, else do it inline，不看用户稿。Stage 4 并陈两边，笔记由用户自己写到 `deliverables/lead/00-system/my-notes-lead-icp-analysis.md`。

## 易错

- 跳过 Stage 1 直接练，或 Stage 2 代写成品。
- Stage 3 读了用户稿，对比作废。
- 催促交卷，或一轮列出超过两条改进。
- 替用户写方法论笔记。
- 案例或示范编造上下文没有的数字。
- 把教学进度写入战役台账 `phase`，或把系统稿直接写入 `deliverables/lead/01-icp/` 等战役目录。
- 把尚未迁入的单元当成已有 skill 目录去打开。
- 把本节例子原文写入任何交付物。

## 清单

- [ ] 单元已确定；已读 `product_context`；状态文件有该行
- [ ] 跳过则已标记且未算完成；否则范围已告知
- [ ] Stage 1 三层齐全；术语附英文原词；任务卡一步一动作
- [ ] Stage 2 只教练、不代写；用户稿已存；未催促
- [ ] Stage 3 先评分再独立产出（dispatch a subagent, else do it inline），未读用户稿
- [ ] Stage 4 有四块对比；笔记是用户原话
- [ ] 全部文件在 `deliverables/lead/00-system/`；未改战役 `phase`
- [ ] 下一单元尊重学习顺序；例子原文未进交付物
