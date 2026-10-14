# workbuddy.md

本文件是参与腾讯 WorkBuddy 专项奖励所需的开发过程记录与智能体联动说明。

---

## 一、开发环境与智能体配置

| 项目 | 内容 |
|---|---|
| **开发工具** | 腾讯 WorkBuddy (Agent 模式) & Antigravity |
| **开发周期** | 2026-10-10 至 2026-10-14 |
| **项目仓库** | `johamwon/mcd-insider` |
| **开发语言与运行时** | Python 3.9+ (内置纯标准库轻量运筹优化器) |
| **协议标准** | Model Context Protocol (MCP) Streamable HTTP |

### WorkBuddy 自定义连接器配置：
在 WorkBuddy 中配置麦当劳官方 MCP 连接器：
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer ${MCD_MCP_TOKEN}"
      }
    }
  }
}
```

---

## 二、开发过程时间线

| 日期 | 阶段 | 关键产出 |
|---|---|---|
| **10-10** | 创意调研 | 深度分析麦当劳 MCP 开放接口与社区痛点，确定「10:29 早餐绝杀 + 民间特调 + 穷鬼套利」复合特工方向 |
| **10-11** | 核心架构搭建 | 编写初始 `SKILL.md`，构建基于 `mcp_config.json` 的标准连接模版与基础计价模型 |
| **10-13** | 算法设计与自测 | 开发 `mcd_budget_optimizer.py`，实现多维约束求解算法（预算、热量、蛋白质、避开油炸），增加 `--spin` 老虎机盲盒功能 |
| **10-14** | 产品体验跃升 | 建立包含 14+ 款经典与民间爆款的 `recipes.md` 知识库，完成特工人格与双模态语气注入 |
| **10-14** | 官方 MCP 连通性测试 | 在 WorkBuddy / Agent 环境中完成 `auto-bind-coupons`、`query-my-account`、`query-addresses` 真实环境冒烟测试与合规审查 |

---

## 三、WorkBuddy 智能体联动与实操验证

在 WorkBuddy 智能体对话环境中，成功测试并验证了以下闭环链路：

1. **时钟感知冒烟**：调用 `now-time-info` 获取服务器时间，时间窗口正确触发极速战备流；
2. **卡券地毯式扫描**：执行 `auto-bind-coupons` 自动化领取所有麦麦省券，并在 `query-my-coupons` 中查验到账；
3. **资产探测**：通过 `query-my-account` 成功读取用户积分与状态；
4. **约束求解仿真**：通过 `list-nutrition-foods` 调取餐品宏量成分，在 20 元预算下成功求解出兼顾高蛋白与零油炸的最佳组合。
