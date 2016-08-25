from app.model import Contact
from app.console_logger import log_error, log_info
from app.execute_around_command import compensate
from app.commands import CreateContact


def main():
    contact = Contact.create("John F Kidd", 0765242421, "john.kidd@test.com", None)
    create_contact = CreateContact()
    execute = compensate(log_error, log_info)
    execute(lambda: create_contact.execute(contact), create_contact.get_description)


if __name__ == '__main__':
    main()
