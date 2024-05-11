import sqlite3

conn = sqlite3.connect("creator.db")

cur = conn.cursor()
sql_text_1 = '''CREATE TABLE creator
           (达人 TEXT PRIMARY KEY,
            类目 TEXT,
            粉丝数 NUMBER,
            视频平均播放数 NUMBER,
            GPM TEXT,
            上次邀请 TEXT
            );'''
conn.commit()
# 执行sql语句
# cur.execute(sql_text_1)
#
# cur.execute("insert into creator values(?,?,?,?,?)", ("noigels_shop", "服饰",20800, 13180, "₱544.53 - ₱816.79"))
# conn.commit()