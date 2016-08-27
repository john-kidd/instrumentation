import unittest

from ..app.shared.console_logger import log_info
from ..app.models import Contact
from ..app.shared.guard import validate_input


class ModelTestCase(unittest.TestCase):
    """Tests for `models.py`."""

    def test_contact_with_empty_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("", "076363633", "john@test.com", None)

    def test_contact_with_no_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create(None, "076363633", "john@test.com", None)

    def test_contact_with_emoty_mobile_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("John F Kidd", "", "john@test.com", None)

    def test_contact_with_no_mobile_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("John F Kidd", None, "john@test.com", None)

    def test_contact_with_empty_email_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("John F Kidd", "075535533", "", None)

    def test_contact_with_no_email_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("John F Kidd", "075535533", None, None)


if __name__ == '__main__':
    unittest.main()
