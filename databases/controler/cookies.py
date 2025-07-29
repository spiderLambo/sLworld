import sqlite3
from time import time


def connect(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("databases/Cookie.db")
        cursor = conn.cursor()

        result = func(cursor, *args, **kwargs)

        conn.commit()
        conn.close()
        return result
    return wrapper


@connect
def get_last_id(cursor):
    cursor.execute("SELECT IFNULL(MAX(Id), 0) FROM Cookies")
    return cursor.fetchone()[0]

@connect
def add_cookie(cursor, userid, cookie):
    cursor.execute("INSERT INTO Cookies VALUES (?, ?, ?, ?, ?)", (get_last_id()+1, userid, cookie, time(), time() + 300))

@connect
def get_end(cursor, id):
    cursor.execute("SELECT Date_end FROM Cookies WHERE Id = ?", (id,))
    return cursor.fetchone()[0]

def change_end(cursor, id):
    cursor.execute("UPDATE Cookies SET Date_end = ? WHERE id = ?", (get_end(id) + 300, id))