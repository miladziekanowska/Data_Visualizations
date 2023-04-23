import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
iris = sns.load_dataset('iris.csv')

# Prepare Data 
# Create as many colors as there are unique midwest['category']
species = np.unique(iris['species'])
colors = ['red', 'pink', 'orange']

# Draw Plot for Each Category
plt.figure(figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

for i, spieces in enumerate(spiecies):
    plt.scatter('sepal_width', 'sepal_length', 
                data=iris.loc[iris.species==species, :], 
                s=20, c=colors[i], label=str(species))

# Decorations

plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='sepal_width', ylabel='sepal_length')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Scatterplot of sepal widths and special lenght for species in Iris", fontsize=22)
plt.legend(fontsize=12)    
plt.show()    
