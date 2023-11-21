"""
Creates a connection to the database file.
NOTE: V1 uses a local sqllite database and v2 will use a full production SQL database
"""
import os
import sqlite3
from sqlite3 import Error
from dotenv import load_dotenv

load_dotenv()
DB_FILE = os.getenv("DATABASE_PATH")


def createDBConnection(db_file=DB_FILE):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
