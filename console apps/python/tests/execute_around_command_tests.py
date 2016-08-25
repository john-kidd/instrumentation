import unittest

from execute_around_command_fixture import ExecuteAroundCommandFixture
from ..app.shared.execute_around_command import timer, around


class ExecuteAroundCommandTestCase(unittest.TestCase):
    """"Tests for 'execute_around_command.py'"""

    def setUp(self):
        self.fixture = ExecuteAroundCommandFixture()

    def test_timer_logs_duration(self):
        action = timer(self.fixture.log_info)
        action(self.fixture.action_stub, lambda: "test description")
        self.assertIn("DURATION", self.fixture.get_message())

    def test_timer_executes_expected_action(self):
        action = timer(self.fixture.log_info)
        action(self.fixture.action_stub, lambda: "test description")
        self.assertEqual(True, self.fixture.has_executed())

    def test_around_logs_before_and_after(self):
        action = around(self.fixture.log_info)
        action(self.fixture.action_stub, lambda: "test description")
        self.assertIn("BEGIN", self.fixture.get_message())
        self.assertIn("END", self.fixture.get_message())


if __name__ == '__main__':
    unittest.main()
