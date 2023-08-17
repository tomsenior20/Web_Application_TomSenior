from flask import Flask, render_template, request, flash,jsonify,session
from method import create_users_table, display_data
from auth import *
import pdb

app = Flask(__name__)
app.config['DEBUG']= True
app.config['SECRET_KEY'] = 'Senior'

returned_user = None
user_id = None
password = None

@app.route('/')
def hello():
    # CREATES THE DATABASE IF THEY DON'T EXSIST
    create_users_table()
    return render_template("index.html")

# Log In function
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        # Gets the Username and Password from form
        user_id = request.form.get('UserID')
        password = request.form.get('Password')
        # Goes to auth.py to handle the data and check Entered password matches entered
        returned_message = check_login(user_id,password)
        # Returned data from the Data Table

    if returned_message == "Logged In Successfully":
        # Goes to the Display_Data method to display data from Data Table on success
        session['UserID'] = user_id
        session['Password'] = password
        returned_data = display_data()
        returned_user = get_user_record(user_id,password)
        # Flash Message is shown based of the returned message
        flash(returned_message, "success")
        return render_template("home.html", returned_data=returned_data, returned_user=returned_user)
    else:
        # Flash Message is shown based of the returned message
        flash(returned_message, "error")
        return render_template("index.html")

# Routing for Register Function
@app.route('/register', methods=['POST'])
def register():
    if request.method == "POST":
        # Gets the form value for all attributes
        full_name = request.form.get('registerUserID')
        password = request.form.get('registerPassword')
        # Sets Default on register to no admin
        admin_privilege = "no"
        # Goes to auth.py to handle the data
        returned_message = check_register(full_name, password)

        # Based on condition, this will always render back to index.html
        if returned_message == "Success, User has been registered":
            flash(returned_message, 'success')
            return render_template("index.html")
        else:
            flash(returned_message, "error")
            return render_template("index.html")

# Routing for the Log out button 
@app.route('/redirect')
def redirect_to_index():
    # If Logout is requested this will send the user back to the Log In Page
        return render_template('index.html')

# Delete Row Function
@app.route('/delete_row_attempt', methods=["POST"])
def delete_row_attempt():
    if request.method == "POST":
        # Get Form Input for delete
        row_to_delete = request.form.get('nameDelete')
        # Check delete Section
        checking_delete = check_delete(row_to_delete)
        # Checked for Success message from check_delete and handle correctly
        if checking_delete == "Row Deleted":
            flash(checking_delete, 'success')
        else:
            flash(checking_delete, 'error')
        # Return Data to the page
        returned_data = display_data()
        # Get the Saved username and password from storage and pass in as param to show / hide correct buttons
        user_id = session.get('UserID')
        password = session.get('Password')
        returned_user = get_user_record(user_id,password)
            
    return render_template('home.html',returned_data=returned_data,returned_user=returned_user)

# Insert Row function 
@app.route('/insert_row_attempt', methods=["POST"])
def insert_row_attempt():
    if request.method == "POST":
        # Get Form Input for Insert
        location_to_insert = request.form.get('nameInsert')
        comment_to_insert = request.form.get('commentInsert')
        jobRole_to_insert = request.form.get('jobRole')
        company_to_insert = request.form.get('companyInsert')
        # Check insert Section and remove whitespace if accidentally added
        checking_insert = insert_row(location_to_insert.strip(),comment_to_insert.strip(), jobRole_to_insert.strip(), company_to_insert.strip())
        # Checked for Success message from insert_row and handle correctly
        if checking_insert == "Row Successfully Inserted":
            flash(checking_insert, 'success')
        else:
            flash(checking_insert, 'error')
        # Return Data to the page after form submit
        returned_data = display_data()
        # Get the Saved username and password from storage and pass in as param to show / hide correct buttons
        user_id = session.get('UserID')
        password = session.get('Password')
        returned_user = get_user_record(user_id,password)
            
        return render_template('home.html',returned_data=returned_data,returned_user=returned_user)

# Update Row Function
@app.route('/update_row', methods=["POST"])
def update_row():
    if request.method == "POST":
        # Get Form Input for Update
        current_comment = request.form.get('currentComment')
        new_comment = request.form.get('newComment')
        # Check update row  Section and remove whitespace if accidentally added
        attemping_update = update_row_attempt(current_comment.strip(), new_comment.strip())
        # Checked for Success message from update_row_attempt and handle correctly
        if attemping_update == "Update Successful":
            flash(attemping_update, 'success')
        else:
            flash(attemping_update, 'error')
        # Return Data to the page after form submit
        returned_data = display_data()
        # Get the Saved username and password from storage and pass in as param to show / hide correct buttons
        user_id = session.get('UserID')
        password = session.get('Password')
        returned_user = get_user_record(user_id,password)
            
    return render_template('home.html',returned_data=returned_data,returned_user=returned_user)

if __name__ == '__main__':
    app.run(debug=True)
