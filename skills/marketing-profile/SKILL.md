---
name: marketing-profile
description: >
  Use when the user says profile, product context, 产品上下文,
  产品定位, ICP, target audience, 目标受众, company profile,
  公司档案, set up my product, or needs product facts confirmed
  before a marketing run. Read the ledger product_context path
  (default ~/Documents/New/CONTEXT.md); if a number, cert, or
  spec is missing, read fact-base/ under that same tree. Point
  only: never copy product facts into this repo, never write a
  second company dossier. Not for playbook init, phase
  navigation, or conversion copy.
---

# 营销档案（指路）

确认产品事实可从台账路径读到，并留下一份不含事实原文的指针。只指路，不在本仓库另写公司档案。

## 步骤

1. **定位**。读 `state/status.md` 的 `product_context`；缺省为 `~/Documents/New/CONTEXT.md`。读时把 `~` 展开为用户主目录，不要把 `~` 当相对路径。完成：能报出将读的绝对路径；文件不存在或不可读则停，指针里标 `status: missing`，不编造、不另建档案。
2. **读总览**。读该 `CONTEXT.md`。完成：本会话能口头指出买家是谁、卖什么、上下文里没有的数字或证据；原文不拷进本仓库。
3. **缺参数再读**。数字、证书、规格、证明点若总览没有，再读 `~/Documents/New/fact-base/`。文件多时 dispatch a subagent, else do it inline：只回报「哪几个文件覆盖了哪几个主题」，不把正文搬进本仓库。完成：每个缺的参数要么能指到 fact-base 里的文件名，要么列入缺口主题名。不补搜、不访谈写档、不发明。
4. **覆盖核对**。按下方 15 个主题给每个标「有」或「无」。完成：15 行都有标记；「无」只记主题名。
5. **落盘指针** `deliverables/marketing/01-foundation/context-pointer.md`，用下方模板。完成：文件非空；只有路径、覆盖表、缺口主题名；无产品事实段落；教学支架原文零出现。用户若要改事实，改 `~/Documents/New`，不改本仓库。

## 默认

- 产品事实只存在 `~/Documents/New`（先 `CONTEXT.md`，需要参数再 `fact-base/`）。
- 本仓库只写指针，不写第二份公司档案，不写 `data/profile-*`，不改台账里的 `product_context` 路径（交接他机由人改）。
- 缺口保持缺口。下游 skill 同样读台账路径，不读本指针当事实源。

## 产出

```markdown
# 产品上下文指针

- source: （台账 product_context 路径，不粘贴原文）
- fact_base_opened: （相对 ~/Documents/New/ 的文件名，无则 none）
- status: readable | missing
- facts_copied: no

## 覆盖

| 主题 | 有/无 |
| --- | --- |
| 业务概览 | |
| 产品规格 | |
| 价值链 | |
| 目标市场 | |
| ICP | |
| 买家角色 | |
| 问题与痛点 | |
| 竞争格局 | |
| 差异化 | |
| 异议与回应 | |
| 客户用语 | |
| 品牌语气 | |
| 贸易与出口 | |
| 证明点 | |
| 目标与指标 | |

## 缺口

（只列主题名）
```

## 例子

> 仅供理解，禁止引用到输出。

读完后指针写 `source: ~/Documents/New/CONTEXT.md`、`ICP：有`、`证书编号：无`，不把沿革或参数表粘进 `deliverables/`。

## 易错

- 把 `CONTEXT.md` 或 fact-base 原文拷进本仓库。
- 档案缺失时现写一份公司简介顶上。
- 把 `~` 当成仓库内相对路径。
- 用网页搜索补全并落盘。
- 问用户「用几句话描述业务」然后开写档案；纠正应改 `~/Documents/New`。

## 清单

- [ ] 已按台账路径读过（或标 missing 并停止）
- [ ] 本会话能指出买家、所卖、缺口，且未把原文写入本仓库
- [ ] 15 主题均已标有/无；缺口只列主题名
- [ ] 文件在 `deliverables/marketing/01-foundation/context-pointer.md`
- [ ] 例子原文未进入交付物
