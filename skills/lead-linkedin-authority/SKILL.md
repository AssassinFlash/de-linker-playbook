---
name: lead-linkedin-authority
description: >
  Use when writing a LinkedIn industry-trend post, thought-leadership,
  market-shift analysis, authority content, industry insight, 权威内容,
  行业趋势帖子, 行业洞察, or "why more buyers choose X" as a market
  shift not a how-to, including phase 8 LinkedIn of this repo's lead
  run. Identify one sourced current trend, analyze it for one ICP and
  region, then draft Structure 2: Hook, Analysis, Connection-and-Value,
  CTA. Distinct from education tips and export-compliance posts. Read
  product_context and approved topic research; invent no trends or
  statistics. Write to deliverables/lead/08-linkedin/. Drafts only;
  the user publishes. Not for topic lists or phase navigation.
---

# LinkedIn 权威帖（行业趋势 / Structure 2）

核一条可引用的当前行业趋势，按 Structure 2 写出可复制的 LinkedIn 权威帖，落到 `deliverables/lead/08-linkedin/`。本 skill 只产帖稿；用户自行发布或经用户已配置的工具发布。缺证据标缺口，不编造趋势或统计。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **输入**。读台账 `state/status.md` 的 `product_context`（默认 `~/Documents/New/CONTEXT.md`；把 `~` 展开为主目录，不当相对路径）。需要参数再读 `~/Documents/New/fact-base/`。硬依赖：已批准的 `deliverables/lead/08-linkedin/topic-research.md`。软依赖存在则读：`deliverables/lead/01-icp/icp-analysis.md`、`deliverables/lead/05-usp/usp-strategy.md`、`deliverables/lead/05-usp/product-knowledge.md`。用户本轮给出的趋势主题、区域、CTA 或风格点名一并记「用户本轮」。品类、ICP、区域或趋势焦点仍缺到无法下笔时，打开 `skills/lead-interview/SKILL.md`（存在则按其做）；不存在则把缺口写入台账，不在本文件另写问卷。完成：能指出品类、ICP、区域、CTA 意向、候选宏观趋势各依据哪几条；原文不拷进本仓库。硬依赖文件缺失、用户本轮也未给出可核验的趋势主题、且无 `user_waiver` → 停。

3. **选题与查证**。从已批准话题研究里选一条**宏观行业趋势**（市场结构、需求转移、材料或工艺偏好、区域展望、供应侧含义），不要选 how-to 或合规手册题。用户本轮点名趋势则优先核该条。用网页搜索按 `references/trend-research.md` 三条意图查证：识别、数据核验、对目标受众的影响。需要原文则抓取指定 URL 的正文。搜索日志格式见 `skills/lead-generation/references/search-protocol.md`。搜不到或搜索不可用 → 换一条已核验趋势；都核不上则停并写缺口，不编造。禁止为凑次数空搜。多候选需隔离核验时 dispatch a subagent, else do it inline。完成：只保留一条趋势；时效在近 1–2 年；每条将写入帖子的数字或判断有 URL、访问日期与摘录。

4. **分析**。按 `references/structure-2.md` 写出对该 ICP 与区域的含义，以及产品是否接得上。完成：策略说明同时有角色、区域、该趋势造成的具体后果；产品句能指回上下文已有能力，或已决定本帖无产品句（第三拍改写为买家可执行含义）。接不上就不硬接。

5. **起草**。按 Structure 2 四拍写完整英文帖。篇幅、钩子类型、CTA、标签、语气、软广与四种风格只读 `skills/lead-generation/references/linkedin-post-guidelines.md`，不要把该文件抄进交付物。用户点名四种风格之一时，只改语气与结构，不改趋势事实与来源。未点名不升级。CTA：用户本轮点名且落在规范四类之一则用；否则默认评论型，问一句该 ICP 可答的经验问题。完成：四拍齐全；钩子在折叠前；恰好一个 CTA；3–5 个标签；产品句（若有）最多 1–2 句，删掉后帖子仍有用。

6. **质检并落盘**。对照清单与共用规范出门清单后，写入 `deliverables/lead/08-linkedin/authority-post.md`。不发布。仅当用户本轮要求发布 **且** 已配置发布工具时，才经该工具发出并记 `publish_status`；否则 `copy_only`。付费能力须先告知并获准。完成：主文件非空；含可复制正文、趋势来源、策略说明、搜索日志；教学例子原文零出现。验证—审查—审批走 `skills/lead-generation/references/orchestration-protocol.md`，本 skill 不代替审批、不代替发布。

## 默认

