from validate_email import validate_email
import uuid


class ValueObject:
    """ base class for all value objects """

    def __init__(self):
        pass

    def __str__(self):
        """ override to provide the state of the value """

    def is_valid(self):
        return True


class Contact(ValueObject):
    def __init__(self, name, mobile, email, contact_id, comments=None):
        if contact_id is not None:
            self.contact_id = contact_id
        else:
            self.contact_id = ContactId(str(uuid.uuid4()))

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

    @classmethod
    def create(cls, name, mobile, email, contact_id=None, comments=None):
        return cls(name, mobile, email, contact_id, comments)

    def is_valid(self):
        return validate_email(self.email)

    def __str__(self):
            return "\tContact\n\t{}\n\t\tName: {}\n\t\tMobile: {}\n\t\tEmail: {}\n\t\tComments: {}\n\t\tValid: {}"\
                .format(
                    self.contact_id,
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

        self.value = contact_id

    def __str__(self):
        return "\tContactId.value: {}".format(self.value)
