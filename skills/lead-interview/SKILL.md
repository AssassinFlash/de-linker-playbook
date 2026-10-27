---
name: lead-interview
description: >
  Use when the user asks for a pre-execution interview, 执行前访谈,
  开始前确认, 问清楚再做, 苏格拉底, Socratic, 清晰度, 歧义, 访谈,
  or to clarify a lead skill before it runs. Adaptive one-question-per-round
  interview that scores product-market fit, scope, success criteria, and
  upstream context, then gates the method skill at 80 percent clarity. Read
  the fact-source entry docs/fact-sources.md and approved
  files under deliverables/lead/ before asking; never re-ask known facts.
  Compile to deliverables/lead/00-system/. Keep the interview inline. Not
  for outreach copy, contact discovery, SEO pages, or phase navigation.
---

# 获客执行前访谈

在跑某个 `lead-*` 方法 skill 之前，用苏格拉底式提问把四维清晰度问到门槛。先读已有材料，只问材料回答不了的问题。访谈必须 inline；通过后再执行目标方法。

## 步骤

1. **共用规则**。读 `skills/marketing-playbook-standards/SKILL.md`。完成：能复述数据锚定、例子禁引用、产出根、工具写能力。

2. **锁定对象**。从用户本轮消息或台账 `state/lead-status.md` 的 `method_skill` 取出目标 skill。必须是已存在的 `skills/{name}/SKILL.md`，且目录名匹配 `lead-` 前缀。未点名则问要为哪个获客 skill 访谈，其他先不问。完成：写出目标目录名；对不上则停并写缺口。

3. **加载与预打分**。只读、不把原文拷进本仓库。
   - 事实源入口 `docs/fact-sources.md`（按其「什么问题查哪个源」取证；查不到标〔未证实〕）
   - 目标 `skills/{name}/SKILL.md` 的数据需求与产出规格
   - `deliverables/lead/` 下与该 skill 相关的已有交付物
   - 打分对照 `references/scoring-rubric.md`；需要问句起点时读 `references/skill-seeds.md`（未列出的 skill 按目标 SKILL.md 现场生成，不套其他 skill 的种子）
   - 建知识地图：已知 vs 缺失。仅凭材料预打分四维：产品上下文覆盖该 skill 所需 → PMF 起分高；上游交付物齐全 → 上游语境起分高；未知项从 0.0 起
   完成：四维各有 0–1 分和一句缺口；已出示预打分卡。加权清晰度 ≥ 80% → 跳到步骤 7，不问。

4. **提问循环**。重复直到步骤 6 的停止条件。
   - 先在已读材料里找答案。找到则静默吸收、更新分数、跳过该问。只问材料不能回答的。
   - 针对当前最低分维度生成恰好 1 题：对准该 skill 的数据需求、接上一轮回答、已确认的不重问；可给选项，用户仍可自由答。
   - 维度策略：PMF = 该 skill 需要但上下文没写清的规格、场景、定位；范围 = 边界、排除、地理/规模/类型过滤；标准 = 产出有用与否的优先级、格式、深度；上游 = 如何解读已有交付物、先做哪条 ICP、优先级。
   - 出示问句卡；收到回答后按评分表重评四维。按信息量打分，不按话多或自信；分数只升不降，除非用户与先前回答或产品上下文矛盾——此时显式问以哪个为准，不默默覆盖。
   - 出示进度表。
   完成（每轮）：只问了 1 题；四维已重评；进度表已出示。

5. **挑战模式**。到轮次阈值时换视角，每种整场只用一次，用完立刻回到普通提问。挑战轮仍只问 1 题，该题即挑战题。记录已用过的模式。
   - 第 4 轮起，市场挑战者（测的是习惯还是更优市场）：你确定 {假定市场} 真的是最佳目标？有没有可能 {替代} 的需求更大？如果 {假定约束} 其实不存在，策略会怎么变？
   - 第 6 轮起，范围精简者（先钉死 1 条 ICP，强过摊薄多条）：如果这次只能选一条 ICP 来执行，选哪条、为什么？哪些约束是真必要的，哪些是习惯性假设？
   - 第 8 轮且清晰度仍低于 70%，本质探寻者（切开堆砌细节）：用一句话描述这次最理想的结果。一周后看到报告，什么内容会让你觉得「这正是我需要的」？
   完成：本轮若触发，模式已记入状态；未触发则跳过。

6. **停止条件**。命中一条就离开循环，进入步骤 7。

   | 条件 | 动作 |
   | --- | --- |
   | 清晰度 ≥ 80% | 编译 |
   | 四维均 ≥ 0.9 | 快路径：不再问，编译 |
   | 用户说「跳过 / 够了 / 直接开始」 | 低于 80% 先警告；再次确认才编译，并写 `user_waiver` |
   | 四维均 ≥ 0.7 但加权低于 80% | 列出剩余缺口，请用户选再问一轮或带缺口编译（不静默放行） |
   | 8 轮 | 软警告，让用户选继续问或编译 |
   | 15 轮 | 硬顶：编译并写明未达门槛 |
   | 连续 3 轮总分变化不超过 5 个百分点 | 未用过本质探寻者则启用；已用过则警告并编译 |
   | 用户说「不知道」 | 记缺口，换维度，不逼问、不扣分、不加分 |

