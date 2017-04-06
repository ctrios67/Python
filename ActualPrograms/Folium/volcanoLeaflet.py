#! /usr/bin/env python3
# foliumExample.py

import folium
import os
import pandas

# Making this relative incase this is ever cloned by someone.
os.chdir('./Leaflet_Webmap/')
print(os.getcwd())
df = pandas.read_csv('Volcanoes-USA.txt')

newmap = folium.Map(location=[0, 0], zoom_start=4, tiles='Mapbox Bright') #Stamen Terrain tile shows volcanoes better

def color(elev):
    # For color:
    # icon=folium.Icon(color='color')
    minimum = int(min(df['ELEV']))
    step = int((max(df['ELEV'])-min(df['ELEV']))/3)
    # maximum = max(df['ELEV'])
    if elev in range(minimum,minimum+step):
        col = folium.Icon(color='green')
    elif elev in range(minimum+step,minimum+step*2):
        col = folium.Icon(color='orange')
    else:
        col = folium.Icon(color='red')
    return col

fg = folium.FeatureGroup(name='Volcano Locations')

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    folium.Marker(location=[lat,lon],popup=name, icon=color(elev)).add_to(fg)
    #fg.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color=color(elev),icon_color='green')))

newmap.add_child(fg)

newmap.add_child(folium.GeoJson(data=open('Shapefile/untitled.geojson', encoding='utf-8'),
                                name='World Population',
                                style_function = lambda x:{'fillColor':'green' if x['properties']['POP2005']<=10000000 else 'orange' if 10000000<x['properties']['POP2005'] < 20000000 else 'red'}))

newmap.add_child(folium.LayerControl())

newmap.save(outfile='testing.html')
