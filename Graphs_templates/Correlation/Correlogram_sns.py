import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
iris = sns.load_dataset('iris')

# let's create the matrix for correlogram/heatmap
corr = iris.corr(numeric_only=True)

sns.heatmap(corr, cmap='coolwarm', annot=True, fmt=',.2f')

plt.title('Correlation of numeric values in Iris dataset')

plt.savefig('Correlogram_sns.png')