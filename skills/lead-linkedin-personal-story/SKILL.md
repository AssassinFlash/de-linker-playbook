---
name: lead-linkedin-personal-story
description: >
  Use when personal story post, work anecdote, day in the life,
  founder story, team story, 个人故事帖子, 工作经历分享,
  创业故事帖子, founder journey, factory origin story, engineer
  story, overtime story, lessons learned, career reflection,
  what I wish I knew, years in business, or human narrative
  rather than process explanation, including phase 8 LinkedIn
  of this repo's lead run. Distinct from behind-the-scenes and
  authority trend posts. Brainstorm two or three candidate
  anecdotes, optimize only with user-confirmed details, write a
  Structure 19 post under deliverables/lead/08-linkedin/.
  Invent no lived experience or unsourced stats. Not for
  factory tours, thought-leadership, topic research, or
  posting.
---

# LinkedIn 个人故事帖

按 Structure 19 把已确认的工作经历写成可复制的 LinkedIn 个人故事帖，落到 `deliverables/lead/08-linkedin/`。未确认的经历不当作亲身故事发布。缺证据标缺口，不编造。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。篇幅、钩子、CTA、标签、四种风格、软广只读 `skills/lead-generation/references/linkedin-post-guidelines.md`，不把该文抄进本文件或交付物。完成：能复述数据锚定、例子禁引用、产出根、工具写能力，以及本帖型用 Structure 19。

2. **输入**。产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理。硬依赖：无，可独立执行。软依赖有则读、不阻塞：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/05-usp/product-knowledge.md`。用户本轮给出的经历、教训、主题、视觉描述、CTA 一并作为本轮输入。角色、品类、目标海外受众取产品上下文（有 ICP 则用 ICP 的买家互动场景）；不预设某一出口国或「销售经理」。品类或受众缺到无法让故事对上买家：先看本轮消息；仍缺则打开 `skills/lead-interview/SKILL.md`（存在则按其做），否则停并写缺口。不要在本文件另写问卷。原文不拷进本仓库。完成：能指出品类、受众、角色各依据哪几条；若已有具体经历，能复述该经历与其教训。

3. **候选故事（Structure 19 的 Step 1）**。用户本轮已给出具体经历 → 跳过本步，将该经历标 `user_provided`。否则产出 **2–3** 条互不重复的候选，每条含：Suggested Anecdote（一两句工作瞬间）、Corresponding Core Lesson（一句职业教训）。候选必须贴合品类与海外受众，并全部标明「未确认草稿」。禁止用第一人称把候选写成用户亲身经历。本轮能问则只问一句选哪条或请用户改写成自己的事；用户已说直接做、或本轮不能问 → 不把任一候选当已发生事实，进入下一步时 `story_source: unconfirmed_draft`。完成：已提供经历，或候选表 2–3 行且均为未确认草稿。

4. **优化（Step 1+）**。只在用户已选或已提供的那条上加深，不另编情节。可做：把「我学到了 X」改成「这改变了我做 Y 的方式，因为 Z」；点出经历里已有的情绪（焦急、意外、收场后的谦虚）。不可做：补造日期、数字、地点、感官细节、反转、统计。缺细节列在「待确认」，不写进英文帖。反转只在用户叙述里已经发生时保留。数字、时点、客户名：产品上下文、用户本轮或已查证来源里有才用。优化稿呈用户确认后再成帖；不能问或用户要求直接成稿 → `story_confirmed_by_user: no`，英文帖顶标注「未确认草稿，禁止当作亲身经历发布」。完成：优化稿非空；每一处具体细节都能指回用户原文、产品上下文或「待确认」表。

5. **成稿并落盘（Step 2）**。按「写法」写 Structure 19 英文帖 + 中文策略说明，写入 `deliverables/lead/08-linkedin/personal-story-post.md`。用户点名微博客 / 故事叙事 / 滑梯式 / 直销节奏时，按共用规范只改语气与结构，不改已确认事实；未点名只出 Structure 19 一稿。帖中若出现公开事实或行业数字：用 Apify 搜索查证，需要原文则抓取指定 URL，记下 URL 与访问日期。Apify 修复与替代取证后仍不可得 → 删该数字并写缺口，不编造。不为凑数而搜叙事「最佳实践」。需要隔离时 dispatch a subagent, else do it inline；默认单文件 inline。用户自行发布或经用户已配置的工具发布；本 skill 只产帖稿。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本文件不代替审批、不代替发布。完成：主文件非空；结构段齐；教学支架原文零出现。

## 默认

- 产品与公司事实读事实源入口 `docs/fact-sources.md`，按其「什么问题查哪个源」取证；查不到标〔未证实〕，按没有处理；不在本仓库另存档案。
- 产地、角色、目标市场以产品上下文为准，不锁某一国或某一职位。
- 查证用 Apify 搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。故事本身不靠搜索发明。
- 进度只认台账。产出只进 `deliverables/lead/08-linkedin/`。Markdown only，不写表。
- 帖子正文与标签：英文（用户本轮指定其他语言除外）。策略、缺口、搜索日志：中文。
- 幕后流程、产线、设备走 `skills/lead-linkedin-behind-scenes/SKILL.md`（文件存在时）。行业趋势走 `skills/lead-linkedin-authority/SKILL.md`（文件存在时）。选题卡走 `skills/lead-linkedin-topic-research/SKILL.md`（文件存在时）。多平台日历或战役走 `skills/marketing-social-content/SKILL.md`（文件存在时）。本文件只写人的经历与教训。
- 软广、篇幅、钩子类型、CTA 四类、标签组合、四种风格升级：只遵共用规范，不在本文件复述。

## 写法

Structure 19 固定六段，顺序不可改：

1. **Hook**：把读者拉进这个瞬间或它的结果；钩子必须落在折叠前。
2. **The Anecdote**：短故事。只用已确认细节，宁短勿造。
3. **The Lesson**：职业教训必须由这段经历撑起来，不另贴一句鸡汤。
4. **Professional Connection**：把教训接回用户在跨境贸易里实际帮买家做的事（角色取产品上下文）。
5. **Visual Reference**：仅当用户给了工作场景视觉描述时写一句指向该图；没有则整段省略，并在策略说明写「无视觉，已省略」。
6. **CTA**：恰好一个。用户指定则用；未指定默认评论型（一句对方能用经历回答的问题）。

CTA 之后 3–5 个标签，组合按共用规范；品类标签取产品上下文的品类字段。

- 真实优先于光滑：有棱角的真经历优于编出来的圆满叙事。
- 故事要具体，教训可迁移：具体瞬间教一条海外买家也用得上的原则，不写空的「耐心很重要」。
- 个人不是私域：只写职业场景中的观察与反思。读者应觉得「这个同行我能共情」，而不是读到健康、家庭纠纷或政治。
- 示弱是资产：承认失误或卡住，比「我很成功」更能建立信任。禁止纯自夸成交故事。
- 产品句（若有）最多 1–2 句，删掉后帖子仍独立有用；用经验口吻，不用功能清单。
- 一天日常（day in the life）仍走 Structure 19：把当天切成一个有教训的瞬间，不另起结构。

## 产出

目录：`deliverables/lead/08-linkedin/`

主文件 `personal-story-post.md`：

```markdown
# Personal Story Post

