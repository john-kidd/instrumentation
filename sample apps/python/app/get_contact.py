import app.contact_query_repository
from app.shared.guard import validate_input, validate_output


def get_description():
    return "get_contact"


def query(get_contact_by_id=None, log_info=None):
    """returns an query that requires a contact id"""
    read = get_contact_by_id or app.contact_query_repository.get_contact_by_id
    log = log_info or app.shared.console_logger.log_info

    def partial(contact_id):
        validate_input(log, get_description(), contact_id)
        contact = read(contact_id)
        validate_output(log, get_description(), contact)
        return contact
    return partial
