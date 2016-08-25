from ..app.model import Contact


def get_contact_by_id(id):
    return Contact.create("John F Kidd", "+4478866662", "john@test.com", id)


def create_contact(contact):
    print("Saved new contact to db:\n{}".format(contact))