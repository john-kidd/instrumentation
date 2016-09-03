from app.shared.console_logger import log_error, log_info

from app.commands import action, get_description
from app.models import Contact
from app.shared.execute_around_command import compensate


def main():
    contact = Contact.create("John F Kidd", 0765242421, "john.kidd@test.com", None)
    create_contact = action()
    execute = compensate(log_error, log_info)
    execute(lambda: create_contact(contact), get_description)


if __name__ == '__main__':
    main()
