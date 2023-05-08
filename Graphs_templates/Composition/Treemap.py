import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify 


# Import Data
df_raw = sns.load_dataset('healthexp')

# Prepare Data
df = df_raw.groupby('Country').size().reset_index(name='counts')
labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
sizes = df['counts'].values.tolist()
colors = [plt.cm.Spectral(i/float(len(labels))) for i in range(len(labels))]

# Draw Plot
plt.figure(figsize=(12,8), dpi= 80)
squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

# Decorate
plt.title('Treemap of Country entries in the dataset')
plt.axis('off')
plt.show()