import sqlite3
from app.db import get_connection


def create_contact(contact_id, name, mobile, email, comments):
    connection = sqlite3.connect('contacts.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contact (contact_id, name, mobile, email, comments) VALUES (?, ?, ?, ?, ?)",
                   (contact_id.value, name, mobile, email, comments))

    connection.commit()
