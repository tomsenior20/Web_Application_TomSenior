import sqlite3
from flask import Flask, render_template, flash
from methods.classes import User, DataRecord
import bcrypt
import re


# Selects the table and will pass in the table param
def table_exists(cursor, table_name):
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,)
    )
    return cursor.fetchone() is not None


# Creates the tables on page load.
# It will then loop over the array of create_table, for each it will execute via for loop


def create_tables():
    # Create a Array of tables to create
    create_table = [
        """
        CREATE TABLE IF NOT EXISTS users (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL UNIQUE,
            Password TEXT NOT NULL,
            Admin TEXT NOT NULL
        )
    """,
        """
        CREATE TABLE IF NOT EXISTS data (
            LOCATION STRING NOT NULL PRIMARY KEY,
            COMMENT STRING NOT NULL
        )
    """,
        """
            CREATE TABLE IF NOT EXISTS assignmentGroup(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LOCATION TEXT NOT NULL,
            JOBROLE STRING NOT NULL,
            COMPANY STRING NOT NULL,
            FOREIGN KEY (LOCATION) REFERENCES data (LOCATION)
        )
    """,
    ]
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        # then loop over the list
        for table in create_table:
            # Use regex to search for the table name in for loop
            match = re.search(r"CREATE TABLE IF NOT EXISTS (\w+)", table)
            if match:
                table_name = match.group(1)
                # Check if the table already exists
                if not table_exists(cursor, table_name):
                    cursor.execute(table)
                    conn.commit()
                else:
                    return "Table Exists"
    except sqlite3.Error as exception:
        return "Error" + str(exception)
    finally:
        conn.close()


# Runs on register form submit, checks if user exists = true then it will not allow to register
# If the user doesn't exist then this will register the user.


def check_and_register_user(user_id, password):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        # Check if the user with the given user_id already exists
        cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
        existing_user = cursor.fetchone()
        # if condition = true return the string
        if existing_user:
            # User is present in users table
            return "User already exists in the database."
        else:
            # Write the user to the 'users' table if previous condition = false
            if len(user_id) >= 4 and len(password) >= 4:
                try:
                    # Assigns the parameters to an class
                    password_bytes = password.encode("utf-8")
                    salt = bcrypt.gensalt()
                    hashed = bcrypt.hashpw(password_bytes, salt)

                    new_user = User(user_id, hashed, "no")
                    cursor.execute(
                        "INSERT INTO users (user_id, Password, Admin) VALUES (?, ?, ?)",
                        (new_user.user_id, new_user.password, new_user.admin_privilege),
                    )
                    conn.commit()
                    return "Success, User has been registered"
                except:
                    return "error"
            else:
                return "Error Invalid Input"
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()


# Check Login Credentials, strips the username and password for whitespace
# Checks if the user exists, if does login, else throw error.


def check_login_check(username, password):
    # Gets the parameters for the username & password and removes whitespace.
    # Decided to use placeholders, instead of a string for added security.
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        if username and username.strip() and password and password.strip():
            cursor.execute(
                "SELECT * from users WHERE user_id = ? AND password = ?",
                (username, password),
            )
            # Fetchs one record using fetchone()
            user = cursor.fetchone()
            # Checks if the user exists
            if user:
                # Assigns each column to my class
                retuned_record = User(user[1], user[2], user[3])
                # Checks if the entered password & username match the record, return the relevant success / error message
                if (
                    retuned_record.password == password
                    and retuned_record.user_id == username
                ):
                    return "Logged In Successfully"
                else:
                    return "Invalid password"
            else:
                return "User does not exist"
        else:
            return "Please Enter Valid Inputs"
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()


# Display Data Method will select all from the table, loop over rows and create new data record


def display_data():
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        # Executes the SQL Query
        cursor.execute(
            "SELECT data.LOCATION,data.comment,assignmentGroup.JOBROLE,assignmentGroup.COMPANY FROM data JOIN assignmentGroup ON data.LOCATION = assignmentGroup.LOCATION"
        )
        # Fetches all the rows associated to the query
        rows = cursor.fetchall()
        record_list = []
        # For each row in the fetched rows, create new DataRecord object and assign values and append to previous object
        for record in rows:
            data_record = DataRecord(record[0], record[1], record[2], record[3])
            record_list.append(data_record)
        # Close Connection
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()
    # Returns the object
    return record_list


