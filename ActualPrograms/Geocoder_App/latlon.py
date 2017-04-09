#! /usr/bin/env python3
# latlon.py - This goes and fetches latitude and longitude values provided an
# address.
import pandas
from geopy import Nominatim
from flask import Response
from IPython.display import HTML
#from backend import upload

def readfile():
    global df
    #df = pandas.read_csv[backend.upload]
    df = pandas.read_csv('table.csv')

# If this fails, tell flask "this ain't following the rules"
def containsAddress():
    try:
        df['Address']
        return True
    except KeyError:
        print('No Address column in the file.')
        return False

def addingLatLon():
    global df
    latitude = []
    longitude = []
    geolocator = Nominatim()
    # Testing with some stuff I already have
    addresses = []
    for index, row in df.iterrows():
        addresses.append(row['Address'])
    for i in range(len(addresses)):
        location = geolocator.geocode(addresses[i])
        latitude.append(location.latitude)
        longitude.append(location.longitude)
    df['Latitude'] = latitude
    df['Longitude'] = longitude
    #print(df)

def newCSV():
    global df
    df.to_csv('yourfile.csv')

def render():
    df = pandas.read_csv('yourfile.csv')
    return HTML(df.to_html())

readfile()
containsAddress()
addingLatLon()
newCSV()
render()
