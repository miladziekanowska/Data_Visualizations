import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
iris = sns.load_dataset('iris')

# let's create the matrix for correlogram/heatmap
corr = iris.corr(numeric_only=True)
corr = corr.round(2)

# now let's generate the correlogram
corr.style.background_gradient(cmap='coolwarm')