import unittest

from ..app.console_logger import log_info
from ..app.models import Contact
from ..app.validators import validate_input


class ModelTestCase(unittest.TestCase):
    """Tests for `models.py`."""

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
            Contact("John F Kidd", "075535533", None)

    def test_contact_with_invalid_email_raises_expected_error(self):
        c = Contact("John F Kidd", "+4478866662", "john.test.com")

        with self.assertRaises(ValueError):
            validate_input(log_info, c)


if __name__ == '__main__':
    unittest.main()
