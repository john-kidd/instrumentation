import unittest
from ..app.model import Contact
from ..app.commands import CreateContact
import db_stub


class CreateContactTestCase(unittest.TestCase):
    """"Tests for 'commands.py'"""

    def setUp(self):
        self.create_contact = CreateContact(db_stub)

    def test_save_new_contact_no_comments_to_db(self):
        contact_stub = Contact.create("John F Kidd", 07763535221, "john.kidd@test.com", None)
        self.create_contact.execute(contact_stub)

        self.assertIsNotNone(contact_stub.contact_id)

    def test_save_new_contact_has_comments_to_db(self):
        comments_stub = "a comment"
        contact_stub = Contact.create("John F Kidd", 07763535221, "john.kidd@test.com", None, comments_stub)
        self.create_contact.execute(contact_stub)

        self.assertEquals(comments_stub, contact_stub.comments)

    def test_save_new_contact_with_invalid_contact(self):
        with self.assertRaises(ValueError):
            self.create_contact.execute(None)


