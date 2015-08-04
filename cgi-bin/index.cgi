#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()  # for troubleshooting

#print header
print "Content-type: text/html"
print
print "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
print "<!DOCTYPE html>"
print "<html>"
print "<head>"
print "<title>Python CGI test</title>"
print "</head>"
print "<body>"
print "<p>Ranjit: Hello, world!</p>"
print "</body>"
print "</html>"
