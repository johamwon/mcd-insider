# -*- coding: utf-8 -*-
"""
麦门终极特工 00M - 全局穷鬼套餐与多维约束精算引擎 (Constraint Solver & Budget Optimizer)
支持：
1. 静态穷鬼套利排名（单位元蛋白质、单位元热量、差价套利）
2. 多目标约束求解（给定预算、热量、蛋白质目标求最优组合）
3. 选择困难症老虎机轮盘（随机盲盒抽取）
"""

import sys
import argparse
import random

if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# 全量核心餐品数据库 (名称, 分类, 价格, 热量kcal, 蛋白质g, 脂肪g, 碳水g, 是否油炸, 官方单点原价)
MENU_DATABASE = [
    # 1+1 红区
    {"name": "双层吉士汉堡", "category": "1+1红区", "price": 0, "kcal": 448, "protein": 26.0, "fat": 23.0, "carb": 34.0, "fried": False, "origin_price": 17.5},
    {"name": "麦香鸡", "category": "1+1红区", "price": 0, "kcal": 380, "protein": 14.2, "fat": 16.0, "carb": 44.0, "fried": True, "origin_price": 13.0},
    {"name": "麦香鱼", "category": "1+1红区", "price": 0, "kcal": 340, "protein": 15.0, "fat": 13.0, "carb": 40.0, "fried": True, "origin_price": 16.0},
    {"name": "麦乐鸡(5块)", "category": "1+1红区", "price": 0, "kcal": 224, "protein": 13.1, "fat": 13.0, "carb": 14.0, "fried": True, "origin_price": 13.5},
    
    # 1+1 白区
    {"name": "小薯条", "category": "1+1白区", "price": 0, "kcal": 220, "protein": 3.0, "fat": 11.0, "carb": 28.0, "fried": True, "origin_price": 9.0},
    {"name": "菠萝派", "category": "1+1白区", "price": 0, "kcal": 235, "protein": 2.2, "fat": 10.0, "carb": 34.0, "fried": True, "origin_price": 8.5},
    {"name": "迷你草莓新地", "category": "1+1白区", "price": 0, "kcal": 185, "protein": 4.1, "fat": 5.0, "carb": 31.0, "fried": False, "origin_price": 10.0},
    {"name": "零度可乐(中)", "category": "1+1白区", "price": 0, "kcal": 0, "protein": 0.0, "fat": 0.0, "carb": 0.0, "fried": False, "origin_price": 9.5},
    {"name": "锡兰红茶", "category": "1+1白区", "price": 0, "kcal": 2, "protein": 0.1, "fat": 0.0, "carb": 0.5, "fried": False, "origin_price": 9.5},
    
    # 常规精选与特惠单品
    {"name": "板烧鸡腿堡", "category": "常规主食", "price": 23.0, "kcal": 401, "protein": 21.6, "fat": 17.5, "carb": 39.0, "fried": False, "origin_price": 23.0},
    {"name": "巨无霸", "category": "常规主食", "price": 25.5, "kcal": 515, "protein": 26.5, "fat": 26.0, "carb": 43.0, "fried": False, "origin_price": 25.5},
    {"name": "周一会员特惠麦辣鸡腿堡", "category": "特惠主食", "price": 10.0, "kcal": 490, "protein": 22.8, "fat": 24.0, "carb": 46.0, "fried": True, "origin_price": 22.0},
    {"name": "吉士蛋麦满分两件套(含咖啡)", "category": "早餐特惠", "price": 9.9, "kcal": 320, "protein": 18.5, "fat": 14.0, "carb": 28.0, "fried": False, "origin_price": 19.0},
    {"name": "玉米杯(小)", "category": "轻食小食", "price": 8.0, "kcal": 70, "protein": 2.5, "fat": 1.0, "carb": 14.0, "fried": False, "origin_price": 8.0},
    {"name": "纯牛奶(盒)", "category": "饮品", "price": 10.0, "kcal": 130, "protein": 6.8, "fat": 7.0, "carb": 10.0, "fried": False, "origin_price": 10.0},
]

PRICE_1_PLUS_1 = 13.9

def get_all_combinations():
    """生成所有可用的点餐组合候选池"""
    combos = []
    reds = [item for item in MENU_DATABASE if item["category"] == "1+1红区"]
    whites = [item for item in MENU_DATABASE if item["category"] == "1+1白区"]
    
    # 1. 单套 1+1 随心配
    for r in reds:
        for w in whites:
            combos.append({
                "type": "1+1随心配",
                "name": f"【1+1】{r['name']} + {w['name']}",
                "items": [r["name"], w["name"]],
                "price": PRICE_1_PLUS_1,
                "kcal": r["kcal"] + w["kcal"],
                "protein": round(r["protein"] + w["protein"], 1),
                "fat": round(r["fat"] + w["fat"], 1),
                "carb": round(r["carb"] + w["carb"], 1),
                "has_fried": r["fried"] or w["fried"],
                "origin_price": r["origin_price"] + w["origin_price"],
                "saved": round((r["origin_price"] + w["origin_price"]) - PRICE_1_PLUS_1, 1)
            })
            
    # 2. 特惠单品
    for item in MENU_DATABASE:
        if item["category"] in ["特惠主食", "早餐特惠"]:
            combos.append({
                "type": item["category"],
                "name": f"【{item['category']}】{item['name']}",
                "items": [item["name"]],
                "price": item["price"],
                "kcal": item["kcal"],
                "protein": item["protein"],
                "fat": item["fat"],
                "carb": item["carb"],
                "has_fried": item["fried"],
                "origin_price": item["origin_price"],
                "saved": round(item["origin_price"] - item["price"], 1)
            })
            
    # 3. 双份 1+1 交叉重组
    combos.append({
        "type": "双份1+1大满贯",
        "name": "【双份1+1四件套】双吉 + 麦香鸡 + 小薯条 + 零度可乐",
        "items": ["双层吉士汉堡", "麦香鸡", "小薯条", "零度可乐(中)"],
        "price": PRICE_1_PLUS_1 * 2,
        "kcal": 448 + 380 + 220 + 0,
        "protein": round(26.0 + 14.2 + 3.0 + 0, 1),
        "fat": round(23.0 + 16.0 + 11.0, 1),
        "carb": round(34.0 + 44.0 + 28.0, 1),
        "has_fried": True,
        "origin_price": 17.5 + 13.0 + 9.0 + 9.5,
        "saved": round((17.5 + 13.0 + 9.0 + 9.5) - (PRICE_1_PLUS_1 * 2), 1)
    })
    
    # 4. 减脂高蛋白轻食组合
    combos.append({
        "type": "纯净健身组合",
        "name": "【极客减脂盒】板烧鸡腿堡(去酱) + 玉米杯 + 纯牛奶",
        "items": ["板烧鸡腿堡", "玉米杯(小)", "纯牛奶(盒)"],
        "price": 23.0 + 8.0 + 10.0,
        "kcal": 360 + 70 + 130,
        "protein": round(21.6 + 2.5 + 6.8, 1),
        "fat": round(12.0 + 1.0 + 7.0, 1),
        "carb": round(35.0 + 14.0 + 10.0, 1),
        "has_fried": False,
        "origin_price": 41.0,
        "saved": 0.0
    })
    
    return combos

