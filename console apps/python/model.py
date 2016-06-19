from validate_email import validate_email

class ValueObject:
    """ base class for all value objects """

    def is_valid(self):
        return True


class Contact(ValueObject):

    def __init__(self, name, mobile, email, comments = None):
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
