#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb
import MySQLdb

cgitb.enable()
from datetime import datetime, date, time
# Open database 
#db = MySQLdb.connect("localhost","biotoolz_ranjit","ranjitiisc","biotoolz_microbiome_explorer" )
# prepare a cursor object using cursor() method
#cursor = db.cursor()


#db.close()
