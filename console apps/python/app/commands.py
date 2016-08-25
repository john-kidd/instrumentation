from ..app.db import create_contact


class Command:
    """ Command is a base class that simply provides a get_description function """

    def __init__(self):
        pass

    def get_description(self):
        return self.__class__.__name__


class CreateContact(Command):
    def __init__(self, db=None):
        self.db = db

    def execute(self, contact):
        create_contact(contact)
