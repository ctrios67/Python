#! /usr/bin/env python3
# latlon.py - This goes and fetches latitude and longitude values provided an
# address.
import pandas
from geopy import Nominatim
#from flask import Response
#from IPython.display import HTML

class geoCSV:
    def readfile(self,uploadedfile):
        global df
        df = pandas.read_csv(uploadedfile, index_col=0)
        #df = pandas.read_csv('sample.csv')

    # If this fails, tell flask "this ain't following the rules"
    def containsAddress(self):
        # lowerUpper is 0 if Address is a column, 1 if its address
        global lowerUpper
        # Both existing comes first in order to notify the user immediately
        # otherwise it would erroneously process the file
        if( (('address') in df.columns) and (('Address') in df.columns) ):
            return False
        elif ('Address') in df.columns:
            lowerUpper = 0
            return True
        elif ('address') in df.columns:
            lowerUpper = 1
            return True
        else:
            #print('No address column was found.')
            return False

    def addingLatLon(self):
        global df
        global lowerUpper
        latitude = []
        longitude = []
        geolocator = Nominatim()
        if(lowerUpper==0):
            for index, row in df.iterrows():
                location = geolocator.geocode(row['Address'])
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        else:
            for index, row in df.iterrows():
                location = geolocator.geocode(row['address'])
                latitude.append(location.latitude)
                longitude.append(location.longitude)
        df['Latitude'] = latitude
        df['Longitude'] = longitude
        #print(df)

    # This generates the new file with the new columns, but this may actually
    # not even be necessary.
    def newCSV(self):
        global df
        df.to_csv('yourfile.csv')

    # This is the least painful way to generate our new CSV file additions
    # Within the browser. This converts it into an HTML table.
    def render(self):
        global df
        # I am embarassed by the amount of time it took me to figure out how to
        # pass a CSS class to the genrated HTML table....
        return df.to_html(classes='download')

handleUpload = geoCSV()
