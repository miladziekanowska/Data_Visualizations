import scipy.cluster.hierarchy as shc
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


# Import Data
df = sns.load_dataset('car_crashes')


# Plot
plt.figure(figsize=(16, 10), dpi= 80)  
plt.title("USA car crashes Dendogram", fontsize=22)  
dend = shc.dendrogram(shc.linkage(df[['total', 'speeding', 'alcohol', 'not_distracted']], method='ward'), labels=df.abbrev.values, color_threshold=100)  
plt.xticks(fontsize=12)
plt.show()