from sqlite3 import Error


def getUser():
    return "TODO: not implemented yet"


def createTable(conn, sql):
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)
