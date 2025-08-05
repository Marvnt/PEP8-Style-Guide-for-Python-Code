import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker

# Note: Update the file path to your actual Excel file location
hy = pd.read_excel('hyweight.xlsx')  # Updated path for Linux environment
print(hy)
print(hy['weight'].median())
plt.figure(figsize=(10, 6))

# 直方图
sns.histplot(hy['weight'], bins=10, kde=True, color='blue', alpha=0.7)

# 添加标题和标签
plt.title('Distribution of Weights')
plt.xlabel('Weights')
plt.ylabel('Density (%)')

# Option 1: Show x-axis as normal decimal values (no percentage)
# plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x:.2f}'))

# Option 2: Show x-axis as percentages (original format)
# plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x * 100)}%'))

# Option 3: Show x-axis with 2 decimal places and % symbol
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x*100:.1f}%'))

# Option 4: Show x-axis as raw values without any formatting
# (Comment out the xaxis formatter line entirely)

# 格式化 y 轴为百分数
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{int(x * 100)}%'))

# 显示图形
plt.show()