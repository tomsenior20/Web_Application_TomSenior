from flask import Flask, flash, render_template
from method import *

# Login Function


def check_login(user_id, logInPassword):
    # Check for null values in form data
    if not all((user_id.strip(), logInPassword.strip())):
        login_message = "Please fill in all fields."
    elif len(user_id.strip()) < 4 or len(logInPassword.strip()) < 4:
        login_message = "Password or Username is less than required characters"
    else:
        # Goes to method.py to validate against DB
        check_login = check_login_check(user_id, logInPassword)
        if check_login == "Logged In Successfully":
            login_message = check_login
        elif check_login == "invalid password" or "User does not exsist" or "Please Enter Valid Inputs":
            login_message = check_login
    return login_message


# Registers the user function
def check_register(full_name, password, admin_privilege):
    # Check for null values in form data
    if not all((full_name.strip(), password.strip(), admin_privilege.strip())):
        msg = "Please Fill out all Inputs"
    # Handles all scenarios to when char are less than 4 or admin priv is not equal to the string, removes whitespace using .strip()
    elif len(full_name.strip()) < 4 or len(password.strip()) < 4 or (admin_privilege.strip() != "yes" and admin_privilege.strip() != "no"):
        msg = 'one of the mininum inputs requirements havent been met'
    else:
        # Goes to Method.PY to fetch the data and check if exsists if not store.
        returned_register_message = check_and_register_user(
            full_name, password, admin_privilege)
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


def insert_row(location, comment):
    # Check if the location passed is null or not
    if not (location and comment):
        status_msg = 'Invalid inputs'
    else:
        status_check_insert = inserting_row(location, comment)
        # Checks if the response is succefull or not
        if status_check_insert == "success":
            status_msg = "Row Successfully Inserted"
        else:
            status_msg = "Erorr Inserting Row"

    return status_msg

# Update Row


def update_row_attempt(currentLocation, newLocation, currentComment, newComment):
    update_msg = None
    attempt_comment_update = None
    attempt_location_update = None

    if currentComment and newComment and not (currentLocation and newLocation):
        attempt_comment_update = update_comment(currentComment, newComment)
    elif currentLocation and newLocation and not (currentComment or newComment):
        attempt_location_update = update_location(currentLocation, newLocation)
    elif currentComment and newComment and currentLocation and newLocation:
        attempt_comment_update = update_comment(currentComment, newComment)
        attempt_location_update = update_location(currentLocation, newLocation)

    if attempt_comment_update == 'Successfully Updated Row' or attempt_location_update == 'Successfully Updated Row':
        update_msg = 'Update Successful'
    else:
        update_msg = attempt_location_update or attempt_comment_update

    return update_msg
