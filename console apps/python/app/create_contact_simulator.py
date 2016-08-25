from ..app.model import Contact
from ..app.console_logger import log_error, log_info
from ..app.execute_around_command import compensate


def create_contact():
    contact = Contact("John F Kidd", 0765242421, "john.kidd@test.com")
    log_info(contact)


def main():
    execute = compensate(log_error, log_info)
    execute(create_contact, lambda: "Create Contact")


if __name__ == '__main__':
    main()
