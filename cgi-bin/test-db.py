#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
import MySQLdb

cgitb.enable()

from datetime import datetime, date, time

# Open database
db = MySQLdb.connect( host='genome-bmidb.ad.uab.edu', user='rkumar', passwd='qwerty', db='microbiome', port=17998)

# prepare a cursor object using cursor() method
cursor = db.cursor()

#sql = "SELECT * from users where name LIKE '%" + data_name + "%'"
sql = "SELECT * FROM projects"

cursor.execute(sql)

results = cursor.fetchall()

print results

db.close()
