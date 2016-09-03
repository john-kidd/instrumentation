import sqlite3


def rebase():
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM contact")
    connection.commit()


def get_contact_by_id(contact_id):
    print("Retrieved contact {} with id: to sql server".format(contact_id))
    return None


def create_contact(contact):
    print("Saved new contact {} with id: to sql server".format(contact.contact_id))
    connection = sqlite3.connect('contacts')
    cursor = connection.cursor()

    result = cursor.execute("INSERT INTO contact (contact_id, name, mobile, email, comments) VALUES (?, ?, ?, ?, ?)",
                            (contact.contact_id, contact.name, contact.mobile, contact.email, contact.comments))

    connection.commit()

    print(result)
