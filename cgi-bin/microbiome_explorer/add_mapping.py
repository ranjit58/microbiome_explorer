#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

module.print_html_head()
module.print_func()

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query
sql = "SELECT DISTINCT run_id FROM runs;"

cursor.execute(sql)
results = cursor.fetchall()



html_code='''

<div class="container">

<div class="panel panel-default">
<div class="panel-heading">    
<b>Add/Edit excel mapping file for a run</b>
</div>
      <div class="panel-body">  


      <form enctype="multipart/form-data" class="form-inline" action="/cgi-bin/microbiome_explorer/save_mapping.py" method="post">
      Select the run_id: &nbsp;&nbsp;&nbsp;
      <Select name="run_id">
'''
print html_code

for row in results:
  temp = row[0]
  print '<option value=',temp,'>',temp,'</option>'

html_code='''
      </select>
      <br><br>
     
      Excel Run Mapping file: &nbsp;&nbsp;&nbsp;<input type="file" class="form-control" name="mapping_file">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. sample mapping file: <a href="/microbiome_explorer/sample_mapping.xlsx">sample_mapping.xlsx</a><br><br>        
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

	    <button type="submit" class="btn btn-success">Submit</button>
	    </div>
        
      </form> 
      </div>
  
      
    
</div>
</div>

    
  
  
   
</body>
</html>
'''
print html_code




