#! /usr/bin/env python3
# latlon.py - This goes and fetches latitude and longitude values provided an
# address.
import pandas
from geopy import Nominatim
from flask import Response
#from IPython.display import HTML

class geoCSV:
    def readfile(self,uploadedfile):
        global df
        df = pandas.read_csv(uploadedfile)
        #df = pandas.read_csv('table.csv')

    # If this fails, tell flask "this ain't following the rules"
    def containsAddress(self):
        try:
            df['Address']
            return True
        except KeyError:
            print('No Address column in the file.')
            return False

    def containsaddress(self):
        try:
            df['address']
            return True
        except KeyError:
            print('No address column was found.')
            return False

    def addingLatLon(self):
        global df
        latitude = []
        longitude = []
        geolocator = Nominatim()
        for index, row in df.iterrows():
            location = geolocator.geocode(row['Address'])
            latitude.append(location.latitude)
            longitude.append(location.longitude)
        df['Latitude'] = latitude
        df['Longitude'] = longitude
        #print(df)

    def newCSV(self):
        global df
        df.to_csv('yourfile.csv')

    def render(self):
        df = pandas.read_csv('yourfile.csv')
        return df.to_html()

handleUpload = geoCSV()
