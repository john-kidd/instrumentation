import unittest
import uuid

from ..app.models import ContactId
from ..app.queries import query
import db_stub


class GetContactTestCase(unittest.TestCase):
    """"Tests for 'queries.py'"""

    def test_get_contact_from_db(self):
        contact_id_stub = ContactId(uuid.uuid4())
        get_contact = query(db_stub.get_contact_by_id)
        result = get_contact(contact_id_stub)

        self.assertTrue(result.is_valid())
