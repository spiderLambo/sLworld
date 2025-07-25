import sqlite3


def connect(func):
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("databases/User.db")
        cursor = conn.cursor()

        result = func(cursor, *args, **kwargs)

        conn.commit()
        conn.close()
        return result
    return wrapper

@connect
def get_last_id(cursor):
    cursor.execute("SELECT IFNULL(MAX(Id), 0) FROM Users")
    return cursor.fetchone()[0]

@connect
def add_user(cursor, username, name, passworld, email):
    cursor.execute("INSERT INTO Users VALUES (?, ?, ?, ?, ?)", (get_last_id()+1, username, name, passworld, email))

@connect
def del_user(cursor, id):
    cursor.execute("UPDATE Users SET Username = NULL, Name = NULL, Passworld = NULL WHERE Id = ?", (id,))

@connect
def change_username(cursor, id, newusername):
    cursor.execute("UPDATE Users SET Username = ? WHERE Id = ?", (newusername, id))

@connect
def change_name(cursor, id, newname):
    cursor.execute("UPDATE Users SET Name = ? WHERE Id = ?", (newname, id))

@connect
def change_passworld(cursor, id, newpass):
    cursor.execute("UPDATE Users SET Passworld = ? WHERE Id = ?", (newpass, id))

@connect
def change_mail(cursor, id, newmail):
    cursor.execute("UPDATE Users SET Email = ? WHERE Id = ?", (newmail, id))

@connect
def connected(cursor, username, passworld):
    cursor.execute("SELECT COUNT(*) FROM Users WHERE Username = ? AND Passworld = ?", (username, passworld))
    return cursor.fetchone()[0] == 1

@connect
def username_used(cursor, username):
    cursor.execute("SELECT COUNT(*) FROM Users WHERE Username = ?", (username,))
    return cursor.fetchone()[0] != 0