7. **编译**。把访谈上下文写入 `deliverables/lead/00-system/interview-{name}.md`（`{name}` 为目标 skill 目录名）。中断续跑也写同一文件（见「产出」进行中模板）；编完后用编译稿覆盖进行中稿。不写仓外状态目录，不改战役台账的 `phase`。完成：文件非空；含清晰度、四维分数、已确认事实、偏好与约束、缺口；种子问句原文未进入交付物。

8. **交接**。未达 80% 且无 `user_waiver` → 停，列出缺口，不打开目标方法。达门槛或已确认放弃：若本轮还要执行该 skill，打开 `skills/{name}/SKILL.md`，dispatch a subagent, else do it inline，并把本访谈文件当作已确认输入；否则停并宣布该路径。完成：已交接或已停；目标方法未在门槛前偷偷开跑。

## 默认

- 访谈本身必须 inline，等用户逐轮回答；禁止把提问循环派给子代理。
- 进度与产物只进 `deliverables/lead/00-system/`。读仓内文件用相对路径；查证用 Apify 搜索；需要原文时抓取指定 URL。缺文件或Apify 修复与替代取证后仍不可得：记缺口，不编造。
- 产品事实只认台账 `product_context`，不在本仓库另存档案。
- 一场访谈只服务一个 skill、一次执行，不是整场获客立项会。只确认与摊开缺口，不替用户做商业判断。
- 问句与表头用用户本轮语言；下面中文卡片只是形状。
- 加权：`clarity = pmf × 0.35 + scope × 0.25 + criteria × 0.25 + upstream × 0.15`。门槛：清晰度 ≥ 80%（歧义 ≤ 20%）。细则见 `references/scoring-rubric.md`。

## 写法

- 一题一轮，不打包提问。
- 材料里已有的事实（ICP 数量、材质、市场名单）不问。
- 「不知道」记缺口后换维，让后续方法 skill 按已有材料判断。
- 短而补上缺口的回答可以高分；长但重复已知信息不加分。

预打分卡：

```
开始执行前确认 | Skill: {中文名或目录名}

已知信息:
- 产品: {名} （有/缺）
- 目标市场: {市场} （有/缺）
- 上游数据: {逐项有/缺}

当前清晰度: {score}% （目标 ≥ 80%）
```

问句卡：

```
第 {n} 轮 | 聚焦: {维度} | 清晰度: {score}%

{question}
```

## 产出

路径：`deliverables/lead/00-system/interview-{name}.md`。

**进行中（中断可续）：**

```markdown
# 访谈进行中

- skill:
- rounds:
- current_clarity:
- pmf:
- scope:
- criteria:
- upstream:
- challenge_modes_used:
- confirmed_facts:
- gaps:
- updated:
```

**编译稿（覆盖进行中）：**

```markdown
# 访谈上下文

- skill:
- 清晰度:
- PMF / 范围 / 标准 / 上游:
- 轮次:
- user_waiver:

## 已确认信息

-

## 用户偏好与约束

-

## 注意事项

- （清晰度低于 80% 时必填缺口；否则写「无」）
```

进度表每轮出示，不单独落盘：

```
| 维度 | 得分 | 权重 | 加权分 | 缺口 |
| --- | --- | --- | --- | --- |
| 产品-市场匹配 |  | 35% |  |  |
| 范围与约束 |  | 25% |  |  |
| 成功标准 |  | 25% |  |  |
| 上游语境 |  | 15% |  |  |
| 清晰度 |  |  |  |  |
```

## 例子

> 仅供理解，禁止引用到输出。

本 skill 是执行前访谈，例子教提问形状不教营销内容，无对应事实源材料可借，保留通用支架。

目标 skill 是公司研究。产品上下文已写品类与三个市场，上游已有批准的 ICP。预打分 PMF 0.8、上游 0.8，范围与标准仍低。第一问只问「先覆盖全部目标市场还是先钉死一个」，不要问「你们卖什么」。用户说「先做优先市场、只要域名能验证的 15 家」。范围与标准升到门槛，编译进 `deliverables/lead/00-system/interview-lead-company-research.md`，再打开公司研究 skill。

## 易错

- 未读产品上下文和上游交付物就开问。
- 一轮塞多题，或把访谈派给子代理。
- 材料已写明的材质、ICP 数量、市场名单再问一遍。
- 把「四维都到 0.7」当成已过 80% 门槛而静默开跑。
- 用户改口时不确认、直接覆盖旧事实。
- 把种子问句原文写入交付物。
- 未达门槛且无 user_waiver 仍打开目标方法 skill。
- 改战役台账 `phase`，或把状态写到仓外。

## 清单

- [ ] 已读共用规则与 `product_context`；原文未拷进本仓库
- [ ] 目标 skill 已锁定，且是存在的 `lead-*`
- [ ] 提问前已吸收材料能回答的事实；每轮恰好 1 题
- [ ] 打分按 `references/scoring-rubric.md`；矛盾已当面确认
- [ ] 达 80%、用户确认放弃、或硬顶后才编译
- [ ] 文件在 `deliverables/lead/00-system/interview-{name}.md`
- [ ] 种子原文未进入交付物；未达门槛未开跑目标方法
