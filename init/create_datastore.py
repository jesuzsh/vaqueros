import os
import sqlite3
from sqlite3 import Error

def create_datastore():
    """
    A single table is to be created. The fields in this table should provide us
    with basic functionality. This can be done by establishing a connection
    with the sqlite database, then  obtaining a cursor from that connection
    so SQL queries could be executed.

    :return: None
    """
    try:
        conn = sqlite3.connect(get_db_path())
        cursor = conn.cursor()

        list_tables(cursor)
        generate_tables(cursor)
    except Error as e:
        print("ERROR:", e)
    finally:
        print("finally occurs")
        if conn:
            conn.close()

def generate_tables(cursor):
    """
    By the end of this function, the local data store should have all of the
    tables required for basic functionality. Additional tables can be added
    here, but I believe that the ideal situation involves an ORM, or an
    isolated abstraction for handling what the schema of the database looks
    like. There will also be a need for alembic to version control the schema
    of the database.

    :return: None
    """
    trans_sql = """CREATE TABLE transaction (transaction_id INTEGER PRIMARY KEY,
        title TEXT,
        amount_usd REAL, 
        card INTEGER,
        category INTEGER);"""

    card_sql = """CREATE TABLE card (
        card_id INT PRIMARY KEY,
        card_name TEXT,
        card_owner INT);
    """

    cat_sql = """CREATE TABLE category (
        category_id INT PRIMARY KEY,
        category_name TEXT,
        is_essential INT);
    """
    
    print("About to attempt to make the first table")
    cursor.execute(trans_sql)
    cursor.execute(card_sql)
    cursor.execute(cat_sql)


def list_tables(cursor):
    """

    """
    sql = """SELECT name
        FROM sqlite_master
        WHERE type='table';"""

    res = cursor.execute(sql)
    print("Listing tables:")
    for row in res:
        print(row)
    

def get_db_path(): 
    """
    Create a full file/directory path string.

    :return: String
    """
    full_path = os.path.dirname(os.path.realpath(__file__))
    db_loc = full_path + "/../data/test.db"

    return db_loc


if __name__ == '__main__':
    create_datastore()
