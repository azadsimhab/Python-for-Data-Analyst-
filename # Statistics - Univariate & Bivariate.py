#  Univariate 
# 1.Histogram has only one axis
# 2.Box Plot
# 3.Pie Chart

#  Bivariate 
# 1.Bar Plots have 2 axis
# 2.Scatter Plots 
# 3.Line Plots


#  Multivariate Plots
# 1.Stacked Bar Plot
# 2.Multiple Scatterplot
# 3.Multiple Lineplot


import matplotlib.pyplot as plt
from palettable.colorbrewer.qualitative import Pastel1_7

# creat Table
names = [ 'groupA', 'groupB', 'groupC','groupD']
size = [12, 11, 3, 30]

# create a circle at the center of the plot
my_circle = pit.Circle( (0,0), 0.7, color='white')

from palettable.colorbrewer.qualitative import Pastel1_7
plt.pie(size, labels=names,colors=Pastel1_7.hex_colors)
p = plt.gcf()
p.gcs(),add_artist(my_circle)

#show the graph
plt.show()


## Libraries
import matplotlib.pyplot as plt
import squarify #pip install squarify (algorithm for treemap)
import pandas as pd

# create a dta frame with sample data
df = pd.DataFrame({'nb_people':[8,3,4,2], 'group':["groupA", "groupB", "groupC", "groupD"] })

#plot it
squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=,8 )
plt.axis('off')
plt.show()


#import Pandas
import pandas as pd

## Make a data frame with dots to show on the map

data = pd.DataFrame({
    'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'lat':[-34, 49,-38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'name':['Buenos Aires', 'Paris', 'melborn', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
    'value':[10, 12, 40, 70, 23, 43, 100, 43]
}, dtype=str)

data