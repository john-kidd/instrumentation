from validate_email import validate_email


class ValueObject:
    """ base class for all value objects """

    def __init__(self):
        pass

    def __str__(self):
        """ override to provide the state of the value """

    def is_valid(self):
        return True


class Contact(ValueObject):
    def __init__(self, name, mobile, email, comments=None):
        # fail fast
        if not name:
            raise ValueError("Invalid name")

        if not mobile:
            raise ValueError("Invalid mobile")

        if not email:
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
        # fail fast
        if not contact_id:
            raise ValueError("Invalid contact Id")

        self.contact_id = contact_id

    def __str__(self):
        return "Contact ID: {}".format(self.contact_id)