import time

from app.create_contact import action, get_description
from app.db import init_db
from app.db import rebase
from app.models import Contact
from app.shared.execute_around_command import handle_error
from app.shared.file_logger import log_error, log_info


def main():
    init_db()
    rebase()
    contact = Contact.create(
        "John F Kidd",
        "0765242421",
        "john.kidd.test.com",
        comments="A test comment @ {}".format(time.strftime("%H:%M:%S")))

    execute = handle_error(log_error, log_info)
    try:
        execute(lambda: create_and_read(contact), get_description)
    except ValueError:
        print('Handled error')


def create_and_read(contact):
    raise ValueError(contact)

if __name__ == '__main__':
    main()
