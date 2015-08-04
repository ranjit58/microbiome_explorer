#!/usr/bin/python

import cgi,cgitb,MySQLdb,module

def print_func():
	html_code='''<!-- Navigation -->
    <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                     <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="/cgi-bin/microbiome_explorer/runs.py">Microbiome Explorer</a>
            </div>
		<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
		
	 <ul class="nav navbar-nav navbar-right">

     



	 
 	 <li ><a href="/cgi-bin/microbiome_explorer/samples.py">SAMPLES</a></li>
 	 <li ><a href="/cgi-bin/microbiome_explorer/users.py">USERS</a></li>
 	  <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" >RUNS<span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="/cgi-bin/microbiome_explorer/runs.py">RUNS</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/add_run.py">ADD RUN</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/delete.py">DELETE RUN</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/add_mapping.py">EDIT MAPPING FILE</a></li> 
          </ul>
        </li>
 	 
          <li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown">PROJECTS<span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="/cgi-bin/microbiome_explorer/projects.py">PROJECTS</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/add_projects.py">ADD PROJECTS</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/projects_for_edit.py">EDIT PROJECTS</a></li>
            <li><a href="/cgi-bin/microbiome_explorer/del_projects.py">DELETE PROJECTS</a></li>
          </ul>
        </li>
	
	
	 </ul>
                   <!-- /.navbar-collapse -->
        </div>
                  <!-- /.container -->
    </nav>
    <br><br><br><br>'''
	print html_code
	return

def print_html_head():
	html_code='''
<html>
<head>

<title>microbiome_explorer</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="/css/bootstrap.min.css" rel="stylesheet">
  <script src="/js/jquery.min.js"></script>
  <script src="/js/bootstrap.min.js"></script>
  <link href="/css/jquery.dataTables.min.css" rel="stylesheet">
  <script src="/js/jquery.dataTables.min.js"></script>

  <script>
  $(document).ready(function(){
    $('#myTable').dataTable( {
        "lengthMenu": [[25, 50, 100, -1], [25, 50, 100, "All"]]
    } );
  } );
  </script>

  <style type="text/css">
  .table { font-size: 14px;}
  </style>

</head>
<body>
   '''
	print html_code
	return

def get_mysql_connection():
	db = MySQLdb.connect( host='genome-bmidb.ad.uab.edu', user='rkumar', passwd='qwerty', db='microbiome', port=17998)
	return db

def get_mysql_infile_connection():
        db = MySQLdb.connect( host='genome-bmidb.ad.uab.edu', user='rkumar', passwd='qwerty', db='microbiome', port=17998, local_infile = 1)
        return db
