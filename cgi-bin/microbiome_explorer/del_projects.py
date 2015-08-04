#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()
sql = "SELECT DISTINCT run_group FROM projects ORDER BY run_group DESC"
cursor.execute(sql)
results= cursor.fetchall()

module.print_html_head()

module.print_func()

html_code='''

<div class="container">
<div class="panel panel-default">
<div class="panel-heading">    
<b>Delete from projects</b>
</div>
      <div class="form-group" >
<form class="form-inline" action="/cgi-bin/microbiome_explorer/delete_projects.py" method="post">

           
   
 <br>                                 
&nbsp;&nbsp;&nbsp;&nbsp;Delete by run_group:&nbsp;&nbsp;&nbsp;&nbsp;<select name="run_group">
'''







print html_code
for row in results:
  run_group = row[0]
  #fwd_sample = row[1]
  #rev_sample = row[2]
  #sample_name = row[3]
  #run_group = row[0]
  #user_email = row[5]
  #user_project_name = row[6]
  # Now print fetched result
  #print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % \
  #( run_number,fwd_data,rev_data,sample_name,run_group,user_email,user_project )
  #f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % \
  #( run_number,fwd_data,rev_data,sample_name,run_group,user_email,user_project )
  print '<option value=',run_group,'>',run_group,'</option>'

html_code='''

</select>
&nbsp;&nbsp;


        
         <button type="submit" class="btn btn-success">Delete&nbsp;</button>
      </form> 
      </div>
      </div>
      
    
</div>
</div>

    
  
  
   
</body>
</html>
'''
print html_code



cursor.close()
db.commit()
 
# disconnect from server
db.close()
