from validate_email import validate_email


class ValueObject:
    """ base class for all value objects """

    def __str__(self):
        """ override to provide the state of the value """

    def is_valid(self):
        return True


class Contact(ValueObject):
    def __init__(self, name, mobile, email, comments=None):
        if (name == None):
            raise ValueError("Invalid name")

        if (mobile == None):
            raise ValueError("Invalid mobile")

        if (email == None):
            raise ValueError("Invalid email")

        self.name = name
        self.mobile = mobile
        self.email = email
        self.comments = comments

    def is_valid(self):
        return validate_email(self.email)

    def __str__(self):
        return "\n\tName: {0}\n\tMobile: {1}\n\tEmail: {2}\n\tComments: {3}\n\tValid: {4}".format(
            self.name,
            self.mobile,
            self.email,
            self.comments,
            self.is_valid())


class ContactId(ValueObject):

    def __init__(self, contact_id):
        if contact_id is None:
            raise ValueError("Invalid contact Id")

        self.contact_id = contact_id

    def __str__(self):
        return "Contact ID: {}".format(self.contact_id)