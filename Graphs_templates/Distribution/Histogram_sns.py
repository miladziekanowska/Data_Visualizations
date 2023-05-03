import matplotlib.pyplot as plt
import seaborn as sns

# Import the data

df = sns.load_dataset('mpg')

# Draw the plot

sns.histplot(data=df, y='displacement', kde=True) # kde is our line representation of histogram

plt.title('Displacement histogram')
plt.xlabel('Displacement value')
plt.ylabel('Count')
ax = plt.gca()
plt.show()

plt.savefig('Histogram_sns.png')