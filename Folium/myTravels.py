#! /usr/bin/env python3
# foliumExample.py

import folium
import os
import pandas

# This program runs assuming it is located in the same folder
df = pandas.read_csv('travelLocations.csv')
newmap = folium.Map(location=[37.686650, -98.096398], zoom_start=4, tiles='OpenStreetMap') #Stamen Terrain tile shows volcanoes better

def color():
    col = folium.Icon(color='red')
    return col

for lat,lon,city,state,country in zip(df['LATITUDE'],df['LONGITUDE'],df['CITY'],df['STATE'],df['COUNTRY']):
    name = city+ ', ' + state + ', ' + country
    newmap.add_child(folium.Marker(location=[lat,lon],popup=name, icon=folium.Icon(color=color())))
    #folium.Marker(location=[lat,lon],popup=name, icon=color()).add_to(newmap)

newmap.save(outfile='travels.html')
