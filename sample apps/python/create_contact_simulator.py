import time
from app.db import init_db
from app.db import rebase
from app.create_contact import action, get_description
from app.get_contact import query
from app.models import Contact
from app.shared.console_logger import log_error, log_info
from app.shared.execute_around_command import compensate


def main():
    init_db()
    rebase()
    contact = Contact.create(
        "John F Kidd",
        "0765242421",
        "john.kidd@test.com",
        comments="A test comment @ {}".format(time.strftime("%H:%M:%S")))

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
