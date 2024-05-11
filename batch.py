import time

from __init__ import *
from db.get_creator import *
from invite import *
from send_msg import *

def batch():
    # 数据库读取达人信息
    try:
        creators = get_creator()
        for creator in creators:
            if "服饰" not in creator[1]:
                continue
            print(creator)
            # 发送邀请
            if copy_invitation(creator[0]):
                send_msg(creator[0])

            time.sleep(1)
            # 发送消息
    except Exception as e:
        print(e)

