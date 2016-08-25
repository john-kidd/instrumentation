import db
from validators import validate_input, validate_output
from console_logger import log_info


class Query:
    """ Query is a base class that simply provides a get_description function """

    def __init__(self):
        pass

    def get_description(self):
        return self.__class__.__name__


class GetContact(Query):
    """ GetContact is a query that validates we have a contact_id and class a db to retrieve a matching contact """

    def __init__(self, a_db=None):
        if a_db is not None:
            self.db = a_db
        else:
            self.db = db

    def query(self, contact_id):
        validate_input(log_info, contact_id)
        result = self.db.get_contact_by_id(contact_id)
        validate_output(log_info, result)
        return result
