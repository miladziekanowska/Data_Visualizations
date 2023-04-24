import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
iris = sns.load_dataset('iris')

sns.pairplot(iris, hue='species')
plt.show()

plt.savefig('Paiwise_sns.png')