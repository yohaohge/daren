import time

# 打开浏览器登录

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from login import *
from invite import *
from send_msg import *
from collect_creator import *
from batch import *
import time
import tkinter as tk
from home import *
import _thread

def select_nation():
    print("选择了国家:", nation_val.get())

window = tk.Tk()
info_val = tk.StringVar()

info_label = tk.Label(window, textvariable=info_val, text="信息提示")
info_label.grid(row=10)
nation_val = tk.StringVar()
list_items = ["PH", "SG", "VN", "TH", "MY"]
label = tk.Label(window,text="选择站点")
label.grid(row=0, column=0)
index = 1
for item in list_items:
    rb = tk.Radiobutton(window, text=item, variable=nation_val, value=item, command=select_nation)
    rb.grid(row=0, column=index)
    if item == "PH":
        rb.select()
    index+=1



category1 = tk.StringVar()
category2 = tk.StringVar()
category3 = tk.StringVar()
category4 = tk.StringVar()
category5 = tk.StringVar()
category6 = tk.StringVar()
category7 = tk.StringVar()


selected_categorys = []
def select_category():
    global  selected_categorys
    selected_categorys = []
    if category1.get() != "":
        selected_categorys.append(category1.get())
    if category2.get() != "":
        selected_categorys.append(category2.get())
    if category3.get() != "":
        selected_categorys.append(category3.get())
    if category4.get() != "":
        selected_categorys.append(category4.get())
    if category5.get() != "":
        selected_categorys.append(category5.get())
    if category6.get() != "":
        selected_categorys.append(category6.get())
    if category7.get() != "":
        selected_categorys.append(category7.get())
    print(selected_categorys)


category_list = ["美妆", "电子", "服饰", "食品", "家居生活", "母婴", "个护和健康"]
category_var_list = [category1,category2,category3,category4,category5,category6,category7]

index = 0
tk.Label(window, text="选择类目").grid(row=1)
for item in category_list:
    cb = tk.Checkbutton(window, text=item, variable=category_var_list[index], onvalue=item,offvalue="", command=select_category)
    cb.grid(row=1,column=index+1)
    index+=1

# shop_info_text = tk.StringVar()
# shop_info = tk.Label(window, text="当前店铺",textvariable=shop_info_text)
# shop_info.grid(row=6, column=0)
# shop_info_text.set("当前店铺:" + "未获取")


def do_login():
    if login():
        info_val.set("登录成功")
        do_get_info()
    else:
        info_val.set("登录失败")


def do_collect():
    if collect_creator(nation_val.get()):
        info_val.set("收集达人成功")
    else:
        info_val.set("收集达人失败")


def do_batch():
    if len(selected_categorys) == 0:
        print("没有选目标类目")
        return
    _thread.start_new_thread(batch, (nation_val.get(),selected_categorys,))

def do_get_info():
    shop_name = get_home_info()
    window.title("邀请达人("+shop_name+")")
    info_val.set("当前店铺:"+ shop_name)


if __name__ == "__main__":
    window.title("达人邀请")

    window.geometry("700x600")
    l = tk.Label(window, font=('Arial', 12), width=10, textvariable=info_val)

    login_btn = tk.Button(window, text='登录tk账号',   command=do_login)
    login_btn.grid(row=2,column=0,columnspan=3)

    collect_daren = tk.Button(window, text='收集达人信息', command=do_collect)
    collect_daren.grid(row=3,column=0,columnspan=3)

    send_msg = tk.Button(window, text='批量给达人发送消息', command=do_batch)
    send_msg.grid(row=4,column=0,columnspan=3)

    home_info = tk.Button(window, text='获取当前账号信息', command=do_get_info)
    home_info.grid(row=5, column=0, columnspan=3)

    window.mainloop()
