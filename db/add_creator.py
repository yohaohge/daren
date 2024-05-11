import sqlite3


def add_creator(info):
    conn = sqlite3.connect("creator.db")
    cur = conn.cursor()

    try:
        cur.execute("insert into creator values(?,?,?,?,?,?)", info)
        conn.commit()
    except Exception as e:
        conn.rollback()

    conn.close()