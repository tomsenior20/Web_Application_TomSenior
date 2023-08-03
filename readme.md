<!-- Create Virtual Environment -->
python3 -m venv <name of environment>
<!-- Activating the Environment -->
source venv/bin/activate
# Can intall flask
python3 install flask

# Example of how to activate the sqlite3

1) Access Terminal 
# (This is the name of the Database)
2) type in sqlite3 database.db 
3) This will then run the sqlite3 in terminal
4) An SQLLite Explorer will be present on the bottom left to where the database and contents can be seen
5) via the sqllite3 terminal you can enter the below insert script or .tables to show all the present tables in the database.

# Data created inside of Data table
# example doesn't include id, due to being auto incrementing
INSERT INTO data (LOCATION, COMMENT) VALUES ('Crewe', 'Old Office Location');# Web_Application_TomSenior

# Things to note 

1) Data for the data to display on the page will be set up prior to uploading - Please note if this table is data, you will have to login as an admin user and you can create your own data and insert it into the table.

2) If Admin = yes, upon logging into the web_app you will be able to see the buttons to

- update 
- delete
- insert

3) if not admin, you will just be able to see the rendered data, and will have a message showing "You have read only permisions"


# Web_Application_TomSenior
