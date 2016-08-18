import unittest
from ..app.execute_around_query import timer
from ..app.execute_around_query import around
from ..app.console_logger import log_info


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

    def _log_info(self, message):
        self.current_message = self.current_message + message


if __name__ == '__main__':
    unittest.main()
