#!/usr/bin/python

import cgi,cgitb,MySQLdb,module

cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create table as per requirement
sql = """CREATE TABLE projects
        (run_group VARCHAR(255) NOT NULL PRIMARY KEY,
         user_email VARCHAR(255),
         title VARCHAR(255),
         notes VARCHAR(2000),
         links VARCHAR(2000) )"""

cursor.execute(sql)

sql = """CREATE TABLE runs (
         run_id VARCHAR(255) NOT NULL PRIMARY KEY,
         run_name VARCHAR(255),
         run_date VARCHAR(255),
         run_machine VARCHAR(255),
         run_read_length VARCHAR(255),
         run_mapping VARCHAR(255) )"""

cursor.execute(sql)

# Create table as per requirement
sql = """CREATE TABLE samples (
         run_id VARCHAR(255),
         fwd_sample VARCHAR(255) NOT NULL PRIMARY KEY,
         rev_sample VARCHAR(255),
         sample_name VARCHAR(255) NOT NULL,
         run_group VARCHAR(255),
         user_email VARCHAR(255) )"""

cursor.execute(sql)

# Create table as per requirement
sql = """CREATE TABLE user_details ( user_email VARCHAR(255) NOT NULL PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), department VARCHAR(255),
user_notes VARCHAR(255) )"""

cursor.execute(sql)

# Create table as per requirement
sql = """CREATE TABLE users ( user_email VARCHAR(255) NOT NULL PRIMARY KEY, name VARCHAR(255), department VARCHAR(255),
user_notes VARCHAR(255) )"""

cursor.execute(sql)

# disconnect from server
db.close()
