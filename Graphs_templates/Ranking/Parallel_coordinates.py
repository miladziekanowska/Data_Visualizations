# libraries
import pandas
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates
import matplotlib.ticker as ticker

# Take the iris dataset 
import seaborn as sns
df = sns.load_dataset('healthexp')
# df = df[(df['Year'] == 1980) | (df['Year'] == 2020)]
df = df.drop(['Spending_USD'], axis=1)
df = df.pivot(index='Country', columns='Year', values='Life_Expectancy')
df = df.reset_index()


# Make the plot
parallel_coordinates(df, 'Country', colormap=plt.get_cmap("Set2"), axvlines=False)
plt.title('Life expectation from 1970 to 2020')
plt.xlabel('Years')
plt.ylabel('Life expectancy')
ax = plt.gca()
ax.xaxis.set_major_locator(ticker.MultipleLocator(base=5))
plt.legend(loc='lower right')
plt.show()

plt.savefig('Parallel_coordinates.png')
