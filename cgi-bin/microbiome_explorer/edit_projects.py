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

sql = "Select * FROM projects where run_group = '" + data_run_group + "'"

cursor.execute(sql)
results = cursor.fetchall()

module.print_html_head()

module.print_func()



html_code='''
<div  class="container">

<div class="panel panel-default">
<div class="panel-heading">    
<b>EDIT PROJECTS</b>
</div>
      <div class="panel-body">  
      

      <form class="form-inline" action="save_projects.py" method="post">
'''
print html_code

for row in results:
 
  run_group = row[0]
  user_email = row[1]
  title = row[2]
  notes = row[3]
  links = row[4]

print 'Project Name:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
print '<input type="text" name="run_group" style="width: 200px;"  class="form-control" readonly value="' + run_group + '"><br><br>'
print 'Email:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'
print '<input type="text" name="user_email" style="width: 200px;"  class="form-control" readonly value="' + user_email + '"><br><br>'

if title == None:
    title = ''
print 'Title:    &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="title" rows=2 size="71" value="' + title + '"><br><br>'
print 'Notes: &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;<textarea class="form-control" name="notes" rows="6" cols="71">'
if notes == None:
    notes = ''

tmp_notes=notes.splitlines()
for items in tmp_notes:
    print str(items)  
print '</textarea><br><br>'

print 'Links: &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;<textarea class="form-control" name="links" rows="6" cols="71">'
if links == None:
    links = ''
tmp_links=links.splitlines()
for items in tmp_links:
    print str(items)
print '</textarea><br><br>'


html_code='''     
	    <button type="submit" class="btn btn-success">Save</button>
	  
        
      </form> 
      </div>
  
      
    
</div>
</div> 
</body>
</html>
'''
print html_code




