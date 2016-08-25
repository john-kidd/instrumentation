from app.shared.console_logger import log_error, log_info
from app.shared.execute_around_command import compensate

from app.commands import CreateContact
from app.models import Contact


def main():
    contact = Contact.create("John F Kidd", 0765242421, "john.kidd@test.com", None)
    create_contact = CreateContact()
    execute = compensate(log_error, log_info)
    execute(lambda: create_contact.execute(contact), create_contact.get_description)


if __name__ == '__main__':
    main()
