import unittest

from ..app.shared.console_logger import log_info, log_error
from ..app.shared.execute_around_query import around
from ..app.shared.execute_around_query import timer, compensate


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""

    def setUp(self):
        self.current_message = ""

    def test_timer_logs_duration(self):
        query = timer(self._log_info)
        query(lambda: "test", lambda: "test description")
        self.assertIn("DURATION", self.current_message)

    def test_timer_returns_expected_value(self):
        query = timer(log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEqual("test", result)

    def test_around_logs_before_and_after(self):
        query = around(self._log_info)
        query(lambda: "test", lambda: "test description")
        self.assertIn("BEGIN", self.current_message)
        self.assertIn("END", self.current_message)

    def test_around_returns_expected_value(self):
        query = around(log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEqual("test", result)

    def test_compensate_logs_duration(self):
        with self.assertRaises(ValueError):
            query = compensate(log_error, log_info)
            query(self._query_raises_error, lambda: "test description")
            self.assertIn("FAILED", self.current_message)

    def test_compensate_returns_expected_value(self):
        query = compensate(log_error, log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEquals("test", result)

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
