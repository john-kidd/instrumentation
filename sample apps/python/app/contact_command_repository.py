import sqlite3


def rebase():
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contact")
    connection.commit()


def create_contact(contact_id, name, mobile, email, comments):
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO contact (contact_id, name, mobile, email, comments) VALUES (?, ?, ?, ?, ?)",
                   (contact_id, name, mobile, email, comments))

    connection.commit()
