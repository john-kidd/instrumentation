import unittest
from ..app.execute_around_query import timer
from ..app.execute_around_query import around
from ..app.console_logger import log_info


class ExecuteAroundQueryTestCase(unittest.TestCase):
    """"Tests for 'execute_around_query.py'"""

    def test_timer_logs_duration(self):
        query = timer(log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEqual("test", result)

    def test_around_logs_duration(self):
        query = around(log_info)
        result = query(lambda: "test", lambda: "test description")
        self.assertEqual("test", result)


if __name__ == '__main__':
    unittest.main()
