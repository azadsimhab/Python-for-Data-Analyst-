import pandas as pd

## Make a data frame with dots to show on the map

data = pd.DataFrame({
    'lon':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'lat':[-34, 49,-38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'name':['Buenos Aires', 'Paris', 'melborn', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
    'value':[10, 12, 40, 70, 23, 43, 100, 43]
}, dtype=str)

print(data)

for i in range(0,len(data)):
    folium.marker(
        location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
        popup=data.iloc[i]['name'],
    ).add_to(m)
    
    
    #make a empty map 
    =folium.map(location[20,0], tiles="OpenStreetMap", zoom_start=2)
    
    ##show the map again
    
