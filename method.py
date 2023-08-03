import sqlite3
from flask import Flask, render_template, flash
from classes import User, DataRecord

# Creates the tables on page load 
def create_users_table():
    # Connect to the database (creates a new database if it doesn't exist)
    conn = sqlite3.connect("database.db")
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    # Create the Table SQL query to create the table if not present
    create_user_table_query = '''
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL UNIQUE,
            Password TEXT NOT NULL,
            Admin TEXT NOT NULL
        )
    '''
    create_data_table_query = '''
        CREATE TABLE IF NOT EXISTS data (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LOCATION STRING NOT NULL,
            COMMENT STRING NOT NULL
            
        )
    '''
    # Runs the SQL Query
    cursor.execute(create_user_table_query)
    cursor.execute(create_data_table_query)
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Runs on register form submit
def check_and_register_user(user_id, password, admin_privilege):
    # Connect to the database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    msg = None
    # Check if the user with the given user_id already exists
    cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
    existing_user = cursor.fetchone()
    # if condition = true return the string
    if existing_user:
        # User already exists
        msg =  "User already exists in the database."
    else:
        # Write the user to the 'users' table if previous condition = false
        if len(user_id) >= 4 and len(password) >= 4 and (admin_privilege == "yes" or admin_privilege == "no"):
            try:
                #Assigns the parameters to an object
                new_user = User(user_id,password,admin_privilege)
                cursor.execute("INSERT INTO users (user_id, Password, Admin) VALUES (?, ?, ?)", (new_user.user_id, new_user.password, new_user.admin_privilege))
                conn.commit()
                msg = "Success, User has been registered"
            except:
                msg = "error"
        else:
            msg = "Error Invalid Input"
    conn.close()
    return msg

# Check Login Credentials
def check_login_check(username,password):
    # Connect to the database
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Gets the paramateres for the username & password and removes whitespace.
    if username and username.strip() and password and password.strip():
        cursor.execute("SELECT * from users WHERE user_id = ? AND password = ?" ,(username,password))
        user = cursor.fetchone()
        # Checks if the user exsists
        if user:
            # Assigns each column to the User Class
            retuned_record = User(user[1], user[2], user[3])
            # Checks if the entered password & username match the record, return the relevant success / error message
            if retuned_record.password == password and retuned_record.user_id == username:
                loginMsg = "success"
            else:
                loginMsg = "invalid password"
        else:
            loginMsg = "User does not exsist"
    else:
        return render_template("index.html")
    conn.close()
    return loginMsg

# Display Data Method
def display_data():
    conn  = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Executes the SQL Query
    cursor.execute("SELECT * FROM data")
    # Fetches all the rows associated to the query
    rows = cursor.fetchall()
    # Creates Empty array for the data
    record_list = []
    # For each row in the fetched rows, create new DataRecord object and assign values and append to previous object
    for row in rows:
       data_record = DataRecord(row[2], row[1])
       record_list.append(data_record)
    # Close Connection
    conn.close()
    # Returns the object
    return record_list

# Retrieve a User Record
def get_user_record(username,password):
    conn  = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # Executes the SQL Query
    cursor.execute("SELECT * FROM users WHERE user_id = ? and Password = ?" ,(username, password,))
    user = cursor.fetchall()
    
    matched_record = []
    # Loop over all the records
    for matched_user in user:
        matched_user_record = User(matched_user[1],matched_user[2], matched_user[3])
        matched_record.append(matched_user_record)
    # close connection  
    conn.close()
    return matched_record

# Deleting From SQL Script
def delete_row(location):
    conn  = sqlite3.connect("database.db")
    cursor = conn.cursor()
    
    cursor.execute("select * from data WHERE Location = ?", (location,))
    row_present = cursor.fetchall()
    
    if row_present:
        # Executes the SQL Query via DELETE
        cursor.execute("DELETE FROM data WHERE Location = ?" ,(location,))
        conn.commit()
        delete_msg = "success"
    # Close Connection
    else:
        delete_msg = "error"
    
    conn.close()
    return delete_msg

# Inserting Row function
def inserting_row(location,comment):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM data where Location =?", (location,))
    location_exists = cursor.fetchall()
    
    if location_exists:
        msg = "Location already is in data, no duplicates allowed"
    else:
        # Execute the SQL query using wildcard
        cursor.execute("INSERT INTO data (Location, Comment) VALUES (?,?)", (location,comment))
        conn.commit()
        msg = "success"
        
    return msg


# Updating Location
def update_location(oldLocation, newLocation):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    # See if the record is present in the DB with the old location name
    cursor.execute("select * from data WHERE Location = ?",(newLocation,))
    exisitng_location = cursor.fetchall()
    
    if exisitng_location:
        location_msg = "Error - New location already exists in the database"
    else:
        cursor.execute("select * from data WHERE Location = ?",(oldLocation,))
        location_record = cursor.fetchall()
        
        if location_record:
            # Execute the SQL
            cursor.execute("UPDATE data SET Location =? WHERE Location = ? ", (newLocation, oldLocation))
            conn.commit()
            location_msg = "Successfully Updated Row"
        else:
            location_msg = "Error - Record with Location not found"
        
    return location_msg

# Updating comment
def update_comment(oldComment, newComment):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
     # See if the record is present in the DB with the old comment
    cursor.execute("select * from data WHERE Comment = ?",(newComment,))
    existing_comment = cursor.fetchall()
    
    if existing_comment:
        comment_msg = "Error - New Comment already exists in the database"
    else:
        cursor.execute("select * from data WHERE Comment = ?",(oldComment,))
        comment_record = cursor.fetchall()
        
        if comment_record:
            # Execute the SQL
            cursor.execute("UPDATE data SET Comment = ? WHERE Comment = ? ", (newComment, oldComment))
            conn.commit()
            comment_msg = "Successfully Updated Row"
        else:
            comment_msg = "Error - Record with Comment not found"
        
    return comment_msg