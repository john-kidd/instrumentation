import sqlite3
from app.models import Contact, ContactId
from app.db import get_connection

def get_contact_by_id(contact_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contact WHERE contact_id = ?", [contact_id.value])
    row = cursor.fetchone()
    contact = Contact.create(row[1], row[2], row[3], ContactId([0]), row[4])
    return contact
