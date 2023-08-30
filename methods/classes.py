# Creates the User Class
class User:
    def __init__(self, user_id, password, admin_privilege):
        self.user_id = user_id
        self.password = password
        self.admin_privilege = admin_privilege
# Creates the Data Record class
class DataRecord:
    def __init__(self, Location, comment, jobrole, company):
        self.Location = Location
        self.comment = comment
        self.jobrole = jobrole
        self.company = company
