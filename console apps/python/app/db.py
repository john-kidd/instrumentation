from model import Contact


def get_contact_by_id(id):
    return Contact("John F Kidd", "+4478866662", "john@test.com")


def create_contact(contact):
    print("Saved new contact to db:\n{}".format(contact))