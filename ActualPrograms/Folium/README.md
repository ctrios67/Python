# volcanoLeaflet.py
This is a Python program that generates a leaflet map of the world. This map plots the points
of all the volcanoes located within the United States via grabbing this data from a csv file. This program also colorizes countries based on population numbers (from circa 2005 I believe) from a geojson file. The output can be viewed in Leaflet_Map/testing.html

- Requirement:
	- Generate a leaflet map that plots Volcano locations in the U.S.
	- Colorize countries based on population information from the Leaflet_Map/Shapefile/worldPopulation.geojson file.
- Packages Used:
	- Pandas
	- Folium
- Data Source:
	- Volcano CSV file.
	- World Population geojson file.
	
# myTravels.py
This is a Python program that generates a leaflet map with points of places I have lived in or visited in my travels.
- Requirement:
	- Generate a leaflet map that plots travel locations/residences in the U.S., Canada, & Carribbean.
- Packages Used:
	- Pandas
	- Folium
- Data Source:
	- CSV File.
- Improvement:
	- Call a different program I've made that can open Google Maps when you provide an address, grab the Latitutde and Longitude from that address, and save the results into a CSV file instead of manually making it myself.