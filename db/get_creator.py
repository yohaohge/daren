import sqlite3


def get_creator() -> list:
    conn = sqlite3.connect("creator.db")
    cur = conn.cursor()

    ret = list()
    try:
        cur.execute("select * from creator")
        ret = cur.fetchall()
    except Exception as e:
        print(e)
        conn.rollback()

    cur.close()
    conn.close()

    return ret



# ret = get_creator()
# for data in ret:
#     print(data)