# 选题方法卡

条件：步骤 3 采集、步骤 4 筛选、步骤 5 编制话题卡时读本文。执行顺序与完成条件以 `SKILL.md` 为准。

## 目录

- [窗口](#窗口)
- [ICP 三问](#icp-三问)
- [换品类测试](#换品类测试)
- [五类角度](#五类角度)
- [四路查询](#四路查询)
- [建议帖类型](#建议帖类型)
- [话题卡字段](#话题卡字段)
- [排序](#排序)
- [缺口](#缺口)

## 窗口

只收当前公历年与上一年能核验的趋势、法规、争议或买家说法。没有年份的常青套话不进主名单。来源早于「当前公历年 − 2」必须标陈旧，默认不进主名单，除非用户本轮点名要历史对照。

## ICP 三问

每条选题至少回答一问，并能指回 `deliverables/lead/01-icp/icp-analysis.md` 的一节（`icp_ref`）：

1. 这会降低我的风险或少掉一个麻烦吗？
2. 这能帮我打到被考核的 KPI 吗？
3. 这会让我看起来比对手先一步吗？

三问都答不上 → 丢弃，不论听起来多「有料」。

## 换品类测试

把选题里的利基换成无关品类。句子仍通顺、仍像一条通用商务建议 → 太泛，丢弃。留下的选题应同时绑利基、应用或采购场景、目标市场。

## 五类角度

`angle` 只取下列枚举（方法约定，不是平台承诺的互动率）：

| angle | 含义 | 何时用 |
| --- | --- | --- |
| mythbust | 隐藏风险、常见误区、行业以为对其实错 | 来源里有被反复说错的做法 |
| before_after | 改变前后，最好有可核验数字 | 来源有基线与结果；没有数字就不要编 |
| case_story | 短情景说明一个判断 | 有公开案例或用户本轮提供的真实情景；不编客户名 |
| checklist | 买家能立刻用的清单或决策框架 | 能写成 5–7 条可执行检查 |
| frustration | 买家希望供应商别再做的事 | 来源是买家抱怨，不是卖方自夸 |

主名单不得只有一个 `angle`。目标覆盖 3 类；来源撑不起则按实有类数写缺口，不硬编。

## 四路查询

花括号是字段，不是要抄进交付物的句子。`{year}` 取环境当前公历年；`{origin}` 取产品上下文的产地/供应路径，上下文没写则用 `import` / `cross-border sourcing`，不填某一出口国。

### 行业趋势

```
"{product_niche}" trends {year} {target_market}
"{product_niche}" challenges buyers {target_market} {year}
```

### 买家痛点与抱怨

```
"{product_niche}" buyer frustrations sourcing {origin} {year}
"{product_niche}" "common mistakes" OR "hidden risks" {target_market}
```

### 公开内容讨论

```
"{product_niche}" {target_market} thought leadership OR LinkedIn
"{product_niche}" procurement discussion {year}
```

搜不到 LinkedIn 公开页或结果是登录墙：改搜行业媒体、协会简报、买家论坛。不要把「搜不到互动数据」写成「高互动」。

### 法规与市场变化

```
"{product_niche}" new regulations {target_market} {year}
"{product_niche}" market changes {target_market} {year}
```

有用：能指出具体趋势、抱怨、法规或采购卡点，来源可打开。噪声：泛泛软文、内容农场、把任何行业套上去都成立的「五点建议」。

## 建议帖类型

`suggested_post_skill` 只点名，不代写帖。对应文件不存在仍写出名称，并在缺口记「帖类型 skill 未迁入」。

| suggested_post_skill | 何时建议 |
| --- | --- |
| `lead-linkedin-authority` | 宏观行业趋势、市场转向 |
| `lead-linkedin-education` | 可执行 how-to、清单 |
| `lead-linkedin-mythbust` | 揭穿误区、隐藏风险 |
| `lead-linkedin-buyer-concern` | 该 ICP 正在担心的具体问题 |
| `lead-linkedin-market-challenge` | 目标市场的结构性挑战 |
| `lead-linkedin-pain-solution` | 痛点接到可核验解法 |
| `lead-linkedin-behind-scenes` | 过程透明；仅当产品上下文有可公开过程 |
| `lead-linkedin-expertise` | 法规、物流、合规知识 |
| `lead-linkedin-faq` | 反复出现的采购问题 |
| `lead-linkedin-personal-story` | 真实短故事；仅当用户本轮提供真实经历，不编 |

同一条选题只建议一个主帖类型。清单/决策框架优先 `lead-linkedin-education`；揭误区优先 `lead-linkedin-mythbust`。

## 话题卡字段

| 字段 | 要求 |
| --- | --- |
| 标题 | 英文，具体，能看出利基与场景 |
| `angle` | 上表五类之一 |
| `icp_question` | 三问之一，原文简述 |
| `icp_ref` | ICP 文件中的节名或画像名 |
| `why_now` | 1–2 年窗口内成立的原因 + 来源年份 |
| `suggested_post_skill` | 上表之一 |
| `hook` | 一句英文开场，测停滑；数字必须来自 `sources` |
| `sources` | 至少一条 URL + 访问日期 + 摘录 |

`hook` 不是成品帖，不套篇幅、标签、CTA。

## 排序

主名单按下列顺序排，不按想象中的点赞数：

1. `icp_ref` 能指到具体痛点或 KPI，而不是整份 ICP
2. 窗口内独立来源数（多源在前）
3. 与已排条目的 `angle` 重复则后移，保证多样性

两条同角度且同 ICP 问：留更具体的那条。

## 缺口

- 某路查询零有用结果：该路标缺口，不编趋势。
- 已验证不足 8 条：按实有条数交付，写差几条、缺在哪一路。
- 来源与候选对不上：该条 `unverified`，进附录，不进主名单。
- 前后对比没有数字：改 checklist 或 frustration，或丢弃；禁止补造百分比。
