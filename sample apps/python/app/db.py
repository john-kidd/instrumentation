import sqlite3


def get_connection():
    return sqlite3.connect('contacts.db')


def init_db():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS contact ("
                   "    contact_id text(32),"
                   "    name text(255),"
                   "    mobile text(30),"
                   "    email text(100),"
                   "    comments text(500))")




