from app.shared.console_logger import log_error, log_info
from app.commands import action, get_description
from app.models import Contact
from app.queries import query
from app.shared.execute_around_command import compensate
from app.contact_repository import rebase


def main():
    rebase()
    contact = Contact.create("John F Kidd", 0765242421, "john.kidd@test.com", None)
    execute = compensate(log_error, log_info)
    execute(lambda: create_and_read(contact), get_description)


def create_and_read(contact):
    create_contact = action()
    get_contact = query()
    create_contact(contact)
    result = get_contact(contact.contact_id)
    log_info(result)


if __name__ == '__main__':
    main()