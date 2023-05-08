# let's import the liblaries
import numpy as np
import pandas as pd
# import matplotlib as mlp 
import matplotlib.pyplot as plt

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.3, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig, ax = plt.subplots()
ax.pie(sizes,
      labels=labels,
      explode=explode,
      autopct='%1.0f%%')

plt.title('How many -ogs are in the data?', pad=25, fontsize=20)

plt.plot()