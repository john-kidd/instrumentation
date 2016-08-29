from ..app.shared.console_logger import log_info
from ..app.shared.guard import validate_input, validate_output

import db


def get_description():
    return "get_contact"


def query(get_contact_by_id=None):
    """returns an query that requires a contact id"""
    def partial(contact_id):
        validate_input(log_info, contact_id)
        if get_contact_by_id is not None:
            contact = get_contact_by_id(contact_id)
        else:
            contact = db.get_contact_by_id(contact_id)
        validate_output(log_info, contact)
        return contact
    return partial
