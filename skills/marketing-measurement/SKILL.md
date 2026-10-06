---
name: marketing-measurement
description: >
  Use when the user wants to set up measurement, testing, and operations,
  run Phase 7 Measurement, 度量, 搭建数据指标体系, 设计 A/B 测试,
  配置 GTM 和 UTM, analytics, KPI tree, event dictionary, RevOps,
  先跑一遍 measurement 阶段, or a full measurement pass that needs
  analytics and optimization together. Coordinate
  marketing-analytics-and-optimization from the product context named
  in the ledger; enforce hard dependencies from landing page, paid
  advertising, and funnel work before measurement; write the strategy
  doc and matching table under deliverables/marketing/07-measurement/.
  Not for a single tracking bug, ad-account reporting only,
  product-profile setup, or phase navigation.
---

# 营销度量阶段

在产品上下文可读的前提下，按依赖把分析与优化方法 skill 跑完。产出只进 `deliverables/marketing/07-measurement/`。方法正文在那个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。读 `state/status.md` 的 `product_context`（缺省 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 measurement 段与机器可读 JSON，核对 `global_gates`、方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。硬依赖（着陆页、付费广告、漏斗优化）缺失且无 `user_waiver` → 停。方法 `SKILL.md` 不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、方法文件存在、三条硬依赖。
3. **分析与优化**。打开 `skills/marketing-analytics-and-optimization/SKILL.md`，dispatch a subagent, else do it inline。完成：下方两件均在 `deliverables/marketing/07-measurement/`、非空、不是例子原文。
4. **收束**。回写 `state/status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/07-measurement/`）。当众列出两件交付物的本仓库相对路径，并给至少一项下一步。方法失败或降级时，总结写明阻塞点、影响范围及补救路径。度量是战役末阶段：评审未 `passed` 且无 `user_waiver` 时，不把战役标为完成；下一步给评审、补缺口或 `stop`，不另起阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、渠道与商业目标陈述。
- 表的字段与工作表以方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与分析栈以产品上下文为准，不预设某一广告或电商平台。
- 查证由方法 skill 做：用网页搜索查证；需要原文时抓取指定 URL 的正文。缺搜索则停并写缺口，不编造。
- 单方法、无并行机会：需要隔离时 dispatch a subagent, else do it inline；否则 inline 做完。
- 不写仓外日志目录，不写编排器运行日志。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/07-measurement/analytics-and-optimization.md` | `deliverables/marketing/07-measurement/analytics-and-optimization.xlsx` |

宣布：

```markdown
- phase: 7
- phase_name: 度量
- method_skill: marketing-measurement
- output_dir: deliverables/marketing/07-measurement/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「先跑一遍 measurement 阶段」。上下文可读，方法 skill 在，上游着陆页、付费广告、漏斗交付物已批准。打开分析与优化方法 skill 跑完。总结列出两条本仓库相对路径，下一步给评审或 stop，不把本节句子写入交付物。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做度量。
- 方法 skill 不存在时自造 KPI、UTM、事件字典或实验步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表，或反之。
- 把单点追踪故障或广告账户报表当成阶段完成。
- 写仓外运行日志。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时把战役标为完成。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 方法 skill 已按其正文跑完，未自造流程
- [ ] 两件交付物在 `deliverables/marketing/07-measurement/`，非空，不是例子原文
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前把战役标为完成
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
