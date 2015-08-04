#!/usr/bin/python
print "Content-type:text/html\r\n\r\n"

import cgi,cgitb,MySQLdb,module
cgitb.enable()

# Open database connection
db = module.get_mysql_connection()

import os

module.print_html_head()
module.print_func()

form = cgi.FieldStorage()


# Get filename here.
fileitem1 = form['mapping_file']
data_run_id = form.getvalue('run_id')

if fileitem1.filename and data_run_id != '':
   fn1 = os.path.basename(fileitem1.filename)
   tmp_name=str(data_run_id) + "_mapping.xlsx"

   if os.path.exists('../../html/microbiome_explorer/mapping_files/' + tmp_name):
      try:
          os.remove('../../html/microbiome_explorer/mapping_files/' + tmp_name)
      except OSError, e:
          print ("Error: %s - %s." % (e.filename,e.strerror))

   open('../../html/microbiome_explorer/mapping_files/' + tmp_name, 'w').write(fileitem1.file.read())
   message = '<div class="container"><h4>Mapping file changed.</h4></div>'
   print message

else:
   message = '<div class="container"><h4>Not all input provided. Please provide input in all fields.</h4></div>'  
   print message
 
html_code='''

</body>
</html>
'''
print html_code

