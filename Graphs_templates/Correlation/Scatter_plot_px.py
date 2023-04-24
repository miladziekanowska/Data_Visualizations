import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# let's import a dataset
iris = sns.load_dataset('iris')

# it's also very easy using plotly, and let's include the best fit line as well

fig = px.scatter(iris,
                 x='sepal_width', 
                 y='sepal_length',
                 color='species',
                 trendline='ols'
                 )

# the trendline requires module statsmodels to be installed

fig.show()
plt.savefig('Scatter_plot_px.png')
