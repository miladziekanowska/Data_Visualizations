import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('iris')

# Draw Plot
plt.figure(figsize=(13,10), dpi= 80)
sns.violinplot(x='species', y='sepal_width', data=df, scale='width', inner='quartile')

# Decoration
plt.title('Violin Plot of Sepal Width by Iris Species', fontsize=22)
plt.show()