# There are so many different graphs
While we create a lot of code, analyze datasets and wish to predict something from them, we might have a more 
visual grasp on the data, since with just number, it might be harder to spot some dependecies between them.

While when we are doing the standard EDA and firstly try to understand the dataset, we already might come up with
some relations between the data:
- if the inflation is higher, so are the prices;
- most of the students might be choosing an university closest to their home;
- the prices in one neighborhood are much more similar to the one's close and not across the town.

While we might come up with some of these assumptions, and in many cases, they might be accurate,
with visualisation it will be even easier for us to spot the unexpected dependencies or better see the patterns,
that might not cross our head while getting to know the dataset. 

This also becomes more important when we are deliberating on what statistical or mathematical method to use for some
machile learning algorithms and using which data with the others will give us the most optimal result we are looking for.

Graphs are there to help.

However, as many as there are scientific methods, there are even more graphs. Therefore it is important to know, which 
graphs to use in which situations and to show which expected dependencies. 

This note and parts of the code in the samples are inspired by [this](https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/) article and [this](https://www.python-graph-gallery.com) website :)

In this markdown I will go through different types of graphs, using similar systematics as in the article and divide it into seven categories.

## Correlation dependencies
With correlation we are trying to present how two different variables/values/columns relate. Just like with the prices getting higher with the inflation, or the drop of jackets sales when the temperature rises, we can determine if change of one variable will influence the other one. 

When speaking out correlation, we need to know, that correlation falls in range of <-1, 1> and we can differenciate negative correlation, when the value is close or equals -1 (one of the variables rises when the other one drops) and positive correlation, the closer the value is to 1 (when one variable rises the other does too). The closed the correlation is to 0, then there is no correlation between these two variables.

Another elemnent we need to note with correlation is so-called line of best fit. The line shows, how the perfect correlation for the mentioned two variables would look like. Of course, when working with real-life examples, most often we will not get a perfect correlation, but the closer most of the values are to the line of best fit, we are able to assume the correlation between these two variables. Similarly as with no correlation being a 0, if the line is straight or strange looking - there is no correlation.

We can also speak about the strenght of correlation, when speaking about how close the dots on the scattered plot are to the line of best fit:
- if they are really close - the correlation is strong;
- if they are kinda close - the correlation is moderate;
- if they aren't very close - the correlation is weak.  
This works both on positive and negative correlation.

For this repository, we will consider three different types of correlation graphs:
1. **Scattered plot** - which is a basic form of graph to show correlation. When we are presenting different groups from our data, it's best to show each group in different color. IMPORTANT! X and Y in scattered plot cannot be categorical data, since that will not give us much information - is should be numerical data only (best if it's continuous, but with a bigger range of discrete data it could work as well, depening what it means);
2. **Correlogram** - this graph provides us with a matrix representing the correlation between all the columns in a dataset. 
3. **Pairwise plot** - is a favorite in exploratory analysis to understand the relationship between all possible pairs of numeric variables. It is a must have tool for bivariate analysis.

## Deviation