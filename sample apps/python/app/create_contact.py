import shared.console_logger
import contact_command_repository
from shared.guard import validate_input


def get_description():
    return "create_contact"


def action(create_contact=None, log_info=None):
    log = log_info or shared.console_logger.log_info
    create = create_contact or contact_command_repository.create_contact

    def partial(contact):
        validate_input(log, contact)
        create(contact)
    return partial
