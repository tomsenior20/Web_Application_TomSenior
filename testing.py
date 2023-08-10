import unittest
# Patch allows for me to mock the method
from unittest.mock import patch
from auth import check_login, check_register


class TestInsertRow(unittest.TestCase):
    # Unit Test for Log in Methods
    @patch('auth.check_login')
    def test_successful_login(self, mock_successfull_login):
        mock_successfull_login = "success"
        # Passing in valid credentials in DB
        result = check_login("admin", "admin")
        print("@test_successful_login - " + result)
        self.assertEqual(result, "Logged In Successfully")

    @patch('auth.check_login')
    def test_failed_login(self, mock_invalid_login):
        # Setting Scenario for lower than char length
        result = check_login("sss", "ss")
        print("@test_failed_login -  " + result)
        self.assertEqual(
            result, "Password or Username is less than required characters")

    @patch('auth.check_login')
    def test_invalid_inputs(self, mock_invalid_login):
        # Testing For Empty Inputs
        result = check_login("", "")
        print("@test_invalid_inputs - " + result)
        self.assertEqual(result, "Please fill in all fields.")

    # Testing the Registering

    # * note for TS will need to find a unique string each time it is ran, for this to work **

    # This needs to have unique entry each time or the test will fail
    # @patch('auth.check_register')
    # def test_valid_reg(self, mock_text_reg):
    #     # Note Before each test these needs to be unique
    #     result = check_register("dddd", "dddd", "yes")
    #     print("@test_valid_reg - " + result)
    #     self.assertEqual(result, "Success, User has been registered")

    # Check for Greater than 4 char
    @patch('auth.check_register')
    def test_invalid_reg(self, mock_text_reg):
        # Note this checks for < 4 characters
        result = check_register("dd", "ddd", "yes")
        print("@test_invalid_reg - " + result)
        self.assertEqual(
            result, 'one of the mininum inputs requirements havent been met')

    # Checks for null entry
    @patch('auth.check_register')
    def test_null_reg(self, mock_text_reg):
        # Note checks for null entries
        result = check_register("", "", "")
        print("@test_null_reg - " + result)
        self.assertEqual(
            result, 'Please Fill out all Inputs')

    # Checks for valid name and password but incorrect admin
    @patch('auth.check_register')
    def test_invalid_admin_reg(self, mock_text_reg):
        # Note checks for invalid admin entry
        result = check_register("testuser", "testuser", "hello")
        print("@test_invalid_admin_reg - " + result)
        self.assertEqual(
            result, 'one of the mininum inputs requirements havent been met')

    # Delete Functionality Unit Test


if __name__ == '__main__':
    unittest.main()
