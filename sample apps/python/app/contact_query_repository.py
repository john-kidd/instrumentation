import sqlite3
from models import Contact


def get_contact_by_id(contact_id):
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contact WHERE contact_id = ?", [contact_id])
    row = cursor.fetchone()
    contact = Contact.create(row[1], row[2], row[3], row[0], row[4])
    return contact
