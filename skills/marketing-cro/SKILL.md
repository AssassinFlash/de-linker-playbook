---
name: marketing-cro
description: >
  Use when the user wants to improve conversion rates, run Phase 5
  CRO, CRO 阶段, 转化优化, 转化率, 着陆页, 落地页, 漏斗优化, 询盘流程,
  我要提高询盘转化率, 优化着陆页, 诊断询盘流程, conversion rate
  optimization, landing page diagnosis, funnel drop-off, 先跑一遍
  cro 阶段, or a full CRO pass that needs landing page, funnel
  optimization, and inquiry flow together. Coordinate
  marketing-landing-page, marketing-inquiry-flow, and
  marketing-funnel-optimization from the product context named in
  the ledger; enforce hard dependencies before funnel optimization;
  write strategy docs and matching tables under
  deliverables/marketing/05-cro/. Not for a single page copy edit,
  analytics instrumentation only, product-profile setup, or phase
  navigation.
---

# 营销 CRO 阶段

在产品上下文可读的前提下，按依赖把着陆页、询盘流程、漏斗优化三个方法 skill 跑完。产出只进 `deliverables/marketing/05-cro/`。方法正文在那三个文件里；本文件只管闸门、顺序与收束。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。
2. **闸门**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。入口读不到则停，打开 `skills/marketing-profile/SKILL.md`。读 `skills/marketing-orchestrator/references/dependency-graph.md` 的 cro 段与机器可读 JSON，核对 `global_gates`、三个方法 skill 的依赖与产出路径。`deliverables/marketing/` 缺失则打开 `skills/marketing-init/SKILL.md`。着陆页的硬依赖（定位、文案）或询盘流程的硬依赖（定位）缺失且无 `user_waiver` → 停。三个方法 `SKILL.md` 任一不存在 → 停并写缺口，不自造方法。完成：能报出上下文可读、三文件存在、着陆页与询盘流程的硬依赖。
3. **着陆页与询盘流程**。二者无硬依赖，可并行：打开 `skills/marketing-landing-page/SKILL.md` 与 `skills/marketing-inquiry-flow/SKILL.md`，各 dispatch a subagent, else do it inline。完成：下方四件均在 `deliverables/marketing/05-cro/`、非空、不是例子原文；着陆页 CTA 与询盘入口不互相矛盾。
4. **漏斗优化**。仅当步骤 3 两套交付物 frontmatter 为 `approved`，或台账已记 `user_waiver`。打开 `skills/marketing-funnel-optimization/SKILL.md`，dispatch a subagent, else do it inline。完成：`funnel-optimization.md` 与 `funnel-redesign.xlsx` 同上目录、非空、不是例子原文。
5. **收束**。回写 `state/marketing-status.md`（已完成与磁盘一致；`output_dir` 为 `deliverables/marketing/05-cro/`）。当众列出六件交付物的本仓库相对路径，并给至少一项下一步。某方法失败或降级时，总结写明阻塞点、影响范围及补救路径，不静默跳过。评审未 `passed` 且无 `user_waiver` 时，不把战役推进到下一阶段。完成：summary 含路径与下一步；未另写一套编排。

## 默认

- 进度只认台账。本文件不是总编排器；多阶段导航走 `skills/marketing-orchestrator/SKILL.md`。
- 产品事实只读 `product_context`，原文不拷进本仓库。交付物须能回溯其中的受众、价值主张与询盘路径陈述。
- 表的字段与工作表以各方法 skill 为准；本文件只核对这些路径上的文件非空。
- 目标渠道与落地页技术栈以产品上下文为准，不预设某一电商或表单平台。
- 查证由方法 skill 做：用网页搜索查证；需要原文时抓取指定 URL 的正文。缺搜索则停并写缺口，不编造。
- 诊断须基于已观察数据或可验证的用户行为假设；转化率、停留、提交率未观察到则写缺口，禁止估计后写成事实，禁止纯审美判断。
- 着陆页与询盘流程互无硬依赖，可并行；漏斗优化必须串行。单文件、无并行机会的工作 inline 做完，不 dispatch。
- 不写仓外日志目录。

## 产出

| 策略文档 | 表 |
| --- | --- |
| `deliverables/marketing/05-cro/landing-page.md` | `deliverables/marketing/05-cro/cro-experiment-queue.xlsx` |
| `deliverables/marketing/05-cro/inquiry-flow.md` | `deliverables/marketing/05-cro/inquiry-flow-optimization.xlsx` |
| `deliverables/marketing/05-cro/funnel-optimization.md` | `deliverables/marketing/05-cro/funnel-redesign.xlsx` |

宣布：

```markdown
- phase: 5
- phase_name: CRO
- method_skill: marketing-cro
- output_dir: deliverables/marketing/05-cro/
- product_context:
- files:
- next:
```

## 例子

> 仅供理解，禁止引用到输出。

用户说「先跑一遍 cro 阶段」。输入写「换按钮颜色」或无来源的「转化率提升 30%」。成稿应改成：上下文可读、三个方法 skill 都在、定位与文案已批准；先并行着陆页与询盘，两套批准后再做漏斗。诊断按公开目录+锁价、注册一次审批墙、以及批发摩擦当转化阻碍（价格登录后才见、货期是色块不是日期、RMA 推回厂家、注册等人工审核），P0 用「当前线上 | 最终替换」对照，缺观察数据就写缺口。总结列出六条本仓库相对路径。

着陆页把套餐当一等公民、CTA 对申请贸易账户而不是「立即开始」；询盘一次审核、资格字段与交货能力分开，不要每单再加人工门；漏斗把价格门与审批等待当流失点，每条 hypothesis + metric。临门一脚只拆已有阻碍，不种下新疑虑。不要写成试用开通漏斗，也不把证言人名或本节句子写入交付物。

## 易错

- 没读产品上下文，或上下文不可读仍开跑。
- 跳过依赖图，硬依赖缺失且无 `user_waiver` 时做着陆页、询盘流程或漏斗优化。
- 方法 skill 不存在时自造着陆页、询盘或漏斗步骤。
- 把本文件当总编排器，或回头把工作再交给编排器跑同一阶段（循环）。
- 产出写到本仓库之外，或写进其他阶段目录，或文件名与上表不符。
- 只交策略文档、没有对应表。
- 只跑其中一个方法却宣称本阶段完成。
- 把 CRO 简化成换按钮颜色，没有假设—数据—指标—验证闭环。
- 漏斗只看着陆页，忽略确认页、邮件确认和后续跟进流失。
- 一次并行过多实验，无法区分因果关系。
- 着陆页 CTA、询盘表单与漏斗步骤互相矛盾。
- 编造转化率，或缺少获客/基础洞察时把估计写成事实。
- 总结不列路径、不给下一步，失败时不写阻塞点。
- 不回写台账。
- 评审未过且无 `user_waiver` 时进入下一阶段。
- 把 skill 例子原文写入交付物。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 已读依赖图；硬依赖已满足或已记 `user_waiver`
- [ ] 三个方法 skill 都已按其正文跑完，未自造流程
- [ ] 六件交付物在 `deliverables/marketing/05-cro/`，非空，不是例子原文
- [ ] 着陆页与询盘先并行；漏斗在二者 `approved`（或 `user_waiver`）之后
- [ ] 总结列出相对路径与至少一项下一步
- [ ] 台账已回写；未在评审前跳阶段
- [ ] 工具只写能力；子代理句为 dispatch a subagent, else do it inline
