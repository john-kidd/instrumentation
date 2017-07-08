import unittest

from app.shared.console_logger import log_info, log_error
from app.shared.execute_around_command import time, wrap, handle_error


class ExecuteAroundCommandTestCase(unittest.TestCase):
    """"Tests for 'execute_around_command.py'"""

    def setUp(self):
        """ configure the test case"""
        self.action_executed = False
        self.current_message = ""

    def test_time_logs_duration(self):
        target = time(self.log_info_stub)
        target(self.action_stub, lambda: "test description")
        self.assertIn("DURATION", self.current_message)

    def test_time_executes_expected_action(self):
        target = time(self.log_info_stub)
        target(self.action_stub, lambda: "test description")
        self.assertEqual(True, self.action_executed)

    def test_wrap_logs_before_and_after(self):
        target = wrap(self.log_info_stub)
        target(self.action_stub, lambda: "test description")
        self.assertIn("BEGIN", self.current_message)
        self.assertIn("END", self.current_message)

    def test_handle_error_logs_duration(self):
        with self.assertRaises(ValueError):
            target = handle_error(log_error, log_info)
            target(self.action_raises_error_stub, lambda: "test description")
            self.assertIn("FAILED", self.current_message)

    def test_handle_error_raises_expected_exception(self):
        with self.assertRaises(ValueError):
            target = handle_error(log_error, log_info)
            target(self.action_raises_error_stub, lambda: "test description")

    """ fixture """
    @staticmethod
    def action_raises_error_stub():
        raise ValueError("test error")

    def log_info_stub(self, message):
        self.current_message = self.current_message + message

    def log_error_stub(self, message):
        self.current_message = self.current_message + message

    def action_stub(self):
        self.action_executed = True

if __name__ == '__main__':
    unittest.main()
