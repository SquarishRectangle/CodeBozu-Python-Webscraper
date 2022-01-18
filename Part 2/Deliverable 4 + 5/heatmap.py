import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv("media sentiment by president.csv", index_col=0)
plt.figure(figsize=(12.93, 10.41))
sns.set(font_scale=1)
ax = sns.heatmap(df, cmap ='RdYlGn', linewidths = 0.30, annot = True, vmin=-1)
#ax.figure.tight_layout()
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
plt.savefig("Figure.png")
plt.show()