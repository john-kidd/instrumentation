import unittest
from console_logger import log_info
from validators import validate_input
from model import Contact

class ModelTestCase(unittest.TestCase):
    """Tests for `model.py`."""

    def test_contact_with_empty_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact("", "076363633", "john@test.com")


    def test_contact_with_no_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact(None, "076363633", "john@test.com")


    def test_contact_with_emoty_mobile_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact("John F Kidd", "", "john@test.com")


    def test_contact_with_no_mobile_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact("John F Kidd", None, "john@test.com")


    def test_contact_with_empty_email_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact("John F Kidd", "075535533", "")


    def test_contact_with_no_email_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact("John F Kidd", "075535533",  None)


    def test_contact_with_invalid_email_raises_expected_error(self):
        c = Contact("John F Kidd", "+4478866662", "john.test.com")

        with self.assertRaises(ValueError):
            validate_input(log_info, c)

if __name__ == '__main__':
    unittest.main()