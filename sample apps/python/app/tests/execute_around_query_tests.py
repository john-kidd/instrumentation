import unittest
import uuid

from app.get_contact import get_description, query
from app.models import Contact
from app.models import ContactId
from app.shared.console_logger import log_info, log_error
from app.shared.execute_around_query import log_wrap
from app.shared.execute_around_query import log_time, handle_error


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""

    def setUp(self):
        """ configure the test case"""
        self.contact_id_stub = ContactId(uuid.uuid4())
        self.current_message = ""
        self.expected_contact = self.get_contact_by_id_stub(self.contact_id_stub)
        self.query = query(self.get_contact_by_id_stub)

    def test_long_time_duration(self):
        target = log_time(self.log_info_stub)
        target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIn("DURATION", self.current_message)

    def test_long_time_returns_expected_value(self):
        target = log_time(log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIsNotNone(result.contact_id)

    def test_log_wrap_logs_before_and_after(self):
        target = log_wrap(self.log_info_stub)
        target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIn("BEGIN", self.current_message)
        self.assertIn("END", self.current_message)

    def test_around_returns_expected_value(self):
        target = log_wrap(log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertEqual(self.expected_contact.contact_id, result.contact_id)

    def test_handle_error_logs_duration(self):
        with self.assertRaises(ValueError):
            target = handle_error(log_error, log_info)
            target(self.query_raises_error_stub, get_description)
            self.assertIn("FAILED", self.current_message)

    def test_handle_error_returns_expected_value(self):
        target = handle_error(log_error, log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertEqual(self.expected_contact.contact_id, result.contact_id)

    def test_handle_error_raises_expected_exception(self):
        with self.assertRaises(ValueError):
            target = handle_error(log_error, log_info)
            target(self.query_raises_error_stub, get_description)

    @staticmethod
    def query_raises_error_stub():
        raise ValueError("test error")

    def log_info_stub(self, message):
        self.current_message = self.current_message + message

    def log_error_stub(self, message):
        self.current_message = self.current_message + message

    @staticmethod
    def get_contact_by_id_stub(contact_id):
        return Contact.create("John F Kidd", "+4478866662", "john@test.com", contact_id)

if __name__ == '__main__':
    unittest.main()
