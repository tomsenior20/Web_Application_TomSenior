from methods.auth import check_register
# from methods.auth import *
import unittest
# Patch allows for me to mock the method
from unittest.mock import patch

class TestInsertRow(unittest.TestCase):

    # Check for Greater than 4 char
    @patch('methods.auth.check_register')
    def test_invalid_reg(self, mock_text_reg):
        # Note this checks for < 4 characters
        result = check_register("dd", "ddd")
        self.assertEqual(
            result, 'one of the mininum inputs requirements havent been met')
        print("@test_invalid_reg ~ Test Ran Successfully ")

    # Checks for null entry
    @patch('methods.auth.check_register')
    def test_null_reg(self, mock_text_reg):
        # Note checks for null entries
        result = check_register("", "")
        self.assertEqual(
            result, 'Please Fill out all Inputs')
        print("@test_null_reg ~ Test Ran Successfully ")

    # Checks for valid name and password but incorrect admin
    @patch('methods.auth.check_register')
    def test_invalid_admin_reg(self, mock_text_reg):
        # Note checks for invalid admin entry
        result = check_register("testuser", "testuser")
        self.assertEqual(
            result, 'Username and password Cannot be the same')
        print("@test_invalid_admin_reg ~ Test Ran Successfully")

        
if __name__ == '__main__':
    unittest.main()