# Retrieve a User Record, match record and then create a new user class


def get_user_record(username, password):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    # Executes the SQL Query
    try:
        cursor.execute(
            "SELECT * FROM users WHERE user_id = ? and Password = ?",
            (
                username,
                password,
            ),
        )
        user = cursor.fetchall()

        matched_record = []
        # Loop over all the records
        for matched_user in user:
            matched_user_record = User(
                matched_user[1], matched_user[2], matched_user[3]
            )
            # Once i've created my user class append to list
            matched_record.append(matched_user_record)
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()
    return matched_record


# Deleting From SQL Script


def delete_row(location):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        cursor.execute("select * from data WHERE Location = ?", (location,))
        row_present = cursor.fetchall()

        if row_present:
            # Executes the SQL Query via DELETE
            delete_row = [
                ("DELETE FROM data WHERE Location = ?", (location,)),
                ("DELETE FROM assignmentGroup WHERE Location = ?", (location,)),
            ]
            # loop over list per delete statement
            for delete_row, values in delete_row:
                cursor.execute(delete_row, values)

            conn.commit()
            return "success"
        else:
            return "error"
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()


# Inserting Row function


def inserting_row(location, comment, jobRole, company):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        cursor.execute("SELECT * FROM data where Location =?", (location,))
        location_exists = cursor.fetchall()
        # Checks if the record exsists
        if location_exists:
            return "Location already is in data, no duplicates allowed"
        else:
            # Execute the SQL query using wildcard
            insert_row = {
                (
                    "INSERT INTO data (Location, Comment) VALUES (?, ?)",
                    (location, comment),
                ),
                (
                    "INSERT INTO assignmentGroup (LOCATION, JOBROLE, COMPANY) VALUES (?, ?, ?)",
                    (location, jobRole, company),
                ),
            }
            # Loop over my list for insert statement
            for insert, values in insert_row:
                cursor.execute(insert, values)

            conn.commit()
            return "success"
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()


# Updating Location
def update_location(oldLocation, newLocation):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        # See if the record is present in the DB with the old location name
        cursor.execute("select * from data WHERE Location = ?", (newLocation,))
        exisitng_location = cursor.fetchall()
        # Checks if the record exsists
        if exisitng_location:
            return "Error - New location already exists in the database"
        else:
            cursor.execute("select * from data WHERE Location = ?", (oldLocation,))
            location_record = cursor.fetchall()

            if location_record:
                # Execute the SQL to update Location
                cursor.execute(
                    "UPDATE data SET Location =? WHERE Location = ? ",
                    (newLocation, oldLocation),
                )
                conn.commit()
                return "Successfully Updated Row"
            else:
                return "Error - Record with Location not found"
    except:
        print("Error")
    finally:
        conn.close()


# Updating comment


def update_comment(location, comment, jobrole, company):
    try:
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    try:
        # See if the record is present in the DB with the old comment
        cursor.execute("select * from data WHERE LOCATION = ?", (location,))
        existing_comment = cursor.fetchall()
        # If the record is existing then we don't want to over ride it / throw error
        if not existing_comment:
            return "Error - Location doesn't exist in the database"
        else:
            # Selects the all comment from the DB
            cursor.execute("select * from data WHERE LOCATION = ?", (location,))
            comment_record = cursor.fetchall()

            if comment_record:
                cursor.execute(
                    "UPDATE data SET Comment = ? WHERE Location = ? ",
                    (comment, location),
                )
                cursor.execute(
                    "UPDATE assignmentGroup SET JOBROLE = ?, COMPANY = ? WHERE Location = ? ",
                    (jobrole, company, location),
                )
                conn.commit()
                return "Successfully Updated Row"
            else:
                return "Error - Record with Comment not found"
    except sqlite3.Error as exception:
        print("Error" + str(exception))
    finally:
        conn.close()
