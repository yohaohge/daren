import datetime
import sqlite3


def update_invite(name:str):
    conn = sqlite3.connect("creator.db")
    cur = conn.cursor()

    try:
        cur.execute("update creator set 上次邀请 = ? where 达人 = ?",  (datetime.datetime.now().strftime("%Y%m%d"),name ))
        conn.commit()
    except Exception as e:
        conn.rollback()

    conn.close()