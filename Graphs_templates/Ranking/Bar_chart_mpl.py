import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
healthexp = sns.load_dataset('healthexp')
df = healthexp[healthexp['Year'] == 1970]

fig, ax = plt.subplots(facecolor='white', dpi= 80)
ax.vlines(x=df.Country, ymin=0, ymax=df.Spending_USD, alpha=0.9, linewidth=20)

# Annotate Text
for i,j in zip(df['Country'],df['Spending_USD']):
    ax.annotate(str(j),xy=(i,j), 
                horizontalalignment='center',
                bbox={'fc':'white', 'alpha': 0.7})
    
# Decorators
ax.set_title('Healthcare spendings in 1970', pad=20)
ax.set_xlabel('Countries')
ax.set_ylabel('Spendings (USD)')
ax.grid(alpha=0.5)

plt.savefig('Bar_chart_mpl.png')