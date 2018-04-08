#!/usr/local/bin/python3
>>> 
>>> import cgi
>>> 
>>> def htmlTop():
	print("""Content-type:text/html\n\n
<!DOCTYPE html>
<html lang = "en">
<head>
<meta charset="utf-8"/>
<title>My server-side template</title>
</head>
<body>""")

	
>>> def htmlTail():
	print("""</body>
</html>""")

    def getData():
        formData=cgi.FieldStorage()
        name = formData.getvalue('name')
        return name

	
>>> #main program
>>> if __name__ == "_main_":
	try:
		htmlTop()
		name = getData()
		print(format(name))
		htmlTail()
	except:
            cgi.print_exception()
            
