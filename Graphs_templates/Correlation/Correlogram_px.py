import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# let's import a dataset
iris = sns.load_dataset('iris')

# let's create the matrix for correlogram/heatmap
corr = iris.corr(numeric_only=True)

fig = px.imshow(corr, text_auto=True, aspect="auto")
fig.show()

fig.write_image('Correlogram_px.png')
