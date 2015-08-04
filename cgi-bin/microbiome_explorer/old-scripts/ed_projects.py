#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"
import cgi,cgitb
cgitb.enable()
import MySQLdb
import module
# Open database connection
db = MySQLdb.connect("localhost","biotoolz_ranjit","ranjitiisc","biotoolz_microbiome_explorer" )
# prepare a cursor object using cursor() method
cursor = db.cursor()


form = cgi.FieldStorage()


# Get filename here.

data_run_group = form.getvalue('run_group')
data_user_email = form.getvalue('user_email')
data_title = form.getvalue('title')
data_notes = form.getvalue('notes')
data_links = form.getvalue('links')

# Test if the file was uploaded
if "run_group" and "user_email" and "title" and "notes" and "links" in form:
   
   message = '<div class="container"><h4>Projects updated successfully</h4></div>'
   
   sql = "UPDATE projects set user_email='" + data_user_email + "',title='" + data_title + "',notes='" + data_notes + "',links='" + data_links + "' where run_group = '" + data_run_group + "'"
   cursor.execute(sql)
  
 
  
else:
   message = '<div class="container"><h4>No input provided</h4></div>'  
   
   
   
html_code='''
\Content-Type: text/html\n
<html>
<head>
<title>microbiome_explorer</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  

  <link href="/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
</head>
<body>
'''

print html_code
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
