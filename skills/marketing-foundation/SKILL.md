---
name: marketing-foundation
description: >
  Use when the user wants to establish positioning, pricing, and a
  competitive baseline, run Phase 1 Foundation, 定位, 竞品分析,
  定价策略, 帮我做定位和竞品分析, 我要制定定价策略, 先跑一遍
  foundation 阶段, or a full foundation pass that needs those three
  together. Coordinate marketing-positioning,
  marketing-competitor-intelligence, and marketing-pricing-strategy
  from the product context named in the ledger; enforce hard
  dependencies before pricing; write strategy docs and matching tables
  under deliverables/marketing/01-foundation/. Not for a single
  competitor list, pricing-only work, product-profile setup, SEO
  audits, copy drafts, or phase navigation.
---

# 营销基础阶段

在产品上下文可读的前提下，按依赖把定位、竞品、定价三个方法 skill 跑完。产出只进 `deliverables/marketing/01-foundation/`。方法正文在那三个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。入口读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 foundation 段与机器可读 JSON，核对 `global_gates`、三个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。缺少 hard dependency 且无 `user_waiver` → 停。三个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、三文件存在、定价的硬依赖。
3. **定位与竞品**。二者无硬依赖，可并行：打开 `skills/marketing-positioning/SKILL.md` 与 `skills/marketing-competitor-intelligence/SKILL.md`，各 dispatch a subagent, else do it inline。完成：下方四件均在 `deliverables/marketing/01-foundation/`、非空、不是例子原文。
4. **定价**。仅当步骤 3 两套交付物 frontmatter 为 `approved`，或台账已记 `user_waiver`。打开 `skills/marketing-pricing-strategy/SKILL.md`，dispatch a subagent, else do it inline。完成：`pricing-strategy.md` 与 `pricing-benchmark.xlsx` 同上目录、非空、不是例子原文。
5. **收束**。回写 `state/marketing-status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/01-foundation/`）。当众列出六件交付物的本仓库相对路径，并给至少一项下一步。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与品类以产品上下文为准。
- 查证由方法 skill 做：用 Apify 搜索查证；需要原文时抓取指定 URL 的正文。Apify 与替代取证仍不可得则停并写缺口，不编造。
- 单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/01-foundation/product-positioning.md` | `deliverables/marketing/01-foundation/positioning-data.xlsx` |
| `deliverables/marketing/01-foundation/competitor-analysis.md` | `deliverables/marketing/01-foundation/competitor-profiles.xlsx` |
| `deliverables/marketing/01-foundation/pricing-strategy.md` | `deliverables/marketing/01-foundation/pricing-benchmark.xlsx` |

宣布：

```markdown
- phase: 1
- phase_name: 基础
- method_skill: marketing-foundation
- output_dir: deliverables/marketing/01-foundation/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「买家看不见净价，目录批发交货后沉默，先跑一遍 foundation 阶段」。上下文可读，三个方法 skill 都在。先并行做定位与竞品，两套交付物批准后再做定价。总结列出六条本仓库相对路径，不把本节句子写入交付物。

用户说「中间带缺口、EPC 双闸，先跑 foundation」。同样闸门：定位与竞品并行，批准后再定价；宣布 phase 1、method_skill、`output_dir: deliverables/marketing/01-foundation/`。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做定价。
- 方法 skill 不存在时自造定位、竞品或定价步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或文件名与上表不符。
- 只有策略文档、没有对应表。
- 总结不列路径、不给下一步。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 三个方法 skill 都已按其正文跑完，未自造流程
- [ ] 六件交付物在 `deliverables/marketing/01-foundation/`，非空，不是例子原文
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
