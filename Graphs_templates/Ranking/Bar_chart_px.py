import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# let's import a dataset
healthexp = sns.load_dataset('healthexp')
df = healthexp[healthexp['Year'] == 1970]

# Bar Chart
fig = px.bar(df, x='Country', y='Spending_USD', text_auto='.2s', title='Healthcare spendings in 1970')
fig.show()

fig.write_image('Bar_chart_px.png')
