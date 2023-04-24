import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
healthexp = sns.load_dataset('healthexp')
df = healthexp[healthexp['Year'] == 1970]

# Bar Chart
ax = sns.barplot(df, x=df['Country'], y=df['Spending_USD'])
ax.bar_label(ax.containers[0], fmt='%.1f')
    
# Decorators
plt.title('Healthcare spendings in 1970', pad=20)
plt.xlabel('Countries')
plt.ylabel('Spendings (USD)')
plt.grid(alpha=0.5)

plt.savefig('Bar_chart_sns.png')