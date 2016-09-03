from ..models import Contact


def get_contact_by_id(contact_id):
    return Contact.create("John F Kidd", "+4478866662", "john@test.com", contact_id)


def create_contact(contact_id, name, mobile, email, comments):
    print("Saved new contact to db:\n{}".format(contact_id))

