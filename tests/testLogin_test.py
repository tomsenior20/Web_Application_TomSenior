from methods.auth import check_login
# from methods.auth import *
import unittest
# Patch allows for me to mock the method
from unittest.mock import patch

class TestInsertRow(unittest.TestCase):
    # Unit Test for Log in Methods
    @patch('methods.auth.check_login')
    def test_successful_login(self, mock_successfull_login):
        mock_successfull_login = "success"
        # Passing in valid credentials in DB
        result = check_login("admin", "admin1")
        self.assertEqual(result, "Logged In Successfully")
        print("@test_successful_login ~ Test Ran Successfully")

    @patch('methods.auth.check_login')
    def test_failed_login(self, mock_invalid_login):
        # Setting Scenario for lower than char length
        result = check_login("sss", "ss")
        self.assertEqual(
            result, "Password or Username is less than required characters")
        print("@test_failed_login ~ Test Ran Successfully ")

    @patch('methods.auth.check_login')
    def test_invalid_inputs(self, mock_invalid_login):
        # Testing For Empty Inputs which should throw below error
        result = check_login("", "")
        self.assertEqual(result, "Please fill in all fields.")
        print("@test_invalid_inputs ~ Test Ran Successfully")
        
if __name__ == '__main__':
    unittest.main()
