# comment-analyzer-api
Example program of a basic API that uses IBM Bluemix's tone analyzing technology to analyze a comment identified by SKU,
and then stores the result.

Program uses a mysql database, so you need to insert your mysql username and password at line 7 and 
10 of db.py, and line 6 of save.py, and run the db.py file. If you want to just see the program without the database, simply 
comment out line 48 of main.py. You also need to add your bluemix credentials in main.py.