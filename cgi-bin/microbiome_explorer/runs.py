#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

import os.path
from datetime import datetime, date, time

# prepare a cursor object using cursor() method
cursor = db.cursor()


module.print_html_head()
module.print_func()

# Prepare SQL query
sql = "SELECT * FROM runs ORDER BY run_id DESC"

cursor.execute(sql)

results = cursor.fetchall()


html_code='''
<div class="container"><h3><u>Runs</u></h3><br>
<table id="myTable" class="table table-striped table-bordered table-condensed table-hover" cellspacing="0" width="100%">
         <thead>

          <tr class="jumbotron">
            <th>S.no</th>
            <th>Run_Id</th>
            <th>Run_Name</th>
            <th>Run_Date</th>
            <th>Run_Machine</th>
            <th>Read_properties</th>
            <th>Run_mapping</th>
          </tr>
        </thead>
'''
print html_code
c0=0
for row in results:
      
      c1 = row[0]
      c2 = row[1]
      c3 = row[2]
      c4 = row[3]
      c5 = row[4]
      
      
      
      # Now print fetched result
      c0=c0+1
      print '<tr><td>' + str(c0) + '</td><td>' + c1 + '</td><td>' + c2 + '</td><td>' + str(c3) + '</td><td>' + c4 + '</td><td>' + c5 + '</td><td>'

      filename = '../../html/microbiome_explorer/mapping_files/' + c1 + '_mapping.xlsx'
      if os.path.isfile(filename):
            print '<a href=/microbiome_explorer/mapping_files/' + c1 + '_mapping.xlsx>' + c1 + '_mapping.xlsx</a>'
      else:
            print "-"
      print '</td></tr>'
      print "\n"     

html_code='''
</table>
</div>
</body>
</html>
'''
print html_code

db.close()
