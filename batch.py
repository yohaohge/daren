import time

from __init__ import *
from db.get_creator import *
from invite import *
from send_msg import *

is_doing = False

def batch(nation:str, categorys):
    global is_doing
    if not is_doing:
        is_doing = True
    else:
        return

    # 数据库读取达人信息
    try:
        creators = get_creator()
        for creator in creators:
            if creator[6] != nation:
                continue

            is_target = False
            for category in categorys:
                if category in creator[1]:
                    is_target = True
                    break
            if not is_target:
                print(creator[0], "非目标达人")
                continue

            print("给达人发消息:", creator[0], nation)
            # 发送邀请
            # if copy_invitation(creator[0]):
            # 没有发送过消息
            if creator[5] == '':
                send_msg(creator[0], nation)
                update_invite(creator[0])
            time.sleep(1)
            # 发送消息
    except Exception as e:
        print(e)
    is_doing = False