- source: 台账 product_context（不粘贴原文）
- accessed:
- story_source: user_provided | brainstorm_selected | unconfirmed_draft
- story_confirmed_by_user: yes / no
- publish_status: copy_only
- style_variant: structure_19 | 微博客 | 故事叙事 | 滑梯式 | 直销节奏

## 输入摘要
品类 / 受众 / 角色 / 主题 / 用户经历（有则摘一句，无则写未提供）

## 候选故事
| id | anecdote | lesson | status |
| --- | --- | --- | --- |

## 优化故事
待确认：

## LinkedIn Post
[可复制英文正文：Hook → Anecdote → Lesson → Connection → Visual? → CTA → 标签]

## 策略说明
为何选这条、叙事如何服务目标 ICP、软广句（若有）删掉后是否仍成立

## 视觉说明
用户描述或「无」

## 搜索日志
本轮未检索 / URL + 访问日期 + 摘录

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 英文帖按 Structure 19 成段；无视觉则五段并注明省略
- 结尾恰好一个 CTA；标签 3–5 个
- `story_confirmed_by_user: no` 时，英文帖顶有「未确认草稿」声明
- 含数字的句子有来源，或未使用数字
- 教学支架原文零出现
- `publish_status: copy_only`；AI 不代发布，发帖由操作者亲手做

## 例子

> 仅供理解，禁止引用到输出。

竞品调研无 LinkedIn 成帖或用户亲身经历语料：论坛原话是别人第一人称（须匿名，禁止当本帖故事）；OEM 案例是指标+范围+边界，证言人名不可用；摩擦表是买家损失议题不是经历。保留通用支架。

用户只说「分享一个交期教训」但没给事件。应产出 2–3 条未确认草稿（清关延误对上客户时限、样品交期与大货交期被当成同一件事），等用户认领或改写成自己的事再成帖。不要把论坛帖改写成「上周我在海关等了三小时」并当作真经历，也不要把本节句子粘进交付物。

## 易错

- 把候选故事或模型记忆写成用户亲身经历。
- 为「真实感」补造日期、数字、反转或感官细节。
- 为凑次数空搜叙事最佳实践。
- 教训是贴上去的鸡汤，或整帖在自夸成交。
- 写成产线/设备流程（应走幕后帖）或宏观行业趋势（应走权威帖）。
- 把健康、家庭纠纷、政治写进职业帖。
- 复述共用规范全文，或把四种风格四稿一起交（未点名只出一稿）。
- 代替用户点发布。
- 把教学例子原文写入交付物。
- 终稿第一人称经历未确认却无「未确认草稿」标记。

## 清单

- [ ] 已读共用规则、帖子共用规范与 `product_context`，原文未拷进本仓库
- [ ] 已提供经历或 2–3 条未确认候选；未把未确认经历写成亲身故事
- [ ] 优化未补造细节；数字有来源或未使用
- [ ] 英文帖为 Structure 19；钩子在折叠前；恰好一个 CTA；3–5 个标签
- [ ] 无视觉则已省略 Visual 段；产品句可删且帖子仍有用
- [ ] 文件在 `deliverables/lead/08-linkedin/personal-story-post.md`；`publish_status: copy_only`
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
