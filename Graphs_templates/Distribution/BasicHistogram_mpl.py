import matplotlib.pyplot as plt
import seaborn as sns #  Importing it here for the dataset only

# Import the data
df = sns.load_dataset('mpg')
mean = df['displacement'].mean()                     
                    
                      
                      
# Create the plot
plt.hist(df['displacement'], bins=8, histtype='stepfilled')
plt.axvline(df['displacement'].mean(), color='k', linestyle='dashed', linewidth=1) # creating mean line
plt.text((mean+1),120,' mean') #creating mean label

    
plt.title('Displacement histogram')
plt.xlabel('Displacement value')
plt.ylabel('Count')
ax = plt.gca()
plt.show()

plt.savefig('BasicHistogram.png')