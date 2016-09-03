from shared.console_logger import log_info

import contact_repository
from shared.guard import validate_input


def get_description():
    return "create_contact"


def action(create_contact=None):
    db_action = create_contact or contact_repository.create_contact

    def partial(contact):
        validate_input(log_info, contact)
        db_action(contact)
    return partial