def solve_constraints(budget=None, max_kcal=None, min_protein=None, no_fried=False):
    """根据多重条件求解满足约束的最佳方案"""
    combos = get_all_combinations()
    filtered = []
    
    for c in combos:
        if budget is not None and c["price"] > budget:
            continue
        if max_kcal is not None and c["kcal"] > max_kcal:
            continue
        if min_protein is not None and c["protein"] < min_protein:
            continue
        if no_fried and c["has_fried"]:
            continue
        filtered.append(c)
        
    # 排序标准：优先按单位元蛋白质（性价比高），其次按省钱金额
    filtered.sort(key=lambda x: (x["protein"] / x["price"] if x["price"] > 0 else 0), reverse=True)
    return filtered

def spin_wheel():
    """选择困难症轮盘盲盒抽取"""
    combos = get_all_combinations()
    chosen = random.choice(combos)
    return chosen

def main():
    parser = argparse.ArgumentParser(description="麦门终极特工 00M 穷鬼套餐与约束求解算力引擎")
    parser.add_argument("--budget", type=float, help="预算上限 (元)")
    parser.add_argument("--max-kcal", type=float, help="热量上限 (kcal)")
    parser.add_argument("--min-protein", type=float, help="蛋白质下限 (g)")
    parser.add_argument("--no-fried", action="store_true", help="严格避开油炸食品")
    parser.add_argument("--spin", action="store_true", help="启动选择困难症盲抽老虎机")
    
    args = parser.parse_args()
    
    if args.spin:
        res = spin_wheel()
        print("🎰 麦门特工轮盘疯狂旋转中...")
        print(f"🎉 盲盒命中：{res['name']}")
        print(f"💰 实付单价：¥{res['price']} (官方标价：¥{res['origin_price']}，立省 ¥{res['saved']})")
        print(f"📊 宏量营养：热量 {res['kcal']} kcal | 蛋白质 {res['protein']}g | 脂肪 {res['fat']}g | 碳水 {res['carb']}g")
        return
        
    if args.budget or args.max_kcal or args.min_protein or args.no_fried:
        print(f"🎯 正在执行多维约束求解：[预算 <= {args.budget}元, 热量 <= {args.max_kcal}kcal, 蛋白质 >= {args.min_protein}g, 避开油炸={args.no_fried}]")
        results = solve_constraints(args.budget, args.max_kcal, args.min_protein, args.no_fried)
        if not results:
            print("❌ 未搜索到同时满足全部严苛约束的组合，建议适当放宽预算或热量限制！")
        else:
            print(f"✅ 成功锁定 {len(results)} 个合格方案，推荐 TOP 3：\n")
            for idx, r in enumerate(results[:3], 1):
                p_rate = round(r["protein"] / r["price"], 2) if r["price"] > 0 else 0
                print(f"{idx}. {r['name']}")
                print(f"   实付: ¥{r['price']} | 蛋白质性价比: {p_rate}g/元")
                print(f"   热量: {r['kcal']} kcal | 蛋白质: {r['protein']}g | 碳水: {r['carb']}g | 含有油炸: {'是' if r['has_fried'] else '否'}\n")
        return

    # 默认模式：打印全局穷鬼排行榜
    print("=== 麦门 1+1 随心配全局套利排行 (单位元蛋白质 TOP 3) ===")
    all_combos = [c for c in get_all_combinations() if c["type"] == "1+1随心配"]
    by_protein = sorted(all_combos, key=lambda x: x["protein"] / x["price"], reverse=True)[:3]
    for idx, c in enumerate(by_protein, 1):
        print(f"{idx}. {c['name']} | 每元含蛋白: {round(c['protein']/c['price'], 2)}g | 总蛋白: {c['protein']}g | 实付: ¥{c['price']}")

    print("\n=== 差价套利之王 (让资本家倒贴最多 TOP 3) ===")
    by_saved = sorted(all_combos, key=lambda x: x["saved"], reverse=True)[:3]
    for idx, c in enumerate(by_saved, 1):
        print(f"{idx}. {c['name']} | 官方原价: ¥{c['origin_price']} | 随心配立省: ¥{c['saved']}")

if __name__ == "__main__":
    main()
