from shared.console_logger import log_info
from shared.validators import validate_input

import db


class Command:
    """ Command is a base class that simply provides a get_description function """

    def __init__(self):
        pass

    def get_description(self):
        return self.__class__.__name__


class CreateContact(Command):
    def __init__(self, a_db=None):
        if a_db is not None:
            self.db = a_db
        else:
            self.db = db

    def execute(self, contact):
        validate_input(log_info, contact)
        self.db.create_contact(contact)
