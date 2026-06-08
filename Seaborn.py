import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('/content/sample_data/anscombe.json')
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='X', y='Y', hue='Series', style='Series', s=100)
plt.title('Scatter Plot of Anscombe\'s Quartet')
plt.xlabel('X-value')
plt.ylabel('Y-value')
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
sns.displot(data=df, x='Y', col='Series', kde=True, bins=5, height=4, aspect=1.2)
plt.suptitle('Distribution of Y for Each Dataset', y=1.02)
plt.show()
