def query_raises_error():
    raise ValueError("test error")


class ExecuteAroundCommandFixture:
    def __init__(self):
        self._action_executed = False
        self._current_message = ""

    def action_stub(self):
        self._action_executed = True

    def has_executed(self):
        return self._action_executed

    def get_message(self):
        return self._current_message

    def log_info(self, message):
        self._current_message = self._current_message + message

    def log_error(self, message):
        self._current_message = self._current_message + message
