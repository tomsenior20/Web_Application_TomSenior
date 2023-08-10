# Create Virtual Environment
python3 -m venv <name of environment>
# Activating the Environment
source venv/bin/activate
# Intall flask
python3 install flask
# Run Environment via the Source code
The code can either be ran via the following two options:

1) python3 test.py
2) debugger window - via the flask application.
3) it will then provide a IP in the terminal which will normally be host :5000

# Example of how to activate the sqlite3

1) Access Terminal 
(This is the name of the Database)
2) type in sqlite3 database.db 
3) This will then run the sqlite3 in terminal
4) An SQLLite Explorer will be present on the bottom left to where the database and contents can be seen
5) via the sqllite3 terminal you can enter the below insert script or .tables to show all the present tables in the database.
6) Alternatively you can see all data present in the tables, via SQL Explorer and right click on the table and click "show Table"

# example doesn't include id, due to being auto incrementing
INSERT INTO data (LOCATION, COMMENT) VALUES ('Crewe', 'Old Office Location');# Web_Application_TomSenior

# Things to note 
For the data to display on the page, this should be set up prior to accessing. However, Please note if this table is empty, you will have to login as an admin user and you can create your own data and insert it into the table.

2) If Admin = yes, upon logging into the web_app you will be able to see the buttons to perform the following steps:

- update 
- delete
- insert

3) If admin is "no", you will just be able to see the rendered data. With a message showing "You have read only permisions"

# Unit Tests - (Completed only ) 
Can be accessed via testing.py

1) check_login (aut.py)

# Can run test via the following command
- python3 testing.py
