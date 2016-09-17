import unittest
from app.models import ContactId


class ContactIdTestCase(unittest.TestCase):
    """Tests for `models.py`."""

    def test_contact_id_with_empty_id_raises_expected_error(self):
        with self.assertRaises(ValueError):
            ContactId(None)


if __name__ == '__main__':
    unittest.main()
