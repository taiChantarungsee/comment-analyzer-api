Run main.py to run the program. The program uses a database to save the comments and I've used a dictionary called 
'payload' to mock the data. In order to use it with the mysql database, enter your username and password at line 7 and 
10 of db.py, and line 6 of save.py, and run the db.py file. If you want to just see the program without the database, simply 
comment out line 40 of main.py. 

The program is built with a reliable relational database, Mysql,and uses logging when an error occurs. This will make it 
easier to scale. The code is RESTful, because all the information a particular request needs is contained within that 
request. There is only one URL which is defined as responsding to the 'GET' method ('POST' or 'PUT' could have been
conceivably used but I decided not to since the user doesn't actually need to send the information that will be saved
himself). I have documented the API using comments. I have also split the program into several modular files, which helps
with development, scaling and trouble shooting. And finally I have written a test for it, which helps with trouble shooting
(The test also prints out a warning along with the test result, this is specifically a Python 3 issue that can't be resolved).