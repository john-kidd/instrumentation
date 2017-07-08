import unittest
from app.models import ContactId


class ContactIdTestCase(unittest.TestCase):
    """Tests for `models.py`."""

    def test_contact_id_with_empty_id_raises_expected_error(self):
        with self.assertRaises(ValueError):
            ContactId(None)

    def test_contact_id_to_string(self):
        target = ContactId("12345")
        expected = "\tContactId.value: {}".format(target.value)
        actual = target.__str__()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
