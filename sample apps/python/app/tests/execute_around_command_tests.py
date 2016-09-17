import unittest

from app.shared.console_logger import log_info, log_error
from app.shared.execute_around_command import timer, around, compensate
from execute_around_command_fixture import ExecuteAroundCommandFixture


class ExecuteAroundCommandTestCase(unittest.TestCase):
    """"Tests for 'execute_around_command.py'"""

    def setUp(self):
        self.fixture = ExecuteAroundCommandFixture()

    def test_timer_logs_duration(self):
        target = timer(self.fixture.log_info)
        target(self.fixture.action_stub, lambda: "test description")
        self.assertIn("DURATION", self.fixture.get_message())

    def test_timer_executes_expected_action(self):
        target = timer(self.fixture.log_info)
        target(self.fixture.action_stub, lambda: "test description")
        self.assertEqual(True, self.fixture.has_executed())

    def test_around_logs_before_and_after(self):
        target = around(self.fixture.log_info)
        target(self.fixture.action_stub, lambda: "test description")
        self.assertIn("BEGIN", self.fixture.get_message())
        self.assertIn("END", self.fixture.get_message())

    def test_compensate_logs_duration(self):
        with self.assertRaises(ValueError):
            target = compensate(log_error, log_info)
            target(self.query_raises_error, lambda: "test description")
            self.assertIn("FAILED", self.current_message)

    def test_compensate_raises_expected_exception(self):
        with self.assertRaises(ValueError):
            target = compensate(log_error, log_info)
            target(self.query_raises_error, lambda: "test description")

    @staticmethod
    def query_raises_error():
        raise ValueError("test error")

    def log_info(self, message):
        self.current_message = self.current_message + message

    def log_error(self, message):
        self.current_message = self.current_message + message


if __name__ == '__main__':
    unittest.main()
