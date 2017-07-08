import unittest

from app.models import Contact


class ContactModelTestCase(unittest.TestCase):
    """Tests for `Contact - models.py`."""

    def test_contact_with_empty_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create("", "076363633", "john@test.com", None)

    def test_contact_with_no_name_raises_expected_error(self):
        with self.assertRaises(ValueError):
            Contact.create(None, "076363633", "john@test.com", None)

    def test_contact_with_empty_mobile_raises_expected_error(self):
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

    def test_contact_with_invalid_email_address_returns_expected_value(self):
        contact_stub = Contact.create("John F Kidd", "0776666621", "j.test.com")
        actual = contact_stub.is_valid()
        self.assertFalse(actual)

    def test_contact_to_string(self):
        name_stub = "John F Kidd"
        mobile_stub = "0776666621"
        email_address_stub = "j@test.com"
        target = Contact.create(name_stub, mobile_stub, email_address_stub)
        expected = "\tContact\n\t{}\n\t\tName: {}\n\t\tMobile: {}\n\t\tEmail: {}\n\t\tComments: {}\n\t\tValid: {}"\
            .format(
                target.contact_id,
                target.name,
                target.mobile,
                target.email,
                target.comments,
                target.is_valid())
        actual = target.__str__()
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
