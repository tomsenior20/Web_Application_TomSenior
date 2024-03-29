from flask import Flask, flash, render_template
from methods.method import *

# Login Function, checks the validation and then continue to check_login_check


def check_login(user_id, logInPassword):
    user_id = user_id.strip()
    logInPassword = logInPassword.strip()
    # Check for null values in form data
    if not all((user_id, logInPassword)):
        return "Please fill in all fields."
    # Ensure Greater than 4 char
    elif len(user_id) < 4 or len(logInPassword) < 4:
        return "Password or Username is less than required characters"
    # Ensure Password and UserNames don't match
    elif user_id == logInPassword:
        return "Username or password cannot match"
    else:
        # Goes to method.py to validate against DB
        check_login = check_login_check(user_id, logInPassword)
        if check_login == "Logged In Successfully":
            return check_login
        elif (
            check_login == "invalid password"
            or "User does not exsist"
            or "Please Enter Valid Inputs"
        ):
            return check_login


# Registers the user function then to ensure Validation before continuing to check_and_register_user
def check_register(full_name, password):
    fullname = full_name.strip()
    password = password.strip()

    # Check for null values in form data
    if not all((fullname, password)):
        return "Please Fill out all Inputs"
    # Handles all scenarios to when char are less than 4 -  removes whitespace using .strip()
    elif len(fullname) < 4 or len(password) < 4:
        return "one of the mininum inputs requirements havent been met"
    # Ensure Username and password don't match
    elif fullname == password:
        return "Username and password Cannot be the same"
    else:
        # Goes to Method.PY to fetch the data and check if exsists if not store.
        returned_register_message = check_and_register_user(fullname, password)
        # Check the Message returned and assign a msg to it
        if returned_register_message == "Success, User has been registered":
            return returned_register_message
        elif returned_register_message == "User already exists in the database.":
            return returned_register_message


# Deletion of Row Function

# checks the check_delete function validation then continue to delete_row()


def check_delete(location):
    # Check if the location passed is null or not
    if not location:
        return "Please fill out Location Input"
    else:
        # Go to method.py and perform the SQL Script to delete
        attempt_delete = delete_row(location)
        # Based on the returned messaged you will show an message
        if attempt_delete == "success":
            return "Row Deleted"
        else:
            return "error"


# Inserting Row Function, adds validation before continuing to inserting_row


def insert_row(location, comment, jobRole, company):
    # Check if the location passed is null or not
    if not (location and comment) or not (jobRole and company) or len(location) < 4:
        return "One of the inputs are invalid"
    else:
        status_check_insert = inserting_row(location, comment, jobRole, company)
        # Checks if the response is success or not
        if status_check_insert == "success":
            return "Row Successfully Inserted"
        else:
            return "Erorr Inserting Row"


# Update Row, checks validation before continuing to update_comment


def update_row_attempt(location, comment, jobrole, company):
    attempt_comment_update = None
    location = location.strip()
    comment = comment.strip()
    jobrole = jobrole.strip()
    company = company.strip()

    # Checks for the user comment is not null and above 2 characters
    if location and comment and jobrole and company:
        attempt_comment_update = update_comment(location, comment, jobrole, company)
    # If the new and old commend is none then return message
    elif not comment and not jobrole and company:
        return "Either current or new commend is invalid"
    # Default Error to return
    else:
        return "Updated of comment failed"
    # Gets Response from my attempt to update comment
    if attempt_comment_update == "Successfully Updated Row":
        return "Update Successful"
