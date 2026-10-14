---
name: marketing-content
description: >
  Use when the user wants to plan and create content, run Phase 3
  Content, 内容策略, 帮我制定内容策略, 我要写网站文案, 需要广告视频脚本,
  content strategy, editorial calendar, 内容日历, 配图方案, 视频脚本,
  先跑一遍 content 阶段, or a full content pass that needs content
  strategy, copywriting, and visual content together. Coordinate
  marketing-content-strategy, marketing-copywriting, and
  marketing-visual-content from the product context named in the
  ledger; enforce hard dependencies before copywriting and visual
  content; write strategy docs and matching tables under
  deliverables/marketing/03-content/. Not for copy polish only, one
  landing-page rewrite, paid-ad media planning, product-profile
  setup, or phase navigation.
---

# 营销内容阶段

在产品上下文可读的前提下，按依赖把内容策略、文案、视觉内容三个方法 skill 跑完。产出只进 `deliverables/marketing/03-content/`。方法正文在那三个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。入口读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 content 段与机器可读 JSON，核对 `global_gates`、三个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。内容策略的硬依赖（定位、竞品、SEO 审计）缺失且无 `user_waiver` → 停。三个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、三文件存在、内容策略的硬依赖。
3. **内容策略**。打开 `skills/marketing-content-strategy/SKILL.md`，dispatch a subagent, else do it inline。完成：`content-strategy.md` 与 `content-strategy.xlsx` 均在 `deliverables/marketing/03-content/`、非空、不是例子原文。
4. **文案**。仅当步骤 3 交付物 frontmatter 为 `approved`，或台账已记 `user_waiver`。打开 `skills/marketing-copywriting/SKILL.md`，dispatch a subagent, else do it inline。完成：`copywriting/` 下至少 1 个非空 `.md`，且 `copy-library.xlsx` 同上目录、非空、不是例子原文。
5. **视觉内容**。仅当步骤 3 与步骤 4 交付物为 `approved`（目录产出：至少 1 个 `.md` 为 `approved`），或台账已记 `user_waiver`。打开 `skills/marketing-visual-content/SKILL.md`，dispatch a subagent, else do it inline。完成：`visual-content/` 下至少 1 个非空 `.md`，且 `visual-style-guide.xlsx` 在 `deliverables/marketing/03-content/` 根、非空、不是例子原文。
6. **收束**。回写 `state/marketing-status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/03-content/`）。当众列出六件交付物的本仓库相对路径，并给至少一项下一步。某方法失败或降级时，总结写明阻塞点、影响范围及补救路径，不静默跳过。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、语气与价值主张陈述。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与发布节奏以产品上下文为准。
- 查证由方法 skill 做：用网页搜索查证；需要原文时抓取指定 URL 的正文。缺搜索则停并写缺口，不编造。
- 本阶段三个方法 skill 有硬依赖，必须串行；单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/03-content/content-strategy.md` | `deliverables/marketing/03-content/content-strategy.xlsx` |
| `deliverables/marketing/03-content/copywriting/` | `deliverables/marketing/03-content/copywriting/copy-library.xlsx` |
| `deliverables/marketing/03-content/visual-content/` | `deliverables/marketing/03-content/visual-style-guide.xlsx` |

宣布：

```markdown
- phase: 3
- phase_name: 内容
- method_skill: marketing-content
- output_dir: deliverables/marketing/03-content/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「买家看不见净价，先跑一遍 content 阶段」。上下文可读，三个方法 skill 都在。先做内容策略；策略批准后再做文案；文案批准后再做视觉内容。总结列出六条本仓库相对路径，不把本节句子写入交付物。

用户说「中间带缺口，帮我制定内容策略」。仍跑完整内容阶段，不在本层展开选题日历。宣布 phase 3、method_skill 为 marketing-content、output_dir 为 `deliverables/marketing/03-content/`。

用户说「目录批发交货后沉默，我要写网站文案」。仍从内容策略起跑，不跳到文案；文案批准后再做视觉。不把本节句子写入交付物。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做内容策略、文案或视觉内容。
- 方法 skill 不存在时自造内容策略、文案或视觉步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表。
- 只跑其中一个方法却宣称本阶段完成。
- 把文案草稿当成最终设计稿，或跳过视觉内容。
- 三个方法并行，未等上游 `approved`。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 三个方法 skill 都已按其正文跑完，未自造流程
- [ ] 六件交付物在 `deliverables/marketing/03-content/`，非空，不是例子原文
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
