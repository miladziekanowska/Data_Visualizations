import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

# let's load the data
diamonds = sns.load_dataset('diamonds')

# and prepare it
df = diamonds.groupby('color').sum(numeric_only=True)
x = df.loc[:, ['price']]
df['s_price'] = (x - x.mean())/x.std() # here we standardize the price
df['colors'] = ['red' if x < 0 else 'green' for x in df['s_price']] # and assign the rules we will follow
df.sort_values('s_price', inplace=True)
df.reset_index(inplace=True)

# Draw plot
sns.barplot(data=df,
            x=df['s_price'], 
            y=df['color']
            )

# Decorations
plt.title('Diverging Bars of diamonds\'s price', fontdict={'size':20})
plt.grid(linestyle='--', alpha=0.5)
plt.show()

plt.savefig('Diverging_Bar_sns.png')
