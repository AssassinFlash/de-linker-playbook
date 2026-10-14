---
name: marketing-skill-eval
description: >
  Use when 八维, Pass 2, 综合分 0-100, 最弱维, 八维评分, 定义质量,
  skill-eval, or scoring a skill definition on eight weighted
  dimensions; also before a marketing-evolve cycle that needs a
  weakest dimension. Read the named skill under skills/, score
  Pass 2 definition quality with cited evidence, write the report
  to deliverables/marketing/00-system/, and if the composite is
  below 70 name exactly one weakest dimension for marketing-evolve.
  Not for the extraction-spec ten-item acceptance checklist,
  fixtures, or pass-fail (open marketing-eval), campaign plans,
  SEO audits, or phase navigation.
---

# 营销 Skill 定义评测

对目标 `skills/<name>/SKILL.md` 做八维定义质量评分（Pass 2），有交付物时先对照其清单做产出质量（Pass 1）。报告只进 `deliverables/marketing/00-system/`。综合分低于 70 时只点名一个最弱维度，本轮不改目标正文。只跑规格验收 pass/fail 走 `marketing-eval`。

## 步骤

1. **步骤 0 与锁定目标**。读 `skills/marketing-playbook-standards/SKILL.md`。从用户本轮消息取目标 skill 名；不明、不存在或一次点了多份则停，不猜测。完成：唯一路径 `skills/<name>/SKILL.md` 存在；能复述共用规则四条硬约束。
2. **采集**。读目标 `SKILL.md` 全文（有 `references/` 再按需读）。读 `skills/marketing-orchestrator/references/dependency-graph.md` 对应条目；没有该文件或没有该条目则标 `[MISSING_REGISTRY_ENTRY]`，跳过注册表相关分，不编造。读该 skill 最近一份已落地交付物；没有则标 `[NO_DELIVERABLE]`，只评定义。读台账 `state/marketing-status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`，把 `~` 展开为主目录）只为核对 skill 是否要求用上下文，原文不拷进本仓库。用网页搜索查证该 skill 领域现行 B2B 做法，至少 2 个可打开的 URL；需要原文时抓取指定 URL 的正文。搜索不可用则停止并写缺口，不编造。完成：目标文件已读完；注册表/交付物/两条 URL 齐或缺口已标明。
3. **Pass 1 产出质量**。有交付物时，对照目标 skill 的清单与产出规格逐项勾。需要隔离时 dispatch a subagent, else do it inline。无交付物则整节写 `[NO_DELIVERABLE]`，不打产出分。完成：通过项与失败项列表，每条有文件路径。
4. **Pass 2 定义质量**。按「写法」八维各打 0–100，权重见下。每分必须引用步骤 2 的章节、行或 URL；无证据的维度不打分、整份停。`composite` = 各维 `score × weight` 之和，保留一位小数。最弱维取分数最低的一个；并列取表中最先写出的那个。细则不够用时读 `references/skill-eval-protocol.md` 与 `references/eval-rubric.md`。完成：八行评分表 + composite + 最弱维 + 证据。
5. **落盘与触发**。按「产出」写入报告，并追加一条历史。综合分低于 70：读 `references/improvement-catalog.md`，只为最弱维选一条 fix pattern，写出一处建议编辑（路径、旧片段方向、新方向）；`evolve_triggered: true`；下一步打开 `skills/marketing-evolve/SKILL.md`。综合分不低于 70：`evolve_triggered: false`。本 skill 不改 `skills/<name>/`。完成：报告非空；历史多 1 条；`evolve_triggered` 与阈值一致。

## 默认

- 正典评分维是下方八维。只跑规格验收 pass/fail 走 `marketing-eval`，不在此重复、不另写一套尺子。
- 无证据不打分。参考值标「参考」，不当目标。
- 一次只点名一个最弱维。改进计划可列 P0/P1/P2，但建议编辑只对应最弱维。
- 产出只进 `deliverables/marketing/00-system/`。
- 综合分不低于 70 为通过。任一维低于 40 在报告标「需重建」，本轮仍只修最弱维。
- 分档（写入报告，触发仍以 70 为准）：不低于 80 不改；70–79 建议不阻塞；50–69 建议 evolve；低于 50 警告定义质量严重不足。
- 产品事实只指路。针对性高分来自「必须读上下文才能填值」，不是把品类名写进 skill。

## 写法

