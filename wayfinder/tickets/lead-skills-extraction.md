---
wayfinder: task
status: open
assignee: chesterjohn+agent
blocked_by: [extraction-spec, repo-skeleton]
---

# 43 个 lead skill 抽取改写

## Question

从 `~/Documents/lead-generation_副本/skills/`（canonical，43 个；`.kimi/`、`.codex/` 是适配层不抽）按抽取规格迁入本仓库 `skills/`，裸名统一加 `lead-` 前缀（如 `icp-analysis` → `lead-icp-analysis`）。

执行方式：子代理 swarm，每 skill 一个子代理；按主题分批出 review checkpoint（研究管线/触达邮件/LinkedIn/SEO/售后/meta）。

注意：方法论源自用户自购付费 prompt——自用，不分发；跳过 `config.md`、`product-context.md`、`icp-*.json/xlsx`、`scripts/cookies.txt`、`downloads/` 等一切产品与机器数据。
