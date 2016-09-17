import unittest
import uuid
import app.tests.db_stub
from app.shared.console_logger import log_info, log_error
from app.shared.execute_around_query import around
from app.shared.execute_around_query import timer, compensate
from app.models import ContactId
from app.get_contact import get_description, query


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""

    def setUp(self):
        self.contact_id_stub = ContactId(uuid.uuid4())
        self.current_message = ""
        self.expected_contact = app.tests.db_stub.get_contact_by_id(self.contact_id_stub)
        self.query = query(app.tests.db_stub.get_contact_by_id)

    def test_timer_logs_duration(self):
        target = timer(self.log_info)
        target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIn("DURATION", self.current_message)

    def test_timer_returns_expected_value(self):
        target = timer(log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIsNotNone(result.contact_id)

    def test_around_logs_before_and_after(self):
        target = around(self.log_info)
        target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertIn("BEGIN", self.current_message)
        self.assertIn("END", self.current_message)

    def test_around_returns_expected_value(self):
        target = around(log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertEqual(self.expected_contact.contact_id, result.contact_id)

    def test_compensate_logs_duration(self):
        with self.assertRaises(ValueError):
            target = compensate(log_error, log_info)
            target(self.query_raises_error, get_description)
            self.assertIn("FAILED", self.current_message)

    def test_compensate_returns_expected_value(self):
        target = compensate(log_error, log_info)
        result = target(lambda: self.query(self.contact_id_stub), get_description)
        self.assertEqual(self.expected_contact.contact_id, result.contact_id)

    def test_compensate_raises_expected_exception(self):
        with self.assertRaises(ValueError):
            target = compensate(log_error, log_info)
            target(self.query_raises_error, get_description)

    @staticmethod
    def query_raises_error():
        raise ValueError("test error")

    def log_info(self, message):
        self.current_message = self.current_message + message

    def log_error(self, message):
        self.current_message = self.current_message + message


if __name__ == '__main__':
    unittest.main()
