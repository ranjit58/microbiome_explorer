#!/usr/bin/python

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","0256","microbiome_explorer" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = """LOAD DATA LOCAL INFILE '/users/ranveerk/documents/runs.txt' INTO TABLE runs LINES TERMINATED BY '\r\n';"""

try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
