import unittest
from console_logger import log_info
from validators import validate_input
from model import Contact
from model import ContactId
from execute_around_query import timer
from execute_around_query import around

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


class ContactIdTestCase(unittest.TestCase):
    """Tests for `model.py`."""


    def test_contact_id_with_empty_id_raises_expected_error(self):
        with self.assertRaises(ValueError):
            ContactId(None)


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""


    def test_timer_logs_duration(self):
        query = timer(log_info)
        result = query(lambda : "test", lambda : "test description")
        self.assertEqual("test", result)


    def test_around_logs_duration(self):
        query = around(log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEqual("test", result)


if __name__ == '__main__':
    unittest.main()