import unittest
from unittest.mock import patch
from auth import check_login


class TestInsertRow(unittest.TestCase):
    @patch('auth.check_login')
    def test_successful_login(self, mock_loggin_row):
        # Passing in valid credentials in DB
        result = check_login("admin", "admin")
        print("successfunction - " + result)
        self.assertEqual(result, "Logged In Successfully")

    @patch('auth.insert_row')
    def test_failed_login(self, mock_loggin_row):
        # Setting Scenario for lower than char length
        result = check_login("sss", "ss")
        print("character failure -  " + result)
        self.assertEqual(
            result, "Password or Username is less than required characters")

    def test_invalid_inputs(self):
        # Testing For Empty Inputs
        result = check_login("", "")
        print("Empty string test - " + result)
        self.assertEqual(result, "Please fill in all fields.")


if __name__ == '__main__':
    unittest.main()
