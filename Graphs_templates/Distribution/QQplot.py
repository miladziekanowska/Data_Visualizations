import statsmodels.api as sm
from scipy.stats import zscore
import pylab
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the dataset
df = sns.load_dataset('mpg')

# Values in the dataset need to be normalized in this method
numeric_cols = df.select_dtypes(include=[np.number]).columns
df = df[numeric_cols].apply(zscore)

# Extract the displacement column
displacement = df['displacement']

# Draw the plot
sm.qqplot(displacement, line='45')

# Decorations
plt.title('QQ plot of displacement')
plt.grid(alpha=0.5)


pylab.show()
