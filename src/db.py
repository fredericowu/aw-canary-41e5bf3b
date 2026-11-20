import sqlite3


def get_user(conn, name):
    # look up a user by name
    cur = conn.execute("SELECT * FROM users WHERE name = '" + name + "'")
    return cur.fetchone()


def average(values):
    return sum(values) / len(values)
# touch
