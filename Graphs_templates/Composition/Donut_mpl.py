# library
import matplotlib.pyplot as plt

# create data
size_of_groups=[12,11,3,30]

# Create a pieplot
plt.pie(size_of_groups, labels=size_of_groups)

# add a circle at the center to transform it in a donut chart
my_circle=plt.Circle( (0,0), 0.5, color='white')
p=plt.gcf()

plt.title('Donut plot')
p.gca().add_artist(my_circle)

plt.show()