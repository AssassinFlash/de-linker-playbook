# 发现状态（跨轮学习）

跨多次方法 skill 执行，记录哪些搜索词与查证路径真正产出可用名单。可选文件：`deliverables/lead/00-system/discovery-state.md`（或同名 `.json`）。不存在则跳过，不阻塞战役。进度仍只认 `state/lead-status.md`。

## 目录

- [形态](#形态)
- [操作定义](#操作定义)
- [更新规则](#更新规则)
- [裁剪](#裁剪)
- [模式提取](#模式提取)
- [下一轮实验](#下一轮实验)

## 形态

```json
{
  "version": 1,
  "product_context": "ledger key only, do not paste source text",
  "created": "YYYY-MM-DD",
  "updated": "YYYY-MM-DD",
  "cycle_count": 0,
  "observations": {
    "search_effectiveness": [
      {
        "skill": "lead-company-research",
        "cycle": 1,
        "search_term": "{positioning_term} {market}",
        "capability": "web_search",
        "results_found": 0,
        "results_useful": 0,
        "date": "YYYY-MM-DD"
      }
    ],
    "capability_success_rates_by_skill": {},
    "capability_success_rates_global": {
      "web_search": { "attempts": 0, "successes": 0 },
      "fetch_url": { "attempts": 0, "successes": 0, "blocked": 0 }
    },
    "skill_quality": [],
    "icp_effectiveness": [
      {
        "icp_name": "{icp_name}",
        "companies_found": 0,
        "contacts_found": 0,
        "search_terms_that_worked": [],
        "search_terms_that_failed": []
      }
    ]
  },
  "models": {
    "best_search_terms": [],
    "best_capabilities_by_skill": {},
    "icp_ranking": [],
    "domains_blocked_on_fetch": []
  },
  "next_experiments": {
    "search_terms_to_try": [],
    "capabilities_to_prioritize": {},
    "icps_to_expand": [],
    "icps_to_deprioritize": []
  }
}
```

`capability` 只写能力名：`web_search`、`fetch_url`、`contact_finder`（仅当用户已配置）、`collection_service`（仅当用户已配置）。

## 操作定义

- **search call**：一次网页搜索或一次抓取指定 URL。每个不同查询或 URL = 1 次。
- **results_found**：返回条数。
- **results_useful**：实际写入交付物（被引用或进入名单）的条数。
- **success**：`results_found > 0` 且至少 1 条 useful。有结果但全不相关 = 不成功。
- **cycle**：一次方法 skill 执行。不是整条获客管线。

## 更新规则

每次方法 skill 执行后：

1. 从交付物「搜索日志」追加 `observations.search_effectiveness`。
2. 同时递增 global 与 `by_skill[current_skill]` 成功率。
3. 追加 `skill_quality`：审查分 + 用户裁决。
4. `cycle_count += 1`。

公司/联系人发现后：更新 `icp_effectiveness`（哪个 ICP 真正产出名单、哪些术语有效）。

教学对比产生的 `comparison_gap` **不得**流入 `next_experiments`。下一轮建议只来自 `search_effectiveness`、`capability_success_rates_by_skill`、`icp_effectiveness`。

## 裁剪

- 文件超过约 500KB：先汇总再删原始条目。
- 每 3 个 cycle：把早于最近 3 个 cycle 的 `search_effectiveness` 滚成按术语的平均值，然后删原始行。
- `icp_effectiveness`：不裁（体量由 ICP 数封顶）。
- `skill_quality`：保留最近 30 条，更早的改成平均。

## 模式提取

每 3 个 cycle，或用户要求改进搜索策略时（打开 `skills/marketing-evolve/SKILL.md` 若存在，否则 inline）：

最低样本：不足 3 次观察的项标「数据不足」，不进排名。

1. 按 `results_useful / results_found` 给搜索词排序。
2. 按 skill 给能力成功率排序。
3. 按 `companies_found + contacts_found` 给 ICP 排序（须来自至少 2 个 skill）。
4. 汇总抓取失败的域名，下次对这些域名优先换查询或请用户接手。

写入 `models`。

## 下一轮实验

只读 `models`，不读教学对比。

1. 基于表现最好的术语提出变体（至少 3 次观察）。
2. 某能力对某 skill 成功率低于 50%（且至少 3 次）→ 建议降级该能力。
3. 某 ICP 两轮仍 0 家公司 → 建议降权。
4. 某组域名抓取失败率高于 30% → 建议改查询或人工接手，不编造页面。

写入 `next_experiments`。编排器在下一次执行前若该文件存在，把 `search_terms_to_try` 交给方法 skill。
