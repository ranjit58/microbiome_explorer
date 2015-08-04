#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()


module.print_html_head()

module.print_func()
html_code='''

<div class="container">

<div class="panel panel-default">
<div class="panel-heading">    
<b>Add data from run</b>
</div>
      <div class="panel-body">  


      <form enctype="multipart/form-data" class="form-inline" action="/cgi-bin/microbiome_explorer/save_run.py" method="post">
      Sample Information&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;: &nbsp;&nbsp;&nbsp;&nbsp;<input type="file" class="form-control" name="filename">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g. sample text file: <a href="/microbiome_explorer/sample.txt">sample.txt</a><br><br>
      
      Run Number&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;:&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;<input type="text" class="form-control" name="run_id">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.&nbsp;M58&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      Run_Name&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="run_name">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.&nbsp;M58mar22<br><br>
      Run_Date&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;:    &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="run_date">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.&nbsp;2015-03-22&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      Run_Machine&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;: &nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="run_machine" value="MiSeq">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.&nbsp;MiSeq<br><br>
      Run_length&nbsp;<sup><span class="glyphicon glyphicon-asterisk" style="color:red;font-size: 8px"></span></sup>&nbsp;: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<input type="text" class="form-control" name="run_read_length" value="2X251">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e.g.&nbsp;2X251&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
      <br><br> 

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




