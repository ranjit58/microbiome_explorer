#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
from datetime import datetime, date, time

cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()


module.print_html_head()
module.print_func()

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

data_name = form.getvalue('name')

sql = "SELECT distinct projects.user_email,name,department,user_notes from projects left join users on users.user_email=projects.user_email order by projects.user_email ASC"
cursor.execute(sql)

results = cursor.fetchall()

html_code='''
<div class="container"><h3><u>Users</u></h3><br>
<table id="myTable" class="table table-striped table-bordered table-condensed table-hover" cellspacing="0" width="100%">
         <thead>

          <tr class="jumbotron">
            <th>S.no</th>
            <th>User_Email</th>
            <th>Name</th>
            <th>Department</th>
            <th>Other_Notes</th>
         </tr>
        </thead>
'''
print html_code
c0=0
for row in results:
      user_email = row[0]
      name = row[1]
      department = row[2]
      user_notes = row[3]
      # Now print fetched result
      c0=c0+1
      if name == None:
         name = ''
      if department == None:
         department = ''
      if user_notes == None:
         user_notes = ''
      print '<tr><td>' + str(c0) + '</td><td>' + user_email + '</td><td>' + str(name) + '</td><td>' + str(department) + '</td><td>' + str(user_notes) + '</td></tr>'
      print "\n"     

html_code='''
</table>
</div>
</body>
</html>
'''
print html_code

db.close()
