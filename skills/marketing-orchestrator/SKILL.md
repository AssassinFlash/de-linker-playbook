---
name: marketing-orchestrator
description: >
  Use when starting marketing, SEO, or content work in this repo, or when the
  user asks for the next step, 下一步, 营销, 文案, 内容, 获客, 定位, CRO,
  增长, 度量, a value proposition, or any multi-step marketing workflow that
  needs dependencies, parallel work, or review gates. Read the marketing ledger
  state/marketing-status.md first; announce the current phase, the next method skill, and the output
  path; then run that work (dispatch a subagent, else do it inline) and
  update the ledger. Use this navigator rather than inventing a parallel
  workflow. Greetings get a phase recap only; unrelated coding does not
  start a run.
---

# 营销编排（导航）

读台账、宣布阶段、执行当前工作、回写台账。方法本身在方法 skill 里。依赖与产出路径见 `references/dependency-graph.md`。

## 步骤

1. **读台账** `state/marketing-status.md`（营销台账；获客台账 `state/lead-status.md` 不读不写）。完成：能报出 `phase`、`next`、`method_skill`、`output_dir`、`product_context`。
2. **分流**。推进意图（下一步 / 营销 / 文案 / 内容 / 获客 / 价值主张 / SEO / CRO / “Do the next step…”）→ 步骤 3。寒暄或无关问题 → 复述 `phase` 与 `next`，停。
3. **从当前 phase 做到交付物落地**。进度以台账为准；阶段含义与默认方法 skill 见下表，闸门见 `references/dependency-graph.md`。
   - 台账已写 `method_skill` 且 `skills/<method_skill>/SKILL.md` 存在 → 先读该文件再按其步骤做。需要隔离时 dispatch a subagent, else do it inline。产出进台账 `output_dir`（空则用下表目录）。
   - 该文件不存在 → 停，宣布缺口，不自造流程。
   - 同一 phase 有多个方法 skill：无硬依赖的可并行 dispatch a subagent, else do it inline；有硬依赖的串行。
   - 每完成一阶段先回写台账再继续。硬依赖未满足且无 `user_waiver` → 不停跳。
   - 教学 / 评测 / 进化走 `skills/marketing-teach/SKILL.md`、`skills/marketing-eval/SKILL.md`、`skills/marketing-evolve/SKILL.md` 或 `skills/marketing-skill-eval/SKILL.md`；产出进 `deliverables/marketing/00-system/`，不改战役 `phase`。
4. **回写台账**（步骤 3 的每个 phase 边界都做）。完成：YAML、「当前」表、「已完成」与磁盘一致；`next` 指向下一动作或 `stop`。下一方法 skill 取：台账已指定且文件仍存在的；否则取全量表中依赖已满足、`SKILL.md` 存在的下一个。都没有 → `next: stop`。

## 阶段

| phase | 名称 | 方法 skill | 产出目录 | 完成标准 |
| --- | --- | --- | --- | --- |
| 0 | 读产品上下文 | 只读 `product_context`；需要档案时打开 `skills/marketing-profile/SKILL.md` | 不把原文写入本仓库 | 三条陈述：买家、所卖、缺口 |
| 1 | 基础 | `marketing-positioning`、`marketing-competitor-intelligence`、`marketing-pricing-strategy` | `deliverables/marketing/01-foundation/` | 各方法 skill 交付物非空，且不是例子原文 |
| 2 | SEO | `marketing-seo-audit`、`marketing-ai-seo`、`marketing-programmatic-seo`、`marketing-site-and-schema` | `deliverables/marketing/02-seo/` | 同上 |
| 3 | 内容 | `marketing-content-strategy`、`marketing-copywriting`、`marketing-visual-content` | `deliverables/marketing/03-content/` | 同上 |
| 4 | 获客 | `marketing-social-content`、`marketing-paid-advertising`、`marketing-email-outreach` | `deliverables/marketing/04-acquisition/` | 同上 |
| 5 | CRO | `marketing-landing-page`、`marketing-inquiry-flow`、`marketing-funnel-optimization` | `deliverables/marketing/05-cro/` | 同上 |
| 6 | 增长 | `marketing-launch-strategy`、`marketing-referral-program`、`marketing-retention` | `deliverables/marketing/06-growth/` | 同上 |
| 7 | 度量 | `marketing-analytics-and-optimization` | `deliverables/marketing/07-measurement/` | 同上 |

调研摘录可进 `deliverables/marketing/00-research/`。台账 `output_dir` 若仍是试点根 `deliverables/`，本轮照台账写。

## 默认

- 进度只认台账。
- 产品事实只读 `product_context`（事实源入口 `docs/fact-sources.md`），按其指路取证；查不到标〔未证实〕，按没有处理；不在本仓库另存一份。
- 共用规则若存在则读 `skills/marketing-playbook-standards/SKILL.md`。
- 台账或 `deliverables/marketing/` 缺失时，先打开 `skills/marketing-init/SKILL.md`；该文件不存在则只报缺口。
- 缺来源、缺搜索：停止并写缺口，不编造。需要查证时用网页搜索；需要原文时抓取指定 URL 的正文。
- 交付物带来源栏；数字必须能回溯产品上下文或已抓取 URL。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 清单未过：修一轮，或记录 `user_waiver`。自动修补不超过 3 轮，其后把决策交还用户。
- 获客树 `deliverables/lead/` 不由本 skill 推进。

## 产出

推进时当众宣布：

```markdown
- phase:
- phase_name:
- method_skill:
- output_dir:
- product_context:
```

回写格式见台账「回写」节。不要写仓外路径，不要建外部产出根。

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是编排导航，例子教流程形状不教营销内容，无对应事实源材料可借，保留通用支架。

用户说「下一步」。读出台账 `phase: 0`。当众说：当前 phase 0 读产品上下文，下一方法 skill 为台账 `method_skill`，产出路径为台账 `output_dir`。然后做 phase 0。用户说「你好」只复述 `phase` 与 `next`，不改文件、不跑管线。

## 易错

- 未读台账就开跑，或另写一套阶段。
- `product_context` 读不到仍往下做。
- 硬依赖缺失且无 `user_waiver` 时跳步。
- 方法 skill 文件不存在时自造步骤。
- 把产品上下文原文拷进本仓库。
- 把 skill 例子原文写入交付物。
- 教学/评测改了战役 `phase`。
- 寒暄时改文件。

## 清单

- [ ] 已读台账并当众宣布 phase / 下一 skill / 产出路径
- [ ] 推进时按方法 skill 做完，而不是自造流程
- [ ] 硬依赖已满足或已记录 user_waiver
- [ ] 交付物不是 skill 例子原文
- [ ] 台账已回写
