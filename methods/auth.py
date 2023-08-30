from flask import Flask, flash, render_template
from methods.auth import *
from methods.method import *

# Login Function


def check_login(user_id, logInPassword):
    # Check for null values in form data
    if not all((user_id.strip(), logInPassword.strip())):
        login_message = "Please fill in all fields."
    elif len(user_id.strip()) < 4 or len(logInPassword.strip()) < 4:
        login_message = "Password or Username is less than required characters"
    elif user_id == logInPassword:
        login_message = "Username or password cannot match"
    else:
        # Goes to method.py to validate against DB
        check_login = check_login_check(user_id, logInPassword)
        if check_login == "Logged In Successfully":
            login_message = check_login
        elif check_login == "invalid password" or "User does not exsist" or "Please Enter Valid Inputs":
            login_message = check_login
    return login_message


# Registers the user function
def check_register(full_name, password):
    # Check for null values in form data
    if not all((full_name.strip(), password.strip())):
        msg = "Please Fill out all Inputs"
    # Handles all scenarios to when char are less than 4 -  removes whitespace using .strip()
    elif len(full_name.strip()) < 4 or len(password.strip()) < 4:
        msg = 'one of the mininum inputs requirements havent been met'
    elif full_name.strip() == password.strip():
        msg = "Username and password Cannot be the same"
    else:
        # Goes to Method.PY to fetch the data and check if exsists if not store.
        returned_register_message = check_and_register_user(
            full_name, password)
        # Check the Message returned and assign a msg to it
        if returned_register_message == "Success, User has been registered":
            msg = returned_register_message
        elif returned_register_message == "User already exists in the database.":
            msg = returned_register_message

    return msg

# Deletion of Row Function


def check_delete(location):
    # Check if the location passed is null or not
    if not location:
        delete_msg = 'Please fill out Location Input'
    else:
        # Go to method.py and perform the SQL Script to delete
        attempt_delete = delete_row(location)
        # Based on the returned messaged you will show an message
        if attempt_delete == 'success':
            delete_msg = "Row Deleted"
        else:
            delete_msg = "error"

    return delete_msg

# Inserting Row Function


def insert_row(location, comment, jobRole, company):
    # Check if the location passed is null or not
    if not (location and comment) or not (jobRole and company) or len(location) < 4:
        status_msg = 'One of the inputs are invalid'
    else:
        status_check_insert = inserting_row(
            location, comment, jobRole, company)
        # Checks if the response is success or not
        if status_check_insert == "success":
            status_msg = "Row Successfully Inserted"
        else:
            status_msg = "Erorr Inserting Row"

    return status_msg

# Update Row


def update_row_attempt(currentComment, newComment):
    update_msg = None
    attempt_comment_update = None
    # Checks for the user comment is not null and above 2 characters
    if currentComment and newComment and len(newComment) > 2:
        attempt_comment_update = update_comment(currentComment, newComment)
    else:
        update_msg = 'error'
    # Gets Response from my attempt to update comment
    if attempt_comment_update == 'Successfully Updated Row':
        update_msg = 'Update Successful'

    return update_msg
