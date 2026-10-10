# 阶段模板与产出形状

## 目录

1. [Stage 1 教学文档](#stage-1-教学文档)
2. [Stage 2 用户作业](#stage-2-用户作业)
3. [Stage 3 系统执行解说](#stage-3-系统执行解说)
4. [Stage 4 反馈、对比与笔记](#stage-4-反馈对比与笔记)
5. [任务卡范围](#任务卡范围)
6. [状态文件](#状态文件)
7. [单元映射与学习顺序](#单元映射与学习顺序)

执行任一阶段时读对应节，保证产出形状一致。学习资产一律写到 `deliverables/lead/00-system/`。

---

## Stage 1 教学文档

按这个顺序生成三层。

### 1.1 方法论讲解

```markdown
# {Skill 中文名} — 方法论讲解

## 你在整个流程的哪里

[ASCII 流程位置图，当前步用 ▶ 标出]

## 这一步解决什么问题

[1–2 段。用场景，不用行话。先写买家卡住的具体情境，再写这一步交出什么。品类取自产品上下文，不编。]

## 核心概念

### {概念}（{English term}）
[定义 + 日常类比]

## 常见新手错误

1. **{错法}** — {为什么错} → {改法}
2. ...

## 与前后步骤的关系

- 前一步 ({prev}) 给了你: {what}
- 这一步产出: {what}
- 下一步 ({next}) 需要: {what}
```

### 1.2 任务卡

每一步用同一形状：

```markdown
## 任务卡

### 步骤 1: {一个原子动作}
- **在哪做**: {具体 URL 或公开站点类型}
- **预期看到**: {怎样算做对}
- **卡住了**: {常见障碍与下一步}

### 步骤 2: {一个原子动作}
...
```

规则：

- 一步一个动作，不把两个动作写进同一步。
- 「在哪做」要落到可打开的 URL 或站点类型，不写「去网上搜一下」。
- 每步有「预期看到」，用户能判断自己是否走对。
- 每步有「卡住了怎么办」。

### 1.3 示范

```markdown
## 示范：当前产品上下文的 {skill}

[用台账 product_context 已有事实走完任务卡每一步]
[缺的数字写「未在上下文出现」，不编]
[最终产出与用户将提交的格式相同]
```

---

## Stage 2 用户作业

### Frontmatter

```yaml
---
type: user-work
skill: "{skill-name}"
created: "YYYY-MM-DD"
coverage: null
---
```

`coverage` 在 Stage 4 评分时再填（如 `6/10`）。

### 正文

保留用户原文。无结构时只加标题，不改写、不润色。

路径：`deliverables/lead/00-system/my-work-{skill-name}.md`

---

## Stage 3 系统执行解说

### 系统执行解说

```markdown
## 系统执行讲解

> 正在用网页搜索查证…
> 选择搜索词: "{term}" — 因为 {reasoning}
> 找到 {N} 个结果，筛选标准: {criteria}
> 决策: {what} — 因为 {why}
```

规则：

- 只叙述关键决策，不报能力清单或每次查询。
- 搜索词、筛选、验证的理由要写出来。
- 需要原文时抓取指定 URL 的正文；搜索不可用则停止并写缺口，不编造。
- 系统稿路径：`deliverables/lead/00-system/{skill}-system-output.md`

---

## Stage 4 反馈、对比与笔记

### 反馈模板

```markdown
## 评分反馈

### 做得好的地方
- {具体条目} — {为什么好，连回方法论}

### 遗漏或需要改进
- {具体条目} — {根因：词选错？站点错？概念缺口？}

### 思维误区（如有）
- {误区} — {纠正 + 说明}

### 意外亮点（如有）
- {用户找到、系统未必能找到的}

### 覆盖率
{事实比例}：「你找到了 X 家公司，任务卡目标是 Y 家（覆盖率 X/Y）」
```

规则：

- 先写优点。引用具体条目，不写空「做得好」。
- 遗漏要诊断为什么，不只报缺了什么。
- 改进点每轮 1–2 条。
- 覆盖率只报事实，不做价值判断。

### 并陈对比

```markdown
## 对比分析

### 用户找到、系统没找到
| 项目 | 用户的发现 | 为什么有价值 |
| --- | --- | --- |

### 系统找到、用户没找到
| 项目 | 系统的发现 | 用户可能遗漏的原因 |
| --- | --- | --- |

### 都找到了，深度不同
| 项目 | 用户版本 | 系统版本 | 差异分析 |
| --- | --- | --- | --- |

### 过程对比
| 维度 | 用户 | 系统 |
| --- | --- | --- |
| 搜索关键词 | | |
| 信息源 | | |
| 瓶颈 | | |
| 可借鉴技巧 | — | |
```

路径：`deliverables/lead/00-system/{skill}-comparison.md`

### 方法论笔记

把框架交给用户，让用户自己写：

```markdown
---
type: user-notes
skill: "{skill-name}"
created: "YYYY-MM-DD"
---

# {Skill 中文名} — 我的方法论笔记

## 这一步做什么
[用自己的话写]

## 怎么做（关键步骤）
[用自己的话写]

## 常见陷阱
[用自己的话写]

## 我学到的技巧
[用自己的话写]
```

路径：`deliverables/lead/00-system/my-notes-{skill-name}.md`

用户写正文。不代写。

---

## 任务卡范围

| 类型 | 单元 | 手工范围 | 理由 |
| --- | --- | --- | --- |
| 概念型 | lead-icp-analysis, lead-competitor-analysis | 全量：思考 + 公开网页检索 | 纯分析，不依赖联系人发现服务 |
| 搜索型 | lead-search-term-expansion, lead-company-research, emerging-company-research, lead-distributor-research, distributor-brief, lead-retailer-research | 全量：搜索并记录 | 普通浏览器检索即可 |
| 工具依赖型 | lead-contact-discovery | 缩减：3 家公司，公开网页 + 职业社交网络手动找 | 生产流程常用联系人发现服务；学习只练流程不追产量 |
| 数据密集型 | lead-market-analysis | 聚焦：市场规模 + 竞争格局 + SWOT | 全量手工不现实；其余由系统补 |

范围缩减或聚焦时，必须先向用户说明理由。

---

## 状态文件

路径：`deliverables/lead/00-system/learning-state.md`

不写 `.omc/`，不改 `state/status.md` 的 `phase`。

### 初始（文件不存在时按此创建）

```markdown
# learning-state

- active: true
- current_skill:
- current_stage: 0
- total_units_completed: 0

## units

| skill | stage | skipped | user_work | system_output | notes_written | coverage | source |
| --- | --- | --- | --- | --- | --- | --- | --- |
| lead-icp-analysis | 0 | false | | | false | | lead-teach |
| lead-search-term-expansion | 0 | false | | | false | | lead-teach |
| lead-company-research | 0 | false | | | false | | lead-teach |
| emerging-company-research | 0 | false | | | false | | lead-teach |
| lead-distributor-research | 0 | false | | | false | | lead-teach |
| distributor-brief | 0 | false | | | false | | lead-teach |
| lead-retailer-research | 0 | false | | | false | | lead-teach |
| lead-contact-discovery | 0 | false | | | false | | lead-teach |
| lead-competitor-analysis | 0 | false | | | false | | lead-teach |
| lead-market-analysis | 0 | false | | | false | | lead-teach |
```

进行中时把对应行的 `stage`、路径、`coverage` 填上；`user_work` 填 `my-work-…` 相对路径。保存时机：每阶段结束、用户交卷。续做：读本文件 → 说出上一完成阶段 → 从下一阶段继续。全部完成或跳过仍保留，作为学习日志。

---

## 单元映射与学习顺序

战役阶段目录只用于 Stage 1「你在哪」讲解，**文件不写进这些目录**。

| 学习单元 | 目标 skill（若存在） | 战役阶段（讲解用） | 中文名 |
| --- | --- | --- | --- |
| lead-icp-analysis | `skills/lead-icp-analysis/SKILL.md` | `deliverables/lead/01-icp/` | 客户画像分析 |
| lead-search-term-expansion | `skills/lead-search-term-expansion/SKILL.md` | `deliverables/lead/01-icp/` | 搜索词扩展 |
| lead-company-research | `skills/lead-company-research/SKILL.md` | `deliverables/lead/02-companies/` | 目标公司搜索 |
| emerging-company-research | 无；按 `references/skill-teaching-guide.md` 第 4 节 | `deliverables/lead/02-companies/` | 新兴公司搜索 |
| lead-distributor-research | `skills/lead-distributor-research/SKILL.md` | `deliverables/lead/02-companies/` | 分销商调研 |
| distributor-brief | 无；按 `references/skill-teaching-guide.md` 第 6 节 | `deliverables/lead/02-companies/` | 分销商精简版 |
| lead-retailer-research | `skills/lead-retailer-research/SKILL.md` | `deliverables/lead/02-companies/` | 零售商调研 |
| lead-contact-discovery | `skills/lead-contact-discovery/SKILL.md` | `deliverables/lead/03-contacts/` | 联系人采集 |
| lead-competitor-analysis | `skills/lead-competitor-analysis/SKILL.md` | `deliverables/lead/04-market/` | 竞品分析 |
| lead-market-analysis | `skills/lead-market-analysis/SKILL.md` | `deliverables/lead/04-market/` | 市场分析 |

打开目标 skill 并按其步骤做。无目标 skill 则按教学指南该节做，不发明目录。

学习顺序（当前单元完成或跳过才能进下一个）：

```
阶段 1: lead-icp-analysis → lead-search-term-expansion
阶段 2: lead-company-research → emerging-company-research → lead-distributor-research → distributor-brief → lead-retailer-research
阶段 3: lead-contact-discovery
阶段 4: lead-competitor-analysis → lead-market-analysis
```
