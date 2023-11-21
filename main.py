# This is a test file for testing newly added modules.
from connection.Connection import createDBConnection
from database.CRUD import createTable
from sql.sql import create_users_table

if __name__ == '__main__':
    conn = createDBConnection()
    if conn is not None:
        createTable(conn, create_users_table())
    else:
        print('Failed to create user table! Error: Could not connect to database file.')
