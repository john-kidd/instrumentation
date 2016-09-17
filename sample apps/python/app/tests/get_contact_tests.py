import unittest
import uuid

import app.tests.db_stub

from app.models import ContactId
from app.get_contact import query


class GetContactTestCase(unittest.TestCase):
    """"Tests for 'get_contact.py'"""

    def test_get_contact_from_db(self):
        contact_id_stub = ContactId(uuid.uuid4())
        get_contact = query(app.tests.db_stub.get_contact_by_id)
        result = get_contact(contact_id_stub)

        self.assertTrue(result.is_valid())
