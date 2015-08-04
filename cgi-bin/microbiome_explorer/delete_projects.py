#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
data_run_group = form.getvalue('run_group')
   
sql = "DELETE FROM projects WHERE run_group = '" + data_run_group + "';"


try:
    cursor.execute(sql) 
    db.commit()
    message = '<div class="container"><h4>Project deleted successfully</h4></div>'
except:
    db.rollback()
    message = '<div class="container"><h4>Error: Unable to delete project</h4></div>'

module.print_html_head()

module.print_func()
html_code='''
</body>
</html>
'''
print html_code
print message

cursor.close()
db.commit()
 
# disconnect from server
db.close()
