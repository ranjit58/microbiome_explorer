#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

import os, sys

# prepare a cursor object using cursor() method
cursor = db.cursor()

form = cgi.FieldStorage()


data_run_group = form.getvalue('run_group')
data_user_email = form.getvalue('user_email')
data_title = form.getvalue('title')
data_notes = form.getvalue('notes')
data_links = form.getvalue('links')

if data_title == None:
   data_title = ""
if data_notes == None:
   data_notes = ""
if data_links == None:
   data_links = ""
print data_run_group
print data_user_email

if "user_email" in form and "run_group" in form:

   sql = "INSERT INTO projects (run_group,user_email,title,notes,links) VALUES('" + data_run_group + "', '" + data_user_email + "', '" + data_title + "', '" + data_notes + "', '" + data_links + "');"
   try:
     # Execute the SQL command
     cursor.execute(sql)
     #  Commit your changes in the database
     db.commit()
     message = '<div class="container"><h4>Project added sucessfully</h4></div>'

   except MySQLdb.IntegrityError, e:
     message = '<div class="container"><h4>Error: Project not added (maybe a project with same name exists)</h4></div>'
     # Rollback in case there is any error
     db.rollback()


    
else:
   message = '<div class="container"><h4>Not Sufficient inputs provided!<br><br> Please provide Project name and Email address.</h4></div>'  
   

module.print_html_head()
   
module.print_func()
print message
html_code='''

</body>
</html>
'''
print html_code
cursor.close()
db.commit()
 
# disconnect from server
db.close()
