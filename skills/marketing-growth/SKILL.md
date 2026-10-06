---
name: marketing-growth
description: >
  Use when the user wants to plan growth, retention, and expansion, run
  Phase 6 Growth, 增长, 增长阶段, 上市策略, 推荐计划, 留存, 复购, 新品上市,
  我要做新品上市, 设计推荐计划, 提高老客户复购, 先跑一遍 growth 阶段, or a
  full growth pass that needs launch strategy, referral program, and
  retention together. Coordinate marketing-launch-strategy,
  marketing-referral-program, and marketing-retention from the product
  context named in the ledger; enforce hard dependencies before each
  method; write strategy docs and matching tables under
  deliverables/marketing/06-growth/. Not for standalone launch planning,
  referral-only work, retention-only work, product-profile setup, or
  phase navigation.
---

# 营销增长阶段

在产品上下文可读的前提下，按依赖把上市策略、推荐计划、留存三个方法 skill 跑完。产出只进 `deliverables/marketing/06-growth/`。方法正文在那三个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。读 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 growth 段与机器可读 JSON，核对 `global_gates`、三个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。三个方法的硬依赖（上市：定位、内容策略、竞品；推荐：定位与定价；留存：询盘流、邮件外展、定价）缺失且无 `user_waiver` → 停。三个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、三文件存在、三个方法各自的硬依赖。
3. **上市、推荐、留存**。三者互无硬依赖，可并行：打开 `skills/marketing-launch-strategy/SKILL.md`、`skills/marketing-referral-program/SKILL.md` 与 `skills/marketing-retention/SKILL.md`，各 dispatch a subagent, else do it inline。完成：下方六件均在 `deliverables/marketing/06-growth/`、非空、不是例子原文；三类交付物能回溯同一套定位与价值主张，渠道、激励与留存动作不互相矛盾。
4. **收束**。核：每份策略含 success metrics；上市文档含 Pre-Launch / Launch / Post-Launch；推荐同时定义 `referrer_incentive` 与 `referee_incentive` 并写出 K-factor 算法；留存覆盖 activation / engagement / resurrection 且含 D1 / D7 / D30；每个增长实验有 primary metric 与至少 1 个 guardrail metric；表含可编辑假设参数。回写 `state/status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/06-growth/`）。当众列出六件交付物的本仓库相对路径，并给至少一项下一步。某方法失败、降级或因业务跳过时，总结写明阻塞点、影响范围及补救路径，不静默跳过。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、任务陈述与价值主张。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空，并核步骤 4 的结构项。
- 目标渠道与激励形式以产品上下文为准，不预设某一电商或社交平台。
- 查证由方法 skill 做：用网页搜索查证；需要原文时抓取指定 URL 的正文。缺搜索则停并写缺口，不编造。
- 数字只写观察到的或表内假设参数；没有就写「公开源未找到」，禁止把估计写成事实。
- 本阶段不替代获客或 CRO：名单与投放走获客阶段，落地页与询盘走 CRO 阶段。
- 三者互无硬依赖，可并行；单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/06-growth/launch-strategy.md` | `deliverables/marketing/06-growth/launch-strategy.xlsx` |
| `deliverables/marketing/06-growth/referral-program.md` | `deliverables/marketing/06-growth/referral-program-design.xlsx` |
| `deliverables/marketing/06-growth/retention.md` | `deliverables/marketing/06-growth/retention-strategy.xlsx` |

宣布：

```markdown
- phase: 6
- phase_name: 增长
- method_skill: marketing-growth
- output_dir: deliverables/marketing/06-growth/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「先跑一遍 growth 阶段」。上下文可读，三个方法 skill 都在，上游硬依赖已满足。三者并行：上市三阶段计划、双边激励推荐、按队列的留存干预一起落盘。总结列出六条本仓库相对路径，不把本节句子写入交付物。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做上市、推荐或留存。
- 方法 skill 不存在时自造上市、推荐或留存步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表。
- 只跑其中一个方法却宣称本阶段完成。
- 把上市写成一次性活动，没有上市后反馈与迭代。
- 推荐只奖邀请人，忽略被邀请人的首次行动与接入路径。
- 留存只看复购，忽略 D1 / D7 / D30 与队列曲线。
- 增长实验无 primary metric 或 guardrail metric。
- 把本阶段策略写成获客投放或 CRO 改版，造成受众重叠或漏斗断层。
- 表内用硬编码数字充当测算，用户无法代入自己的假设。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 三个方法 skill 都已按其正文跑完，未自造流程
- [ ] 六件交付物在 `deliverables/marketing/06-growth/`，非空，不是例子原文
- [ ] 每份策略含 success metrics；上市含三阶段；推荐双边激励与 K-factor；留存含队列窗口与三类干预
- [ ] 每个增长实验有 primary 与 guardrail；表含可编辑假设
- [ ] 三类交付物定位与激励一致；未与获客或 CRO 混写
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
