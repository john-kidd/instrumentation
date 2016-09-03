import sqlite3
from models import Contact


def rebase():
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contact")
    connection.commit()


def get_contact_by_id(contact_id):
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM contact WHERE contact_id = ?", [contact_id])
    row = cursor.fetchone()
    contact = Contact.create(row[1], row[2], row[3], row[0], row[4])
    return contact


def create_contact(contact):
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contact (contact_id, name, mobile, email, comments) VALUES (?, ?, ?, ?, ?)",
                   (contact.contact_id, contact.name, contact.mobile, contact.email, contact.comments))

    connection.commit()
