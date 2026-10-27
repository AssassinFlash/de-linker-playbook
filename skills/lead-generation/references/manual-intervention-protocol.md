# 人工接手协议

自动化查证或抓取遇到登录、验证码、付费审批或能力缺失时，输出可执行的人机指令，避免「失败即放弃」。

## 使用原则

1. 先说明已完成动作与卡在哪一步（Apify 搜索 / 抓取原文 / 已配置的发现或采集服务）。
2. 明确「需要用户做什么、预计耗时、做完回什么词」。
3. 承诺从当前进度继续，不重头开始。
4. 处理完成后，在交付物写入 `## 阻塞与升级日志`。

## 登录过期

说：

> 需要你接手约 1 分钟：请登录 {platform}，完成后回复 `done`。我会从当前进度继续，不会重头开始。

记录：`blocker_type: login_expired`；`user_help_needed: yes`；`resume_token: done`

## 验证码 / 反爬挑战

说：

> 页面遇到验证码。请在浏览器里手动通过后回复 `done`。我继续提取，不放弃这条线。

记录：`blocker_type: captcha`；`user_help_needed: yes`；`resume_token: done`

## 付费能力审批

说：

> 免费与已配置的本地能力已跑完。下一步是 {capability}，预计成本 {estimate}。回复 `approve paid` 我再继续，否则保留当前结果并标记缺口。

记录：`blocker_type: paid_approval`；`user_help_needed: yes`；`resume_token: approve paid`

## 能力缺失 / 配置缺口

说：

> 当前环境缺少 {missing_capability}。我会先用 Apify 搜索（需要原文时抓取指定 URL）继续；若你补齐后希望走完整链路，回复 `retry full chain`。

记录：`blocker_type: config_gap`；`user_help_needed: optional`；`resume_token: retry full chain`

## 阻塞日志模板

```markdown
## 阻塞与升级日志
| # | Stage | Blocker | Evidence | Next Action | User Needed |
|---|-------|---------|----------|-------------|------------|
| 1 | 抓取原文 | 验证码 | 403 + challenge | 请用户通过后回复 done | yes |
```
