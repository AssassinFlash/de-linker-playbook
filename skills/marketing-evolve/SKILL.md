---
name: marketing-evolve
description: >
  Use when improving a weak skill, applying a skill-eval or
  marketing-eval improvement recommendation, running one focused
  improvement cycle, 改进 skill, 回写 skill, 当轮清账, evolve after
  eval, skill 修复, eval 失败, playbook maintenance, or patching a
  module after scoring. Read the latest -eval-report.md
  (acceptance item) or -skill-eval-report.md (eight-dimension
  weakest) under deliverables/marketing/00-system/, edit only that
  named gap in the target skill, record the rationale, re-run
  marketing-eval, and close the round with no backlog. Not for
  first-time scoring, teaching methodology, campaign-phase
  navigation, or rewriting several skills at once.
---

# 营销进化（评测回写）

根据已有评测报告，只改本仓库目标 skill 上报告点名的那一条缺口，当轮清账后复评。不评分、不教方法、不推进战役阶段。`-eval-report.md` 点名的是验收条，不是八维；`-skill-eval-report.md` 点名的才是最弱维。

## 步骤

1. **锁定目标与报告**。从用户本轮消息取目标 skill 名。读 `deliverables/marketing/00-system/` 下该 skill 最新报告，按文件名分工：`-eval-report.md` 点名的是验收条（不是八维）；`-skill-eval-report.md` 点名的才是最弱维。没有报告则停：打开 `skills/marketing-eval/SKILL.md`（或 `skills/marketing-skill-eval/SKILL.md`）并按其步骤先评，不凭印象改。完成：能指出 `skills/<name>/SKILL.md`、报告路径与种类、报告点名的唯一缺口。并列时取报告最先写出的那一个。
2. **读目标与模式**。读目标 `SKILL.md` 全文；报告点名了 `references/` 则再读那些文件。报告引用改进模式时，读 `skills/marketing-skill-eval/references/improvement-catalog.md`（文件不存在则只按报告「建议编辑」方向）。完成：能指出要改的章节、拟用模式名、将写入的完成条件。
3. **最小补丁**。只修报告点名的那一条缺口。需要隔离时 dispatch a subagent, else do it inline。写入或修改本仓库相对路径，范围仅 `skills/<name>/`。不删仍成立的方法，只补缺口。改完后该 skill 仍须是正典：frontmatter 仅 `name` + `description`；工具写能力；`SKILL.md` 行数 <500，超了把百科切到该 skill 的 `references/`。完成：diff 只落在目标 skill 目录；该缺口对应的报告建议均已落地或已否决（否决写理由）。
4. **当轮清账**。本轮该缺口上点名的缺陷全部处理完。不另写 backlog、不把其余弱点写成「下次再说」。其他弱点仍在则留给下一次独立的 evolve，不记待办文件。完成：进化记录里 `backlog` 为无。
5. **记录并复评**。按下方模板写入进化记录。不论本轮修的是验收条还是八维，复评都打开 `marketing-eval`，对同一目标按其步骤评一次（不打开 `marketing-skill-eval` 重打八维）。该文件不存在则标「复评待补」，不编造分数。完成：进化记录在 `deliverables/marketing/00-system/`；复评报告已更新或缺口已标明。

## 默认

- 一次一轮、一个 skill、一条缺口（验收条或八维）。用户点了多个目标时只做第一个，其余要新会话。
- `-eval-report.md` 管验收条；`-skill-eval-report.md` 管八维。不要把验收最弱项当成八维来修。
- 本仓库只回写 `skills/<name>/`（含其 `references/`）。不新建 harness 专属 agent 文件，不改 `AGENTS.md`、`state/` 下的两张台账、其他 skill。
- 产出只进 `deliverables/marketing/00-system/`。
- 产品事实不写进 skill。补丁会面会客数字或品类时，读台账 `product_context`（默认 `~/Documents/New/CONTEXT.md`，把 `~` 展开为主目录），只指路不复制。
- 以仓库内文件为准。只有报告要求核对外方法时才用网页搜索查证；搜不到则标缺口，不编造。
- 不把本 skill 当成人批准的替代。会改导航合同或面客事实时停。

## 产出

写入 `deliverables/marketing/00-system/<skill-name>-evolve.md`：

```markdown
# 进化记录

- target:
- eval_report:
- weakest_dimension:
- composite_before:
- pattern:
- backlog: 无

## 改动

- 文件:
- 章节:
- 做了什么:
- 否决与理由:

## 复评

- composite_after:
- 报告路径:
```

`eval_report` 填实际文件名。`weakest_dimension`：验收条报告填最弱项原文；八维报告填最弱维名。
`composite_before`：仅当本轮依据 `-skill-eval-report.md` 时抄其综合分；依据 `-eval-report.md` 则留空（写「未在报告出现」），验收报告没有综合分。
`composite_after`：复评固定跑 `marketing-eval`，验收报告只有 pass/fail、没有综合分，故留空（写「未在报告出现」）。不要为填这个数去跑 `marketing-skill-eval`。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是 skill 改进，例子教当轮修补形状不教营销内容，无对应 New/竞品材料可借，保留通用支架。

评测写「Beginner Clarity 低：步骤没有完成条件」。本轮只给每步补上「完成：…」，不顺手改标题文案，也不把其他维度列成待办。

## 易错

- 没有评测报告就改 skill。
- 把 `-eval-report.md` 的验收条当成八维来修。
- 一次改多个 skill，或把无关清理打进同一补丁。
- 把 P1/P2 写成 backlog 文件，违反当轮清账。
- 改完不复评，或自己编一个综合分。
- 八维补丁后跑 `marketing-skill-eval` 只为填 `composite_after`。
- 把产品上下文原文拷进 skill，或把教学例子写进交付物。

## 清单

- [ ] 已读最新报告，能区分 `-eval-report.md` / `-skill-eval-report.md`，唯一缺口有出处
- [ ] 补丁只落在目标 `skills/<name>/`，正典格式仍成立
- [ ] 本轮该缺口缺陷已清，进化记录 `backlog` 为无
- [ ] `deliverables/marketing/00-system/<skill-name>-evolve.md` 非空
- [ ] 已用 `marketing-eval` 复评或标明「复评待补」；例子原文未进入交付物
