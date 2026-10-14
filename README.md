# 🍔 mcd-insider 麦门终极特工 (McDonald's AI Agent Skill)

> **2026 麦当劳程序员创意开发大赛（M-CODE 挑战赛）参赛开源项目**  
> 深度集成麦当劳官方 MCP（Model Context Protocol）与运筹优化算力的全能内线助手。

[![MCP Compatible](https://img.shields.io/badge/MCP-StreamableHTTP-FFBC0D?logo=mcdonalds&logoColor=DA291C)](https://open.mcd.cn/mcp)
[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## ⚡ 30 秒快速看懂 mcd-insider

很多 AI 点餐助手只是一个“能查菜单的问答壳子”。  
**`mcd-insider` 是一个真正具有时间感知、运筹算力与极客玩梗文化的麦门内线特工（代号：00M）：**

- **⏰ 时间线绝杀**：全国首创**时钟感知型 Agent**，在 10:10~10:28 临界时段自动启动军事化战备流，压哨锁死 9.9 早餐麦满分！
- **🍦 民间特调拆解**：内置 14+ 绝密暗网配方（阿芙佳朵派、摇摇乐、生酮肉饼塔、雪里红），将非标 DIY 意图自动映射为官方标准 SKU + 组装指南。
- **🧮 运筹约束求解**：不只算最便宜，更算最适合！支持复合约束（“预算 ≤20 元、蛋白质 ≥25g、避开油炸、低糖”），一键给出全局最优解。
- **🎲 趣味交互闭环**：自带选择困难症老虎机轮盘盲抽、多人拼单精准 AA 算力、吃麦历史战报分析。

---

## 🏛️ 系统架构与工具拓扑

```mermaid
flowchart TD
    User([用户自然语言意图]) --> Insider[mcd-insider 特工核心 (代号 00M)]
    
    %% 时间感知
    Insider --> TimeProbe{调用 now-time-info 校验时钟}
    TimeProbe -- "10:10~10:28 临界时段" --> ProtocolA[🚨 10:29 早餐压哨绝杀协议]
    TimeProbe -- "常规时段" --> IntentRouter{意图多路研判}
    
    %% 意图分流
    IntentRouter -- "特定吃法 / DIY特调" --> ProtocolB[🍦 recipes.md 暗网特调工坊]
    IntentRouter -- "穷鬼省钱 / 凑单满减" --> ProtocolC[💰 Greedy Budget 贪心套利]
    IntentRouter -- "控卡 / 增肌 / 特殊禁忌" --> ProtocolD[🧮 多维约束运筹求解器]
    IntentRouter -- "不知道吃啥 / 盲抽" --> ProtocolE[🎰 选择困难症老虎机轮盘]
    IntentRouter -- "办公室下午茶 / 宿舍拼单" --> ProtocolF[👨‍👩‍👧‍👦 团队拼单 & AA 账单均摊]

    %% MCP 调度中枢
    subgraph Official_MCP [麦当劳官方 MCP 原子能力层]
        T1[auto-bind-coupons / 全量一键领券]
        T2[query-my-account & mall-points / 积分穿透]
        T3[list-nutrition-foods / 全量营养素大表]
        T4[query-meals & meal-detail / 菜单与定制选项]
        T5[calculate-price / 价格优惠核算]
        T6[create-order / 写入下单通道]
    end

    ProtocolA --> Official_MCP
    ProtocolB --> Official_MCP
    ProtocolC --> Official_MCP
    ProtocolD --> Official_MCP
    ProtocolE --> Official_MCP
    ProtocolF --> Official_MCP

    Official_MCP --> SafeCard[🍔 输出特工出击确认卡 / 严格人工授权防误触]
```

---

## 💬 经典实战交互示例 (Interactive Scenarios)

### 场景 1：10:23 早餐压哨绝杀（极速军事化战备流）
> **用户**：“刚起，快帮我抢份早餐！”  
> **mcd-insider 特工**：  
> `🚨 特工警报！离 10:30 早餐系统切换仅剩 7 分钟！`  
> `已自动为您执行 auto-bind-coupons，锁定当期 9.9 早餐特惠券。`  
> `【已装填方案】：吉士蛋麦满分 + 现磨鲜煮咖啡（实付 ¥9.9，原价 ¥19.0）`  
> `【空投地址】：北京市海淀区中关村南大街 XX 号 (默认地址)`  
> `👉 回复「出击」立刻提交打单！`

### 场景 2：民间隐藏特调点单（阿芙佳朵派）
> **用户**：“我想吃小红书那个阿芙佳朵派！”  
> **mcd-insider 特工**：  
> `收到！已调取绝密特调档案 [RECIPE-01: 阿芙佳朵派]。`  
> `正在逆向拆解官方组件：`  
> `1. 奥利奥麦旋风 ×1（甜品卡券抵扣后 ¥11.0）`  
> `2. 经典香脆苹果派 ×1（¥8.5）`  
> `3. McCafé 浓缩咖啡 (Espresso) ×1（积分商城 0 元兑换）`  
> `【食用秘籍】：苹果派趁烫折成两段插入麦旋风，淋上浓缩咖啡，冷热交融口感绝杀！`  
> `实付 ¥19.5（原价 ¥28.5，立省 ¥9.0）。确认下单吗？`

### 场景 3：多维硬性约束求解（减脂高蛋白无油炸）
> **用户**：“预算 20 块钱以内，蛋白质必须大于 25 克，而且坚决不吃油炸！”  
> **mcd-insider 特工**：  
> `运筹求解中... 已扫描全量营养成分表 (list-nutrition-foods)。`  
> `锁定绝对最优解：`  
> `🍔 【1+1 随心配】双层吉士汉堡 (非油炸牛肉饼) + 锡兰红茶`  
> `📊 营养审计：蛋白质 26.1g (达标) | 热量 450 kcal | 碳水 34.5g | 0 额外游离糖`  
> `💰 资金核算：实付 ¥13.9（预算剩余 ¥6.1），每元蛋白质比高达 1.88g/元！`

### 场景 4：选择困难症老虎机
> **用户**：“今天不知道吃啥，随便摇一个！”  
> **mcd-insider 特工**：  
> `🎰 麦门特工轮盘疯狂旋转中...`  
> `[ 🍔 麦香鱼 ] - [ 🍟 现炸热薯条 ] - [ 🥤 经典零度可乐 ]`  
> `🎉 恭喜命中今日特工盲盒：【深海清爽三件套】！`  
> `原价 ¥35.0，套用随心配与会员券后仅需 ¥18.9。不满意可回复「再摇一次」！`

---

## 📁 目录文件清单

```text
mcd-insider/
├── SKILL.md                  # 核心 Skill 规则与作战规范（支持 Claude / Antigravity / Cursor）
├── recipes.md                # 麦门暗网绝密配方库（包含 14+ 热门民间特调与组装指南）
├── mcp_config.json           # 官方 MCP Server 标准配置文件模版
├── mcd_budget_optimizer.py   # 多维约束求解器、穷鬼精算引擎与老虎机脚本（含 CLI 支持）
└── README.md                 # 项目文档与评审指南
```

---

## 🚀 极速部署指南

### 1. 配置 MCP Server
将 `mcp_config.json` 中的配置复制到你的 Agent 配置文件中（如 Cursor 的 `mcp.json` 或 Antigravity 的 `mcp_config.json`）：
```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_TOKEN"
      }
    }
  }
}
```
> *Token 获取途径：在麦当劳开放平台 [open.mcd.cn/mcp](https://open.mcd.cn/mcp) 登录即可申请。*

### 2. 部署 Skill
将 `SKILL.md` 与 `recipes.md` 拷贝到你的工作区目录：
- `.agents/skills/mcd-insider/` 或
- `~/.gemini/config/skills/mcd-insider/`

### 3. 本地离线引擎快速测试 (无需 Token 亦可试玩)
本项目自带独立的 Python 运筹约束求解器，可脱机离线运行：
```bash
# 1. 运行多维约束求解测试
python mcd_budget_optimizer.py --budget 20 --min-protein 25 --no-fried

# 2. 启动选择困难症老虎机盲抽
python mcd_budget_optimizer.py --spin

# 3. 查看全局穷鬼套利天梯榜
python mcd_budget_optimizer.py
```

---

## 🏅 参赛与致谢

- **大赛**：2026 麦当劳程序员创意开发大赛 (M-CODE 挑战赛)
- **主办方**：麦当劳中国 (M-China) × 腾讯 WorkBuddy
- **开源协议**：MIT License
