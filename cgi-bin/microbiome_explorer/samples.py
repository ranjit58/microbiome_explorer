#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query
sql1 = "SELECT DISTINCT run_id FROM samples ORDER BY run_id DESC"
sql2 = "SELECT DISTINCT user_email FROM samples"



cursor.execute(sql1)
results1= cursor.fetchall()

cursor.execute(sql2)
results2 = cursor.fetchall()

module.print_html_head()
module.print_func()

html_code='''
<div class="container"><h3><u>Samples</u></h3><br>
<div class="panel panel-primary">
<div class="panel-body"> 
<form class="form-inline" action="samples.py" method="post">

	<div class="form-group">
            <input type="text" class="form-control" placeholder="Search by sample_name" name="sample_name">
       </div>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OR&nbsp;&nbsp;&nbsp;
<div class="form-group" >             
      
                                  
Run ID:&nbsp;&nbsp;&nbsp;&nbsp; <select name="run_id">
'''


print html_code
for row in results1:
  run_id = row[0]
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
  print '<option value=',run_id,'>',run_id,'</option>'

html_code='''
<option value="all">ALL</option>
</select>
&nbsp;&nbsp;
</div>
<div class="form-group">

Email:&nbsp;&nbsp;&nbsp;&nbsp;<select name="user_email">
'''
print html_code
for row in results2:
  #run_number = row[0]
  #fwd_data = row[1]
  #rev_data = row[2]
  #sample_name = row[3]
  #run_group = row[4]
  user_email = row[0]
  #user_project = row[6]
  # Now print fetched result
  #print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % \
  #( run_number,fwd_data,rev_data,sample_name,run_group,user_email,user_project )
  #f.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % \
  #( run_number,fwd_data,rev_data,sample_name,run_group,user_email,user_project )
  print '<option value=',user_email,'>',user_email,'</option>'



  
html_code='''
<option value="all" selected>ALL</option>
</select>
&nbsp;&nbsp;
</div>

&nbsp;&nbsp;

<button type="submit" class="btn btn-success">Submit</button>


</form>
</div>

</div>



'''
print html_code


############################################################################


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields

data_run_id = form.getvalue('run_id')
data_user_email = form.getvalue('user_email')

data_sample_name = form.getvalue('sample_name')


#print "Request:"
#print "sample_name:",data_sample_name,"   "
#print "Run:",data_run_id," "
#print "Email:",data_user_email,"  "
#print "Project:",data_user_project_name,"  "


if "run_id" not in form:
      sql4 = "SELECT * FROM samples WHERE run_id = (SELECT DISTINCT run_id from samples ORDER BY run_id DESC LIMIT 1)"

else:
  if "sample_name" in form:
      sql4 = "SELECT * from samples where sample_name LIKE '%" + data_sample_name + "%'"

  elif data_user_email=="all" and data_run_id=="all":
      sql4 = "SELECT * FROM samples"

    


  elif data_run_id=="all":
      sql4 = "SELECT * FROM samples where user_email = '" + data_user_email + "'"
  elif data_user_email=="all":
      sql4 = "Select * FROM samples where run_id = '" + data_run_id + "'"



  else:
      sql4 = "SELECT * FROM samples WHERE run_id = '" + data_run_id + "' AND user_email = '" + data_user_email + "'"
#sql3 = "SELECT * FROM run WHERE run_number = '" + data_run_number + "'"    
#if "data_run_number" == 1:         
#return sql3
#print sql4
# Prepare SQL query
#sql = "SELECT * FROM run WHERE run_group='" + data_run_group + "'"
#sql = "SELECT * FROM run WHERE run_number = (SELECT run_number FROM RUN ORDER BY run_number LIMIT 1)"
#sql = "SELECT * FROM run WHERE run_number = (SELECT run_number from run LIMIT 1)"
#print data_run_group

cursor.execute(sql4)

results4 = cursor.fetchall()


html_code='''
<table id="xmyTable" class="table table-striped table-bordered table-condensed table-hover" cellspacing="0" width="100%">
         <thead>

          <tr class="jumbotron">
            <th>S.no.</th>
            <th>Run_id</th>
            <th>Fastq_fwd</th>
            <th>Fastq_rev</th>
            <th>Sample_name</th>
            <th>Run_Group</th>
            <th>User_Email</th>
            
          </tr>
        </thead>
'''
print html_code
c0=0
for row in results4:
      run_id = row[0]
      fwd_sample = row[1]
      rev_sample = row[2]
      sample_name = row[3]
      run_group = row[4]
      user_email = row[5]
      
      # Now print fetched result
      c0=c0+1
      print '<tr><td>' + str(c0) + '</td><td>' + run_id + '</td><td>' + fwd_sample + '</td><td>' + rev_sample + '</td><td>' + sample_name + '</td><td>' + run_group + '</td><td>' + user_email + '</td></tr>'
      print "\n"     

html_code='''
</table>
</div>
</body>
</html>
'''
print html_code

db.close()
