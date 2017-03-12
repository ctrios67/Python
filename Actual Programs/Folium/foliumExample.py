#! /usr/bin/env python3
# foliumExample.py

import folium

newmap = folium.Map(location=[45.372, -121.697], zoom_start=10, tiles='Stamen Terrain')
folium.Marker(location=[45.3288,-121.6625],popup='Mt. Hood Meadows').add_to(newmap)
folium.Marker(location=[45.3311,-121.7311],popup='Timberlake Lodge').add_to(newmap)
newmap.save('testing.html')
