# This gist contains a direct connection to a local PostgreSQL database
# called "suppliers" where the username and password parameters are "postgres"

# This code is adapted from the tutorial hosted below:
# http://www.postgresqltutorial.com/postgresql-python/connect/

import psycopg2
import os
import glob2

# Since this is a "connect to DB in one shot to do DB stuff" file, get the SQL statement from the ETL_METADATA folder before connecting to Postgres
# TODO: Fix this! This is initial approach is very stupid but I just want to make sure I remember how this works, it's been awhile.
etl_metadata_dir = os.getcwd().replace("ETL_JOBS", "ETL_METADATA")

# Lazily get the SQL file(s) so we can read from it, and store how many files there are
sql_files = []
for i in glob2.glob(os.path.join(etl_metadata_dir, "*.sql")):
    sql_files.append(i)

num_of_sql_files = len(sql_files)

# Open the files we got, and bring the SQL inside as one long string.
sql_to_execute_1 = ""
with open(sql_files[0], "r") as sql_getter:
    sql_to_execute_1 = sql_getter.read()

sql_to_execute_2 = ""
with open(sql_files[num_of_sql_files - 1], "r") as sql_getter:
    sql_to_execute_2 = sql_getter.read()

print(sql_to_execute_1)
print(sql_to_execute_2)
# Establish a connection to the database by creating a cursor object
# The PostgreSQL server must be accessed through the PostgreSQL APP or Terminal Shell

# conn = psycopg2.connect("dbname=suppliers port=5432 user=postgres password=postgres")

# Or:
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="password",  # Please hack me :)
)

# Create a cursor object
cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute(sql_to_execute_1)
# query_results = cur.fetchall()
# print(query_results)

cur.execute(sql_to_execute_2)
# query_results = cur.fetchall()
# print(query_results)

cur.execute("""SELECT * FROM dev_etl.etl_data_source_tracker""")
query_results = cur.fetchall()
print(query_results)

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()
