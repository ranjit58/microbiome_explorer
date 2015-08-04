#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query

sql2 = "SELECT DISTINCT user_email FROM projects;"
sql3 = "SELECT DISTINCT run_group FROM projects;"




cursor.execute(sql2)
results2 = cursor.fetchall()

cursor.execute(sql3)
results3 = cursor.fetchall()

module.print_html_head()
module.print_func()

html_code='''
<form action="/cgi-bin/microbiome_explorer/projects_for_edit.py" method="post">

<div class="container"><h3><u>Projects</u></h3><br>
<div class="panel panel-primary">
    <div class="panel-body">  
                               


Run Group:&nbsp;&nbsp;&nbsp;&nbsp;<select name="run_group">
'''
print html_code

for row in results3:
  run_group = row[0]
  print '<option value=',run_group,'>',run_group,'</option>'

  
html_code='''
<option value="all" selected>ALL</option>
</select>
&nbsp;&nbsp;&nbsp;&nbspEmail:&nbsp;&nbsp;&nbsp;&nbsp;<select name="user_email">
'''
print html_code
for row in results2:
  user_email = row[0]
  print '<option value=',user_email,'>',user_email,'</option>'

html_code='''
<option value="all" selected>ALL</option>
</select> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<button type="submit" class="btn btn-success">Submit</button>

</div>
</div>
</div>
</form>


'''
print html_code


############################################################################


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

data_user_email = form.getvalue('user_email')
data_run_group = form.getvalue('run_group')





if "user_email" not in form:
      sql4 = "SELECT * FROM projects"

else:


  if data_user_email=="all" and data_run_group=="all":
      sql4 = "Select * FROM projects"
    
  
  elif data_user_email=="all":
      sql4 = "Select * FROM projects where run_group = '" + data_run_group + "'"
  elif data_run_group=="all":
      sql4 = "SELECT * FROM projects where user_email = '" + data_user_email + "'"

  else:
      sql4 = "SELECT * FROM projects WHERE user_email = '" + data_user_email + "' AND run_group = '" + data_run_group + "'"


cursor.execute(sql4)

results4 = cursor.fetchall()


html_code='''
<div class="container">
<table id="xmyTable" class="table table-striped table-bordered table-condensed table-hover" cellspacing="0" width="100%">
         <thead>

          <tr class="jumbotron">
            <th>S.no</th>
            <th>Run_Group</th>
            <th>User_Email</th>
            <th>Title</th>
            <th>Notes</th>
            <th>Links</th>
            <th>Edit</th>
          </tr>
        </thead>
'''
print html_code
c0=0
for row in results4:
      run_group = row[0]
      user_email = row[1]
      title = row[2]
      notes = row[3]
      link = row[4]
      # Now print fetched result
      if title == None:
         title = ''
      if notes == None:
         notes = ''
      if link == None:
         link = ''
      c0=c0+1
      
      tmp_notes=notes.splitlines()
      tmp_links=link.splitlines()
     
      print '<tr><td>' + str(c0) + '</td><td>' + run_group + '</td><td>' + user_email + '</td><td>' + str(title) + '</td><td>' 
      for items in tmp_notes:
          print str(items) + '<br>'
      print '</td><td>'
      for items in tmp_links:
          print '<a target="_blank" href="' + str(items) + '">' + str(items) + '</a><br>'
      
      print '</td><td><form action="edit_projects.py" method="post"><input type="hidden" name="run_group" value="' + run_group + '"><input type="image" src="/microbiome_explorer/icon-edit.png" ></input></form></tr>'
      print "\n"     

html_code='''
</table>
</div>
</body>
</html>
'''
print html_code

db.close()
