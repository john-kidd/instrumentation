from db import get_contact_by_id


class Query:
    def __init__(self):
        pass

    def get_description(self):
        return self.__class__.__name__


class GetContact(Query):
    def __init__(self):
        pass

    @staticmethod
    def query(contact_id):
        if contact_id is None:
            raise ValueError("Invalid contact id".format(contact_id))
        return get_contact_by_id(contact_id)
