#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cgi, os
import csv

f = open('wordlist2.csv', 'r')
data = csv.reader(f)

print "Content-type: text/html"
print
print '''<html><head>
    <meta charset="utf-8">
    <title>Glossary</title>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,300,700" rel="stylesheet" type="text/css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/4.1.1/normalize.min.css">
    <link rel="stylesheet" href="site.css">
    </head>

    <style>

    .sidenav {
        height: 100%;
        width: 0;
        position: fixed;
        z-index: 1;
        top: 0;
        left: 0;
        background-color: #111;
        overflow-x: hidden;
        transition: 0.5s;
        padding-top: 60px;
    }

    .sidenav a {
        padding: 8px 8px 8px 32px;
        text-decoration: none;
        font-size: 25px;
        color: #818181;
        display: block;
        transition: 0.3s
    }

    .sidenav a:hover, .offcanvas a:focus{
        color: #f1f1f1;
    }

    .closebtn {
        position: absolute;
        top: 0;
        right: 25px;
        font-size: 36px !important;
        margin-left: 50px;
    }

    @media screen and (max-height: 450px) {
      .sidenav {padding-top: 15px;}
      .sidenav a {font-size: 18px;}
    }
    </style>

    <body>
    <div id="container-mobile-left">
      <img src="http://bigcat.fhsu.edu/volgagerman/sun.png" alt="Sun Flower Chapter logo" style="width:450px;height:75px;">  <img src="http://bigcat.fhsu.edu/volgagerman/khc.jpg" alt="Kansas Humanities Council logo" style="width:200px;height:75px;">  <img src="http://bigcat.fhsu.edu/volgagerman/fhsu.png" alt="FHSU logo" style="width:245px;height:90px;">
    <div id="mySidenav" class="sidenav">
      <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">×</a>
      <a href="http://bigcat.fhsu.edu/volgagerman/about.html">About</a>		
      <a href="http://bigcat.fhsu.edu/volgagerman/haberkorn/index.html">Haberkorn collection</a>		
      <a href="http://bigcat.fhsu.edu/volgagerman/songs.html">Song collection</a>		
      <a href="http://bigcat.fhsu.edu/cgi-bin/volgagerman/dictionary2.py">Glossary</a>
      <a href="http://bigcat.fhsu.edu/volgagerman/grammar.html">Grammar</a>
      <a href="http://bigcat.fhsu.edu/volgagerman/staff.html">Project staff</a>			
    </div>
    <p></p>
    <span style="font-size:30px;cursor:pointer" onclick="openNav()">    ☰ menu  </span>
    <script>
    function openNav() {
        document.getElementById("mySidenav").style.width = "250px";
    }
    function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
    }
    </script>
    <br /><br />
    <form> 
    <input type='text' name='yyy'/>
    </form> '''

arguments = cgi.FieldStorage()
word_list = []
for i in arguments.keys():
    x = arguments[i].value

X = x.capitalize()
for row in data:
    if x==row[0] or X==row[0]:
        word_list.append(row[0])            
        print '<b> %s </b> (%s):' %(row[0], row[1])      
        definitions = [ row[n] for n in range(3, len(row)) if row[n] != '' ]
        def_concatenated = '; '.join(definitions)
        print def_concatenated
        print '<br>'    
        if row[2] is not None:
            print 'Standard German: ', row[2], '<br>'
            
if not word_list:
    print "Sorry, this word has not been added to the glossary yet. <br><br>"

f.close()
hab_dir = '/usr2/web/volgagerman/haberkorn'
os.chdir(hab_dir)
dirs = [name for name in os.listdir(".") if os.path.isdir(name)]

for d in dirs:
    path = hab_dir + '/' + d
    os.chdir(path)
    files = [name for name in os.listdir(".") if os.path.isfile(name)]    
    #print '<table>'    
    example_list = []    
    for f in files:
        if '_ger.txt' in f and '~' not in f:
            f3 = open(f, 'r')
            data = f3.readlines()                          
            for i, j in enumerate(data):             
                 if x in j or X in j:       
                    print '<p>'                    
                    print '...'              
                    try:                    
                        print data[i-4] 
                    except:
                        pass                    
                    try:                    
                        print data[i-2] 
                    except:
                        pass
                    try:                    
                        new = '<b><font color="red">'+x+'</font></b>'
                        j = j.replace(x, new)
                    except:
                        pass
                    try:                    
                        new = '<b><font color="red">'+X+'</font></b>'
                        j = j.replace(X, new)
                    except:
                        pass
                    print j 
                    try: 
                        print data[i+2] 
                    except:
                        pass
                    try:                    
                        print data[i+4] 
                    except:
                        pass
                    print '...'
                    filename = '''https://bigcat.fhsu.edu/volgagerman/haberkorn/''' + d + '/' +d +'.html'
                    print '<br>'                    
                    print '<a href="%s">full text</a>' %(filename)
                    print '</p>'
    os.chdir(hab_dir)
 
print "</body></html>"
