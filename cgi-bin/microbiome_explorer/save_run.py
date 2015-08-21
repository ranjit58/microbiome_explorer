#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module,os
cgitb.enable()

# Open database connection
db = module.get_mysql_infile_connection()

# prepare a cursor object using cursor() method
cursor = db.cursor()

module.print_html_head()
module.print_func()

form = cgi.FieldStorage()


# Get filename here.
fileitem = form['filename']
#data_run = form.getvalue('run')
data_run_id = form.getvalue('run_id')
data_run_name = form.getvalue('run_name')
data_run_date = form.getvalue('run_date')
data_run_machine = form.getvalue('run_machine')
data_run_read_length = form.getvalue('run_read_length')
#data_run_stats = form.getvalue('run_stats')
data_run_mapping = form.getvalue('run_mapping')


      


# Test if the file was uploaded
if fileitem.filename and data_run_id != '' and data_run_name != '' and data_run_date != '' and data_run_machine != '' and data_run_read_length != '':
   # strip leading path from file name to avoid 
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)

   if os.path.exists('tmp/' + fn):
       try:
           os.remove('tmp/' + fn)
       except OSError, e:
           print ("Error: %s - %s." % (e.filename,e.strerror))

   open('tmp/' + fn, 'w').write(fileitem.file.read())
   os.system("dos2unix" + 'tmp/' + fn)

   # test if first column of uploaded file and run_id are same.
   fo = open('tmp/' + fn, "r")
   line = fo.readline()
   line_item =  line.split()
   #print line_item[0]
   fo.close()
   
   if (line_item[0] == data_run_id):
      
     sql1 = "LOAD DATA LOCAL INFILE 'tmp/" + fn + "' INTO TABLE samples LINES TERMINATED BY '\n';"
     try:
       # Execute the SQL command
       cursor.execute(sql1)
       #  Commit your changes in the database
       db.commit()
       #message = '<div class="container"><h4>Samples added sucessfully</h4></div><br>'
       #print message

     except MySQLdb.IntegrityError, e:
       #message = '<div class="container"><h4>Error: Samples not added (maybe samples already exists in database)</h4></div>'
       #print message
       # Rollback in case there is any error
       db.rollback()

     if os.path.exists('tmp/' + fn):
          try:
              os.remove('tmp/' + fn)
          except OSError, e:
              print ("Error: %s - %s." % (e.filename,e.strerror))

     sql2 = "INSERT INTO runs (run_id,run_name,run_date,run_machine,run_read_length) VALUES ('" + data_run_id + "', '" + data_run_name + "', '" + data_run_date + "', '" + data_run_machine + "', '" + data_run_read_length + "');"
     try:
       # Execute the SQL command
       cursor.execute(sql2)
       #  Commit your changes in the database
       db.commit()
       message = '<div class="container"><h4>Run/Samples added sucessfully</h4></div><br>'
       print message
  
     except MySQLdb.IntegrityError, e:
       message = '<div class="container"><h4>Error: Run/Samples not added (maybe run/samples already exists in database)</h4></div>'
       print message
       # Rollback in case there is any error
       db.rollback()
    

#     sql4 = "INSERT INTO projects (run_group,user_email) select distinct run_group,user_email from samples where run_id='" + data_run_id + "'"
#     try:
#       # Execute the SQL command
#       cursor.execute(sql4)
#       #  Commit your changes in the database
#       db.commit()
       #message = '<div class="container"><h4>Project added/edited sucessfully</h4></div>'

#     except MySQLdb.IntegrityError, e:
#       #message = '<div class="container"><h4>Error: Project not added/edited (maybe a project with same name exists)</h4></div>'
#       # Rollback in case there is any error
#       db.rollback()


   else:
     message = '<div class="container"><h4>Error: The Run_Id does not match with first column of the samples file. Please correct it and add the run again.</h4></div>'
     print message

else:
   message = '<div class="container"><h4>Not all input provided. Please provide input in all fields.</h4></div>'  
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



   
