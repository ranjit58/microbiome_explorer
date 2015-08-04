#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql1 = "SELECT DISTINCT user_email FROM users"
cursor.execute(sql1)
results1 = cursor.fetchall()

module.print_html_head()

module.print_func()
html_code='''
<div class="container">

<div class="panel panel-default">
<div class="panel-heading">    
<b>Add Projects</b>
</div>
      <div class="panel-body">
 <form class="form-inline" action="/cgi-bin/microbiome_explorer/save_new_project.py" method="post">
Project Name&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="run_group">

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Email&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input list="user_email" class="form-control" name="user_email">
<datalist id="user_email">
'''
print html_code

for row in results1:
 
  user_email = row[0]
  print '<option value=',user_email,'>',user_email,'</option>'

html_codes='''

<option selected hidden value=""></option>
</datalist> 
'''
print html_codes




html_codes='''

      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <br><br>
      Title:    &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="title" size="69" Value="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>
      Notes: &nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;<textarea class="form-control" name="notes" rows="3" cols="71" value=""></textarea>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>
      Links: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<textarea class="form-control" rows="3" cols="71" name="links" value=""></textarea>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>
     
      

	    <button type="submit" class="btn btn-success">Submit</button>
	    </div>
        
      </form> 
      </div>
  
      
    
</div>
</div>

    
  
  
   
</body>
</html>
'''
print html_codes
