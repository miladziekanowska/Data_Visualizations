import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.lines as mlines

# let's import a dataset
df = sns.load_dataset('healthexp')
df = df[(df['Year'] == 1980) | (df['Year'] == 2020)]
df = df.drop(['Spending_USD'], axis=1)
df = df.pivot(index='Country', columns='Year', values='Life_Expectancy')
df = df.reset_index()
df = df.rename(columns={1980 : '1980',
                        2020 : '2020'})


left_label = [str(c) + ', '+ str(y) for c, y in zip(df.Country, df['1980'])]
right_label = [str(c) + ', '+ str(y) for c, y in zip(df.Country, df['2020'])]
klass = ['red' if (y1-y2) < 0 else 'green' for y1, y2 in zip(df['1980'], df['2020'])]

# draw line
# https://stackoverflow.com/questions/36470343/how-to-draw-a-line-with-matplotlib/36479941
def newline(p1, p2, color='black'):
    ax = plt.gca()
    l = mlines.Line2D([p1[0],p2[0]], [p1[1],p2[1]], color='red' if p1[1]-p2[1] > 0 else 'green', marker='o', markersize=6)
    ax.add_line(l)
    return l

fig, ax = plt.subplots(figsize=(9,9), dpi= 80)

# Vertical Lines
ax.vlines(x=1, ymin=70, ymax=90, color='black', alpha=0.7, linewidth=1, linestyles='dotted')
ax.vlines(x=3, ymin=70, ymax=90, color='black', alpha=0.7, linewidth=1, linestyles='dotted')

# Points
ax.scatter(y=df['1980'], x=np.repeat(1, df.shape[0]), s=10, color='black', alpha=0.7)
ax.scatter(y=df['2020'], x=np.repeat(3, df.shape[0]), s=10, color='black', alpha=0.7)

# Line Segmentsand Annotation
for p1, p2, c in zip(df['1980'], df['2020'], df['Country']):
    newline([1,p1], [3,p2])
    ax.text(1-0.05, p1, c + ', ' + str(round(p1)), horizontalalignment='right', verticalalignment='center', fontdict={'size':9})
    ax.text(3+0.05, p2, c + ', ' + str(round(p2)), horizontalalignment='left', verticalalignment='center', fontdict={'size':9})

# 'Before' and 'After' Annotations
ax.text(1-0.05, 86, 'BEFORE', horizontalalignment='right', verticalalignment='center', fontdict={'size':12, 'weight':500})
ax.text(3+0.05, 86, 'AFTER', horizontalalignment='left', verticalalignment='center', fontdict={'size':12, 'weight':500})

# Decoration
ax.set_title("Life expectancy 1980 vs. 2020", fontdict={'size':22}, pad=20)
ax.set(xlim=(0,4), ylim=(70,86), ylabel='Life expectancty in years')
ax.set_xticks([1,3])
ax.set_xticklabels(["1980", "2020"])
plt.yticks(np.arange(70, 86, 3), fontsize=12)

# Lighten borders
plt.gca().spines["top"].set_alpha(.0)
plt.gca().spines["bottom"].set_alpha(.0)
plt.gca().spines["right"].set_alpha(.0)
plt.gca().spines["left"].set_alpha(.0)
plt.show()

plt.savefig('Slope_chart.png')