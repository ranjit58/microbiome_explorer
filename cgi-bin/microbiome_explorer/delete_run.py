#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module,os
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
data_run = form.getvalue('run')
   
sql = "DELETE FROM runs WHERE run_id = '" + data_run + "';DELETE FROM samples where run_id = '" + data_run + "';"
cursor.execute(sql)

tmp_name=str(data_run) + "_mapping.xlsx"
if os.path.exists('../../html/microbiome_explorer/mapping_files/' + tmp_name):
  try:
      os.remove('../../html/microbiome_explorer/mapping_files/' + tmp_name)
  except OSError, e:
      print ("Error: %s - %s." % (e.filename,e.strerror))

message = '<div class="container"><h4>Run deleted successfully</h4></div>'

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

