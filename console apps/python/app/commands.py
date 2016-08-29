from shared.console_logger import log_info
from shared.guard import validate_input
import db


def get_description():
    return "create_contact"


def action(create_contact=None):
    def partial(contact):
        validate_input(log_info, contact)
        if create_contact is not None:
            create_contact(contact)
        else:
            db.create_contact(contact)
    return partial