- 产品事实只读台账 `product_context`（需要参数再读 `~/Documents/New/fact-base/`），不在本仓库另存档案。
- 查证用网页搜索；需要原文时抓取指定 URL。不并列搜索引擎菜单。搜索不可用则停止并写缺口，不编造。
- 进度只认台账。产出只进 `deliverables/lead/08-linkedin/`。Markdown only，不写表。
- 帖子正文英文（用户本轮指定其他语言则从其）；策略、分析、缺口跟本轮语言（缺省中文）；标签英文。
- 本 skill 只产帖稿。用户自行发布或经用户已配置的工具发布。
- 教育型 how-to 走 `skills/lead-linkedin-education/SKILL.md`（文件存在时）。出口、物流、市场准入合规走 `skills/lead-linkedin-expertise/SKILL.md`（文件存在时）。选题卡走 `skills/lead-linkedin-topic-research/SKILL.md`。多平台日历或战役走 `skills/marketing-social-content/SKILL.md`（文件存在时）。本文件不写那几类。
- 单篇 inline 做完。用户点名多篇时每篇独立核趋势；需要隔离时 dispatch a subagent, else do it inline。

## 写法

- 四拍顺序固定：Hook → Analysis → Connection & Value → CTA。拍内规则见 `references/structure-2.md`。
- 钩子必须是这条已核验趋势或其中一条有来源的数字，不要空套开场。
- 分析必须落到「这个 ICP、这个区域、此刻多了一件具体麻烦或机会」。放之四海皆准的判断不算完成。
- 第三拍默认写趋势与上下文能力的自然连接；焦点是趋势相关性，不是规格表。连不上则不写产品，第三拍改写该 ICP 接下来该看什么。
- 产品句可用「This is why we…」「In response to this shift, our approach…」「For buyers facing this challenge, solutions like…」一类，不用功能清单口吻。
- 过宽、无区域、无买家后果的判断不采用。
- 终稿面客段禁止残留未解释的占位符；缺署名或公司名用 `[待补充]` 或省略。

## 产出

主文件 `deliverables/lead/08-linkedin/authority-post.md`。

```markdown
# Authority Post

- source: 台账 product_context（不粘贴原文）
- accessed:
- icp:
- region:
- trend:
- structure: 2
- style: default | micro_blog | storytelling | slippery_slide | direct_response
- publish_status: copy_only | published_by_user | sent_via_configured_tool
- publish_tool: not_configured | configured

## 策略说明

## 趋势来源

| 声明 | URL | 访问日期 | 摘录 |
| --- | --- | --- | --- |

## 帖子（可复制）

## 结构标注

- Hook:
- Analysis:
- Connection & Value:
- CTA:

## 搜索日志

| 查询或 URL | 日期 | 结论 |

## 缺口

## 下一步
```

断言（未满足则不算全量完成）：

- 正文按 Structure 2 四拍，结构标注与正文一致
- 趋势时效在近 1–2 年；每条数字或趋势判断有 URL 与摘录
- 分析同时出现 ICP 角色、区域、具体后果
- 产品句 0–2 句；有产品句则可删且帖子仍有用
- 钩子在折叠前；恰好一个 CTA；3–5 个标签且品类标签取产品上下文
- `publish_status` 与是否真正发出一致；未要求发布或未配置工具时必为 `copy_only`
- 教学支架原文零出现

## 例子

> 仅供理解，禁止引用到输出。

输入写「行业在变、买家更看重可持续」。应核到一条近 1–2 年、带 URL 的趋势。分析不要停在空判断，而要落到该 ICP、该区域、此刻多出的一件具体麻烦。形状借自案例页的「指标 + 范围 + 边界」：先写可核验标签事实（哪类买方、哪国、哪类应用、相对哪条已公布基线多了一项约束），再写叙事；同一条趋势只落双闸一扇——商务谈判闸（报价窗口、框架条件）或技术批准闸（证书、配对证据），另一扇可以否决这一扇，不要写成「买家整体更绿了」。不要写成操作步骤或合规清单。

选题纪律对照「正文扛事实、引言不顶事实」：权威帖只处理市场上已存在、订货前就会卡住的结构约束，不种新疑虑、不写升档问、不把商务闸与技术闸的问法串进同一分析。产品句只在上下文能力接得上时出现 1–2 句，主语是交付协同不是型号清单，并写清「做到这里停」（不写成制造商、不把库存时效当趋势）。不要写无来源百分比，不要把法规条款号当趋势事实。不要把本节句子粘进交付物。

## 易错

- 没读产品上下文或已批准话题研究就发明趋势。
- 搜索不可用仍写统计，或为凑查证次数空搜。
- 分析不点名 ICP 与区域，写成谁都适用。
- 硬塞产品规格，删掉产品句后帖子站不住。
- 把 how-to 或合规手册写成权威帖。
- 把教学例子或共用规范原文写入交付物。
- 未配置或不要求发布时仍当作已发出。
- 终稿残留未解释占位符，或把 `[待补充]` 假装成已核实署名。

## 清单

- [ ] 已读共用规则与 `product_context`；硬依赖已读或已停并写缺口
- [ ] 一条趋势已按三条意图核验；数字均有来源；无来源则未使用统计
- [ ] 分析含 ICP、区域、具体后果；产品句已赚到或已省略
- [ ] 英文帖为 Structure 2；钩子在折叠前；一个 CTA；3–5 个标签
- [ ] 文件在 `deliverables/lead/08-linkedin/authority-post.md`；未要求发布时未发送
- [ ] 教学例子原文未进入交付物
- [ ] 工具只写能力；需要隔离时为 dispatch a subagent, else do it inline
