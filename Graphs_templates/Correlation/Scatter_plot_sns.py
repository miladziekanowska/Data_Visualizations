import matplotlib.pyplot as plt
import seaborn as sns

# let's import a dataset
iris = sns.load_dataset('iris')

# now it's much easier to create the scatterplot
# sns.scatterplot(
#     data=iris, 
#     x='sepal_width', 
#     y='sepal_length', 
#     hue='species'
#     )


# however, if we wish to show the line of best fit, we cannot use scatterplot();
# instead we will use the following:

sns.lmplot( 
    data=iris, 
    x='sepal_width', 
    y='sepal_length', 
    hue='species'
    )

# decorations
plt.title('Scatterplot of sepal widths and special lenght for species in Iris')
plt.xlabel('Sepal width (mm)')
plt.ylabel('Sepal lenght (mm)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.savefig('Scattered_plot_sns.png')