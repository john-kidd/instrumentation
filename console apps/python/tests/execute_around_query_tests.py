import unittest
import uuid
from ..app.shared.console_logger import log_info, log_error
from ..app.shared.execute_around_query import around
from ..app.shared.execute_around_query import timer, compensate
from ..app.queries import GetContact
from ..app.models import ContactId
import db_stub


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""

    def setUp(self):
        self.contact_id_stub = ContactId(uuid.uuid4())
        self.get_contact = GetContact(db_stub)
        self.current_message = ""
        self.expected_contact = db_stub.get_contact_by_id(self.contact_id_stub)

    def test_timer_logs_duration(self):
        query = timer(self._log_info)
        query(lambda: self.get_contact.query(self.contact_id_stub), self.get_contact.get_description)
        self.assertIn("DURATION", self.current_message)

    def test_timer_returns_expected_value(self):
        query = timer(log_info)
        result = query(lambda: self.get_contact.query(self.contact_id_stub), self.get_contact.get_description)
        self.assertIsNotNone(result.contact_id)

    def test_around_logs_before_and_after(self):
        query = around(self._log_info)
        query(lambda: self.get_contact.query(self.contact_id_stub), self.get_contact.get_description)
        self.assertIn("BEGIN", self.current_message)
        self.assertIn("END", self.current_message)

    def test_around_returns_expected_value(self):
        query = around(log_info)
        result = query(lambda: self.get_contact.query(self.contact_id_stub), self.get_contact.get_description)
        self.assertEquals(self.expected_contact.contact_id, result.contact_id)

    def test_compensate_logs_duration(self):
        with self.assertRaises(ValueError):
            query = compensate(log_error, log_info)
            query(self._query_raises_error, lambda: "test description")
            self.assertIn("FAILED", self.current_message)

    def test_compensate_returns_expected_value(self):
        query = compensate(log_error, log_info)
        result = query(lambda: self.get_contact.query(self.contact_id_stub), self.get_contact.get_description)
        self.assertEquals(self.expected_contact.contact_id, result.contact_id)

    def test_compensate_raises_expected_exception(self):
        with self.assertRaises(ValueError):
            query = compensate(log_error, log_info)
            query(self._query_raises_error, lambda: "test description")

    @staticmethod
    def _query_raises_error():
        raise ValueError("test error")

    def _log_info(self, message):
        self.current_message = self.current_message + message

    def _log_error(self, message):
        self.current_message = self.current_message + message


if __name__ == '__main__':
    unittest.main()
