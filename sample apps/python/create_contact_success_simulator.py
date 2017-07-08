import time
from app.db import init_db
from app.db import rebase
from app.create_contact import action, get_description
from app.get_contact import query
from app.models import Contact
from app.shared.file_logger import log_error, log_info
from app.shared.execute_around_command import handle_error


def main():
    init_db()
    rebase()
    contact = Contact.create(
        "John F Kidd",
        "0765242421",
        "john.kidd@test.com",
        comments="A test comment @ {}".format(time.strftime("%H:%M:%S")))

    execute = handle_error(log_error, log_info)
    execute(lambda: create_and_read(contact), get_description)


def create_and_read(contact):
    create_contact = action(log_info=log_info)
    get_contact = query(log_info=log_info)
    create_contact(contact)
    result = get_contact(contact.contact_id)
    log_info("Valid result: {}".format(result is not None))


if __name__ == '__main__':
    main()
