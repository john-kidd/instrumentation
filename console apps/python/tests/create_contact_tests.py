import unittest
from ..app.model import Contact
from ..app.commands import CreateContact


class CreateContactTestCase(unittest.TestCase):
    """"Tests for 'commands.py'"""

    def test_save_new_contact_no_comments_to_db(self):
        contactStub = Contact.create("John F Kidd", 07763535221, "john.kidd@test.com", None)
        create_contact = CreateContact()
        create_contact.execute(contactStub)

        self.assertIsNotNone(contactStub.contact_id)

    def test_save_new_contact_has_comments_to_db(self):
        comments_stub = "a comment"
        contactStub = Contact.create("John F Kidd", 07763535221, "john.kidd@test.com", None, comments_stub)
        create_contact = CreateContact()
        create_contact.execute(contactStub)

        self.assertEquals(comments_stub, contactStub.comments)
