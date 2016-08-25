import db


class Command:
    """ Command is a base class that simply provides a get_description function """

    def __init__(self):
        pass

    def get_description(self):
        return self.__class__.__name__


class CreateContact(Command):
    def __init__(self, a_db=None):
        self.db = a_db or db

    def execute(self, contact):
        self.db.create_contact(contact)
