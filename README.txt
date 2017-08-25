Run main.py to run the program. The program uses a database to save the comments and I've used a dictionary called 
'payload' to mock the data. In order to use it with the mysql database, enter your username and password at line 25 of 
main.py and line 5 of save.py and run the db.py file. If you want to just see the program without the database, simply 
comment out line 48 of main.py.

The program is built with a reliable relational database, Mysql,and uses logging when an error occurs. This will make it 
easier to scale. The code is restful, because all the information a particular request needs is contained within that request.
I have documented the API using comments. I have also split the program into several modular files, which helps with 
development, scaling and trouble shooting. 