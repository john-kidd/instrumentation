import unittest
from ..app.models import ContactId
from ..app.queries import GetContact
import db_stub
import uuid


class GetContactTestCase(unittest.TestCase):
    """"Tests for 'queries.py'"""

    def test_get_contact_from_db(self):
        contact_id_stub = ContactId(uuid.uuid4())
        get_contact = GetContact(db_stub)
        result = get_contact.query(contact_id_stub)

        self.assertTrue(result.is_valid())
