from flask import Flask, flash,render_template
from method import *

# Login Function
def check_login(user_id,logInPassword):
    # Check for null values in form data
    if not all((user_id.strip(),logInPassword.strip())):
        flash('Please fill in all fields.', 'error')
        login_message = "error"
    elif len(user_id.strip()) < 4 or len(logInPassword.strip()) < 4:
        flash('Password or Username is less than required characters.', 'error')
        login_message = "error"
    else:
        # Goes to method.py to validate against DB
        check_login = check_login_check(user_id,logInPassword)
        if check_login == "success":
            flash("Success", 'success')
            login_message = "success"
        elif check_login == "invalid password" or "User does not exsist":
            login_message = "error"
            flash('Error', 'error')
    return login_message


# Registers the user function
def check_register(full_name,password,admin_privilege):
    # Check for null values in form data
    if not all((full_name.strip(), password.strip() , admin_privilege.strip())):
        msg = "Error, Invalid Input"
    # Handles all scenarios to when char are less than 4 or admin priv is not equal to the string, removes whitespace using .strip()
    elif len(full_name.strip()) < 4 or len(password.strip()) < 4 or (admin_privilege.strip() != "yes" and admin_privilege.strip() != "no"):
        msg = 'Error Invalid Input'
    else:
        # Goes to Method.PY to fetch the data and check if exsists if not store.
        returned_register_message = check_and_register_user(full_name,password,admin_privilege)
        # Check the Message returned and assign a msg to it
        if returned_register_message == "Success, User has been registered":
            msg = "Success, User has been registered"
        elif returned_register_message == "User already exists in the database.":
            msg = "User already exists in the database."

    return msg

# Deletion of Row Function
def check_delete(location):
    # Check if the location passed is null or not
    if not location:
       flash("Please fill out Location Input",'error')
       delete_msg = 'error'
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
        flash("Invlalid inputs", 'error')
        status_msg = 'error'
    else:
        status_check_insert = inserting_row(location,comment)
        #Checks if the response is succefull or not 
        if status_check_insert == "success":
            status_msg = "Row Successfully Inserted"
        else:
            status_msg = "Erorr Inserting Row"
            
    return status_msg

# Update Row
def update_row_attempt(currentLocation, newLocation,currentComment,newComment):
    update_msg = None
    attempt_comment_update = None
    attempt_location_update = None
    
    if currentComment and newComment and not (currentLocation and newLocation):
        attempt_comment_update = update_comment(currentComment, newComment)
    elif currentLocation and newLocation and not (currentComment or newComment):
        attempt_location_update = update_location(currentLocation,newLocation)
    elif currentComment and newComment and currentLocation and newLocation:
        attempt_comment_update = update_comment(currentComment, newComment)
        attempt_location_update = update_location(currentLocation,newLocation)
        
    if attempt_comment_update == 'Successfully Updated Row' or attempt_location_update  == 'Successfully Updated Row':
        update_msg = 'Update Successful'
    else:
            update_msg = attempt_location_update or attempt_comment_update
          
    return update_msg