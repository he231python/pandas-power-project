import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

df=pd.read_csv("D:/项目/venv/简单负荷数据.csv")
print("数据预览:")
print(df.head())

print("\n统计结果:")
print(f"平均负荷:{df['负荷'].mean():.1f}mw")
print(f"最大负荷:{df['负荷'].max()}mw")
print(f"最小负荷:{df['负荷'].min()}mw")

plt.figure(figsize=(8,4))
plt.plot(df["日期"],df["负荷"],marker='o',color='red')
plt.title("一周负荷曲线")
plt.xlabel("日期")
plt.ylabel("负荷(mw)")
plt.grid(True)
plt.show()