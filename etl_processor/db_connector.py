#!/usr/bin/env python3

import psycopg2
import csv
import pandas
import os
import datetime as dt

def get_file_path():
    return os.path.join(os.sep, 'home', 'chin', 'Local_File_Repo')

def is_file_path_valid():
    return os.path.exists(get_file_path())

# TODO: Re-write this to make use of the parameter table. Also, figure out how
# in the hell to fill in the metadata parameters from the parameter table.
if is_file_path_valid():
    conn = psycopg2.connect('host = localhost dbname=DEV_POSTGRES user=etl_chin password=Christian')
    cur = conn.cursor()
    cur.execute('SELECT * FROM etl.ws_etl_data_parameters')
    one = cur.fetchone()
    all_rows = cur.fetchall()

    # Super inefficient way of loading a CSV file.
    with open(os.path.join(get_file_path(),'For_Hire_Vehicles__FHV__-_Active_Drivers.csv'), 'r') as file_1:
        data = csv.reader(file_1)
        next(data) # Skip header
        for record in data:
            print(str(record))
            cur.execute("""INSERT INTO etl.ws_opendata_nyc_tlc_fhv_ps
            VALUES (%s, %s, %s, %s, %s, %s, %s)""", record)
    conn.commit()
else:
    print('Oh snap')
