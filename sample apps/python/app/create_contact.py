import app.shared.console_logger
import app.contact_command_repository
from app.shared.guard import validate_input


def get_description():
    return "create_contact"


def action(create_contact=None, log_info=None):
    logger = log_info or app.shared.console_logger.log_info
    create = create_contact or app.contact_command_repository.create_contact

    def partial(contact):
        validate_input(logger, get_description(), contact)
        create(contact.contact_id, contact.name, contact.mobile, contact.email, contact.comments)
    return partial