| 维度 | 权重 | 问什么 |
| --- | --- | --- |
| Search Depth | 15% | Collect 是否给出可执行查询形状（含要从产品上下文填的字段名）？数量是否配得上该 skill 的阶段？ |
| Data Gates | 10% | 最低数据是否量化？不达标怎么处理？关键数字是否要求来源、时效、双源？ |
| Specificity | 15% | 是否强制读 `product_context` 再适配？正文是否不锁死产品/城市/SKU？SaaS 订阅口吻一票否决，该维 ≤40。 |
| Beginner Clarity | 20% | 随机抽 3 步，每步是否有动词+宾语、能力名、输入、成功标准、失败分支？ |
| Brilliance | 15% | 是否有跨行业、反常识或小团队不对称打法？对照 `references/brilliance-patterns.md`，引用 ≥3 条才冲 90。 |
| Anti-Pattern Depth | 10% | 反模式是否 ≥8 且可操作、且是该 skill 独有失败，而不是「不要编造」复制句？ |
| Teaching Value | 10% | 核心步骤是否解释 WHY，而不只是 WHAT？ |
| Deliverable Spec | 5% | 是否写清 `deliverables/` 路径、字段名、min_rows、`source` 列？ |

分数带：90–100 典范；70–89 可接受；50–69 需改进；低于 50 关键缺口。

Beginner Clarity 计分：3 步 × 5 要素，通过数 ÷ 15 × 100；有前置条件清单 +5，有术语表 +5，上限 100。

阶段与查询数量期望见 `references/skill-eval-protocol.md`。缺阶段信息时按中档（15–24 条具体查询为 70 分）。

## 产出

写入 `deliverables/marketing/00-system/<name>-skill-eval-report.md`：

```markdown
# Skill 定义评测

- target:
- product_context: 台账路径（不粘贴原文）
- registry: 已读 | [MISSING_REGISTRY_ENTRY]
- deliverable: 路径 | [NO_DELIVERABLE]
- web_sources:
- composite:
- verdict: pass | fail
- weakest_dimension:
- evolve_triggered: true | false

## Pass 1 产出质量

（勾选项或 [NO_DELIVERABLE]）

## 维度评分表

| dimension | score | weight | weighted_score | evidence | source |
| --- | --- | --- | --- | --- | --- |
| Search Depth |  | 0.15 |  |  |  |
| Data Gates |  | 0.10 |  |  |  |
| Specificity |  | 0.15 |  |  |  |
| Beginner Clarity |  | 0.20 |  |  |  |
| Brilliance |  | 0.15 |  |  |  |
| Anti-Pattern Depth |  | 0.10 |  |  |  |
| Teaching Value |  | 0.10 |  |  |  |
| Deliverable Spec |  | 0.05 |  |  |  |

## 最弱维度分析

## 改进计划

| improvement_id | target_file | weakest_dimension | issue_summary | fix_pattern | source | priority | status |
| --- | --- | --- | --- | --- | --- | --- | --- |

## 建议编辑

- file:
- old_string 方向:
- new_string 方向:
- rationale:
```

`verdict`：composite 不低于 70 为 pass。此 pass/fail 只表示八维综合分是否 ≥70，与 `marketing-eval` 报告里的 `verdict` 同词不同义（那边是抽取规格第 8 节验收条过不过）。评分表必须 8 行。改进计划至少 3 行，每行 `fix_pattern` 与 `references/improvement-catalog.md` 条目名一致；P0 必须是最弱维。

追加 `deliverables/marketing/00-system/eval-history.json`（无则新建）一条：

```json
{
  "skill": "<name>",
  "date": "YYYY-MM-DD",
  "composite": 0.0,
  "weakest_dimension": "",
  "evolve_triggered": false,
  "source": "skills/marketing-skill-eval/SKILL.md"
}
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是定义质量评测，例子教评分形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

目标 skill 步骤写「搜索竞品」且无查询形状：Search Depth 记低分，evidence 写该步骤所在节。建议编辑只补「用网页搜索查证」加查询形状（品类字段、市场字段、年份）。不要把本段写进报告当素材。

## 易错

- 只读目标 SKILL.md，不读注册表与最近交付物。
- 所有维度 80+ 却无逐条证据。
- 一次建议改多个无关维度，或在本 skill 里直接改目标。
- 建议编辑没有文件路径或旧片段方向。
- 漏 `source`，或把参考值当目标。
- 不追加 `eval-history.json`。
- 把某个产品名写进 skill 当「针对性」。
- 综合分低于 70 却不标 evolve。
- 把本报告 `verdict` 当成验收条过不过，或用验收清单的 pass/fail 代替八维。
- 搜索不可用仍编造 URL。

## 清单

- [ ] 已读共用规则与目标 SKILL.md 全文
- [ ] 注册表、交付物、至少 2 个外部 URL 齐或缺口已标明
- [ ] 八维均有 evidence 与 source；composite 为加权和（一位小数）
- [ ] 唯一最弱维有出处；改进计划 ≥3 行且 P0 对应该维
- [ ] 报告在 `deliverables/marketing/00-system/<name>-skill-eval-report.md`
- [ ] 历史已追加；`evolve_triggered` 与 70 阈值一致
- [ ] 未改目标 skill；例子原文未进入交付物
