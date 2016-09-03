import db
from shared.console_logger import log_info
from shared.guard import validate_input, validate_output


def get_description():
    return "get_contact"


def query(get_contact_by_id=None):
    """returns an query that requires a contact id"""
    db_query = get_contact_by_id or db.get_contact_by_id

    def partial(contact_id):
        validate_input(log_info, contact_id)
        contact = db_query(contact_id)
        validate_output(log_info, contact)
        return contact
    return partial
