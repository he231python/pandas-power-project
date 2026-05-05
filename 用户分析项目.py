import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取数据
df = pd.read_csv('ecommerce_behavior_data.csv')

# 1. 数据概览
print("数据概览：")
print(df.head())
print("\n数据信息：")
print(df.info())
print("\n描述性统计：")
print(df.describe())

# 2. 定义分析所需的核心指标
total_users = df['user_id'].nunique()
total_products = df['product_id'].nunique()
total_purchases = df[df['event_type'] == 'buy'].shape[0]
conversion_rate = (total_purchases / df.shape[0]) * 100

# 3. 输出分析结果
print(f"总用户数: {total_users}")
print(f"总商品数: {total_products}")
print(f"总购买事件数: {total_purchases}")
print(f"整体转化率（购买事件数/总事件数）: {conversion_rate:.2f}%")

# 定义行为漏斗的关键步骤
funnel_steps = ['pv', 'fav', 'cart', 'buy']
funnel_counts = {}

for step in funnel_steps:
    funnel_counts[step] = df[df['event_type'] == step]['user_id'].nunique()

# 将结果转换为DataFrame用于显示
funnel_df = pd.DataFrame(list(funnel_counts.items()), columns=['step', 'user_count'])
print(funnel_df)