import unittest

from app.create_contact import action
from app.models import Contact


class CreateContactTestCase(unittest.TestCase):
    """"Tests for 'create_contact.py'"""

    def test_save_new_contact_no_comments_to_db(self):
        contact_stub = Contact.create("John F Kidd", "07763535221", "john.kidd@test.com", None)
        create_contact = action(self.create_contact_stub)
        create_contact(contact_stub)
        self.assertIsNotNone(contact_stub.contact_id)

    def test_save_new_contact_has_comments_to_db(self):
        comments_stub = "a comment"
        contact_stub = Contact.create("John F Kidd", "07763535221", "john.kidd@test.com", None, comments_stub)
        create_contact = action(self.create_contact_stub)
        create_contact(contact_stub)
        self.assertEqual(comments_stub, contact_stub.comments)

    def test_save_new_contact_with_invalid_contact(self):
        with self.assertRaises(ValueError):
            create_contact = action(self.create_contact_stub)
            create_contact(None)

    @staticmethod
    def create_contact_stub(contact_id, name, mobile, email, comments):
        print("Saved new contact to db:\n{}, {}, {}, {}, {}".format(contact_id, name, mobile, email, comments))
