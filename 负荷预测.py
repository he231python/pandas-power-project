import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import joblib
import os
import sys

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

data_file = "Train.csv"

if not os.path.exists(data_file):
    print(f"错误：找不到文件 {data_file}")
    print("请将数据文件放在当前目录下，或修改 data_file 变量为正确路径。")
    sys.exit(1)

try:
    if data_file.endswith('.xlsx') or data_file.endswith('.xls'):
        df = pd.read_excel(data_file)
    else:
        df = pd.read_csv(data_file)
    print("数据读取成功，前5行如下：")
    print(df.head())
except Exception as e:
    print(f"读取文件失败：{e}")
    sys.exit(1)

required_columns = ['AT', 'PE']
if not all(col in df.columns for col in required_columns):
    print(f"数据中缺少必要的列 {required_columns}，现有列：{list(df.columns)}")
    sys.exit(1)

X = df[['AT']]
y = df['PE']

model = LinearRegression()
model.fit(X, y)

print(f"\n 模型公式：PE = {model.coef_[0]:.2f} × AT + {model.intercept_:.2f}")
print(f" 模型评分 R²：{model.score(X, y):.3f}")

# 生成用于画图的平滑数据
X_plot = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_plot = model.predict(X_plot)

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.3, label='实际数据')
plt.plot(X_plot, y_plot, color='red', linewidth=2, label='拟合直线')
plt.xlabel('温度 (AT)')
plt.ylabel('输出电力 (PE)')
plt.title('温度对输出电力的影响（线性回归）')
plt.legend()
plt.grid(True)

# 预测新温度下的电力
new_temps = [10, 15, 20, 25]
new_X = pd.DataFrame({'AT': new_temps})
predictions = model.predict(new_X)

print('\n 预测结果：')
for temp, pred in zip(new_temps, predictions):
    print(f'   温度 {temp}°C → 预测输出电力 {pred:.1f} MW')

joblib.dump(model, 'load_forecast_model.pkl')
print('\n 模型已保存为 load_forecast_model.pkl')

plt.show()