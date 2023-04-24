import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# let's load the data
df = sns.load_dataset('flights')
x = np.arange(df.shape[0])
y_returns = df.passengers.diff().fillna(0)


# Plot
plt.figure(figsize=(16,10), dpi= 80)
plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] >= 0, facecolor='green', interpolate=True, alpha=0.7)
plt.fill_between(x[1:], y_returns[1:], 0, where=y_returns[1:] <= 0, facecolor='red', interpolate=True, alpha=0.7)



# Decorations
xtickvals = df['year']
plt.gca().set_xticks(x[::12])
plt.gca().set_xticklabels(xtickvals[::12], rotation=90, fontdict={'horizontalalignment': 'center', 'verticalalignment': 'center_baseline'})
plt.xlim(1,100)
plt.title("Changes in monthly flight passengers", fontsize=22)
plt.ylabel('Monthly passengers difference')
plt.grid(alpha=0.5)
plt.show()

plt.savefig('Area_BarChart_mpl.png')