import sqlite3
from db import *
conn = sqlite3.connect("creator.db")

cur = conn.cursor()
# sql_text_1 = '''CREATE TABLE creator
#            (达人 TEXT PRIMARY KEY,
#             类目 TEXT,
#             粉丝数 NUMBER,
#             视频平均播放数 NUMBER,
#             GPM TEXT,
#             上次邀请 TEXT,
#             国家 TEXT
#             );'''
#
# conn.execute(sql_text_1)
# # 执行sql语句
#
# cur.execute("insert into creator values(?,?,?,?,?,?,?)", ("noigels_shop", "服饰",20800, 13180, "₱544.53 - ₱816.79", '', 'PH'))
# conn.commit()

# conn = sqlite3.connect("creator.db")
# cur = conn.cursor()
#
# ret = list()
# try:
#     cur.execute("select * from creator")
#     ret = cur.fetchall()
# except Exception as e:
#     print(e)
#     conn.rollback()
#
# cur.close()
# conn.close()

# add_creator("myqueen_1818","服饰",4400, 0, "S$3.78 - S$5.67", "SG")
# for data in ret:
#     print(data)
#     add_creator(data[0],data[1], data[2], data[3], data[4], data[6])


update_send_msg("bela_tiktokshop", "PH", "JOJOHappy")