---
name: marketing-eval
description: >
  Use when 验收, 夹具, 抽取规格第 8 节十条, pass-fail, marketing-eval,
  extraction-spec acceptance, or checking whether a named skill
  under skills/ meets the ten checklist commands. Read evals
  fixtures if any exist, run the section-8 commands on that
  directory, and write a pass or fail report to
  deliverables/marketing/00-system/. Every finding must cite
  command output or a file line. Do not rewrite the target here
  (open marketing-evolve) and do not invent a second rubric. Not
  for eight-dimension scoring, composite 0-100, or naming a
  weakest dimension (open marketing-skill-eval).
---

# 营销评测

按 `evals/` 夹具与 `wayfinder/extraction-spec.md` 验收清单，判断一份 skill 正典是否过关。报告只写入 `deliverables/marketing/00-system/`；本 skill 不改目标正文。要打分或点最弱维走 `marketing-skill-eval`。

## 步骤

1. **锁定目标**。从用户本轮消息取 skill 的 `name`。目录必须是 `skills/` 下已有文件夹，且内含 `SKILL.md`。不明、不存在或一次点了多份：停，列出候选，不猜测、不批量。完成：唯一目标 `name`。
2. **读尺子**。读 `wayfinder/extraction-spec.md` 第 8 节十条验收命令（含期望）。再按文件名模式查找本仓库 `evals/` 里文件名含该 `name` 的夹具。没有夹具（仅占位文件或空目录）记「无夹具」，不编造断言、不读源仓评测样本。完成：能复述将跑的命令；夹具有或无已记录。
3. **采集**。读本仓库相对路径：目标 `SKILL.md` 与其 `references/`（若有）。需要隔离时 dispatch a subagent, else do it inline。完成：正文与 references 已读完。
4. **跑验收**。在仓库根运行 shell 命令。把规格第 8 节每条命令的扫描路径收到该 `skills/<name>/`（含其 `references/`）以及 `.agents/skills/<name>` 软链；**不改正则、不扩词表、不另写一套规则**。有夹具则按其内断言再跑；夹具格式看不懂则停，在报告写缺口。完成：十条（加夹具项）各有退出码或匹配结果。
5. **落盘**。写入 `deliverables/marketing/00-system/`，文件名为目标 `name` 加 `-eval-report.md`。任一条非零或未满足期望即 **fail**。fail 时只标最先失败的一条为最弱项，下一步打开 `skills/marketing-evolve/SKILL.md`；本轮不改目标 skill。完成：报告非空；每条结论带 evidence（命令输出或文件行）；教学支架原文未当素材写入。

## 默认

- 尺子是 `wayfinder/extraction-spec.md` 第 8 节。与规格冲突时停并上报，不发明第二套规则。
- 本 skill 只出 **pass / fail**，不打 0–100。定性八维走 `marketing-skill-eval`。
- 一轮只评一份 skill；评的是正典，不是战役文案、不是 agent 定义。
- 产出只进 `deliverables/marketing/00-system/`。不改目标 skill，不改 `AGENTS.md`、`state/`、`wayfinder/`。
- 仓外路径只允许 `~/Documents/New/...`。本评测通常不读产品上下文。

## 产出

```markdown
# 评测报告

- target:
- spec: wayfinder/extraction-spec.md 第 8 节
- fixtures: 无 | 路径
- verdict: pass | fail

## 验收

| # | 项 | 结果 | evidence |
| --- | --- | --- | --- |
| 1 | name 正则与目录一致 |  |  |
| 2 | description 长度与字符 |  |  |
| 3 | 禁用 frontmatter 字段 |  |  |
| 4 | harness 工具 ID / 变量 |  |  |
| 5 | 产品词 |  |  |
| 6 | 例子标注 |  |  |
| 7 | 路径 |  |  |
| 8 | 行数上限 |  |  |
| 9 | 扁平与软链 |  |  |
| 10 | 产出根 |  |  |

## 夹具

无夹具 | 断言与结果

## 最弱项

pass 写「无」。fail 写最先失败的一条，附 evidence。

## 下一步

pass：停。fail：打开 skills/marketing-evolve/SKILL.md；本轮不改目标。
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是工作流评测，例子教验收形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

目标 `description` 折叠后 280 字：第 2 条记 fail，evidence 写测得字数；不得改口为「接近 300，算过」。`evals/` 只有占位文件：夹具节写「无夹具」，仍跑完十条。

## 易错

- 当成本仓库另一套评分，不跑规格里的命令。
- 目标不明仍开评，或一次评多份。
- fail 后直接改 skill（应走 `marketing-evolve`）。
- 把源仓评测样本当本仓库夹具。
- 无夹具就跳过验收清单。
- 报告无 evidence，或把 skill 例子原文整段贴进报告当素材。

## 清单

- [ ] 目标 `name` 唯一且 `SKILL.md` 存在
- [ ] 已读规格第 8 节；夹具有无已记录且未编造
- [ ] 十条命令已在仓库根按收窄路径跑完
- [ ] 报告在 `deliverables/marketing/00-system/`，每条有 evidence
- [ ] fail 时只指出最弱一条，且未改目标正文
- [ ] 例子原文未进入交付物
