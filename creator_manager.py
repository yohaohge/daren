import tkinter
from tkinter import ttk
from db import *


def show_creators(current_user, nation):
    window = tkinter.Tk()
    window.title(current_user + " "+ nation)

    # 实例化控件，设置表头样式和标题文本
    columns = ("name", "category", "fans", "invite_time", "msg_time")
    headers = ("达人", "类别", "粉丝数", "上次邀请时间", "上次发消息时间")
    widthes = (120, 250, 120, 120, 120)
    tv = ttk.Treeview(window, show="headings", columns=columns)

    for (column, header, width) in zip(columns, headers, widthes):
        tv.column(column, width=width, anchor="w")
        tv.heading(column, text=header, anchor="w")

    def inser_data():
        creators = get_creator(nation).values()

        i = 0
        for value in creators:
            invite_time = get_invite_time(value["name"], nation, current_user)
            msg_time = get_send_msg_time(value["name"], nation, current_user)
            print(value["name"], invite_time, msg_time)
            val = (value["name"], value["category"], value["fans"], invite_time, msg_time)
            tv.insert('', i, values=val)
            i+=1

    tv.pack()

    inser_data()

    window.mainloop()


if __name__ == "__main__":
    show_creators("JOJOHAPPY", "PH")