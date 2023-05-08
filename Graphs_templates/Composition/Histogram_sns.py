# importing the required library
import seaborn as sns
import matplotlib.pyplot as plt
 
# read a titanic.csv file
# from seaborn library
df = sns.load_dataset('titanic')
 
 
# who v/s fare barplot
sns.barplot(x = 'who',
            y = 'fare',
            hue = 'class',
            data = df,
            palette = "Blues")
 
# Show the plot
plt.show()