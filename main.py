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
from auto_collect import *
from tkinter import messagebox
from creator_manager import *

def select_nation():
    print("选择了国家:", nation_val.get())


window = tk.Tk()
info_val = tk.StringVar()

nation_val = tk.StringVar()
list_items = ["PH", "SG", "VN", "TH", "MY"]
label = tk.Label(window, text="选择站点")
label.grid(row=0, column=0)
index = 1
for item in list_items:
    rb = tk.Radiobutton(window, text=item, variable=nation_val, value=item, command=select_nation)
    rb.grid(row=0, column=index)
    if item == "PH":
        rb.select()
    index += 1

category1 = tk.StringVar()
category2 = tk.StringVar()
category3 = tk.StringVar()
category4 = tk.StringVar()
category5 = tk.StringVar()
category6 = tk.StringVar()
category7 = tk.StringVar()

selected_categorys = []


def select_category():
    global selected_categorys
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
category_var_list = [category1, category2, category3, category4, category5, category6, category7]

index = 0
tk.Label(window, text="选择类目").grid(row=1, sticky='w')
for item in category_list:
    cb = tk.Checkbutton(window, text=item, variable=category_var_list[index], onvalue=item, offvalue="",
                        command=select_category)
    cb.grid(row=1, column=index + 1)
    index += 1

# shop_info_text = tk.StringVar()
# shop_info = tk.Label(window, text="当前店铺",textvariable=shop_info_text)
# shop_info.grid(row=6, column=0)
# shop_info_text.set("当前店铺:" + "未获取")


input = tk.Text(window)
input.grid(row=11, rowspan=5, column=0, columnspan=7, sticky='w')

sample_text = tk.StringVar()
min_fans = tk.StringVar()
min_fans.set("1000")
min_fans_for_msg = tk.StringVar()
min_fans_for_msg.set("1000")

current_user = ""

prefix_len = tk.StringVar()
prefix_len.set("3")
max_cnt = tk.StringVar()
max_cnt.set("10")

def do_login():
    if login():
        print("登录成功")
        do_get_info()
    else:
        messagebox.showinfo("错误", "登录失败")


def do_collect():
    if collect_creator(nation_val.get()):
        print("错误", "收集达人成功")
    else:
        print("错误", "收集达人失败")


def do_batch_msg():
    if get_home_info() != current_user:
        messagebox.showinfo("错误", "请重新初始化")
        return

    if len(selected_categorys) == 0:
        messagebox.showinfo("错误", "没有选目标类目!!!")
        return
    if len(current_user) == 0:
        messagebox.showinfo("错误", "没有同步当前登录的用户!!!")
        return

    if not min_fans_for_msg.get().isdigit() or len(min_fans_for_msg.get()) == 0:
        messagebox.showinfo("错误","最少粉丝数应该输入整数")
    min_fan_num = int(min_fans_for_msg.get())
    _thread.start_new_thread(batch_msg, (nation_val.get(), selected_categorys, input.get(1.0, tk.END), current_user,min_fan_num))


def do_auto():
    if not prefix_len.get().isdigit() or len(prefix_len.get()) == 0:
        prefix_len_num = 3
    else:
        prefix_len_num = int(prefix_len.get())
    if not max_cnt.get().isdigit() or len(max_cnt.get()):
        max_cnt_num = 10
    else:
        max_cnt_num = int(prefix_len.get())
    _thread.start_new_thread(auto, (nation_val.get(),prefix_len_num, max_cnt_num))


def do_reset():
    reload_driver()

def do_show_creators():
    show_creators(current_user, nation_val.get())


def do_batch_invite():
    if len(selected_categorys) == 0:
        messagebox.showinfo("错误", "没有选目标类目!!!")
        return
    if not sample_text.get().isdigit():
        messagebox.showinfo("错误", "样本id需要是数值")
        return

    if not min_fans.get().isdigit() or len(min_fans.get()) == 0:
        messagebox.showinfo("错误","最少粉丝数应该输入整数")
    min_fan_num = int(min_fans.get())
    _thread.start_new_thread(batch_invite, (nation_val.get(), selected_categorys, sample_text.get(), current_user,min_fan_num))


def do_get_info():
    global current_user
    current_user = ""
    shop_name = get_home_info()
    window.title("邀请达人(" + shop_name + ")")
    current_user = shop_name


def do_init():
    do_login()
    if current_user == "":
        return

    sample_text.set(get_template(nation_val.get()))
    messagebox.showinfo("成功", "初始化成功")



if __name__ == "__main__":
    window.title("达人邀请")

    window.geometry("900x600")
    l = tk.Label(window, font=('Arial', 12), width=10, textvariable=info_val)

    login_btn = tk.Button(window, text='初始化（中途切换账号需要重新初始化）', command=do_init)
    login_btn.grid(row=2, column=0, columnspan=3, sticky='w')

    collect_daren = tk.Button(window, text='收集达人信息', command=do_collect)
    collect_daren.grid(row=3, column=0, columnspan=3, sticky='w')

    send_msg = tk.Button(window, text='批量给达人发送消息', command=do_batch_msg)
    send_msg.grid(row=4, column=0, columnspan=3, sticky='w')
    label = tk.Label(window, text="最少粉丝条件")
    label.grid(row=4, column=3, columnspan=1, sticky='w')
    min_fans_input = tk.Entry(window, textvariable=min_fans_for_msg)
    min_fans_input.grid(row=4, column=4, columnspan=2, sticky='w')


    # 筛选条件
    home_info = tk.Button(window, text='批量邀请达人', command=do_batch_invite)
    home_info.grid(row=5, column=0, columnspan=2, sticky='w')
    label = tk.Label(window, text="先输入模版id")
    label.grid(row=5, column=2, columnspan=1, sticky='w')
    input2 = tk.Entry(window, textvariable=sample_text)
    input2.grid(row=5,  column=3, columnspan=2, sticky='w')
    label = tk.Label(window, text="最少粉丝条件")
    label.grid(row=5, column=5, columnspan=1, sticky='w')
    min_fans_input = tk.Entry(window, textvariable=min_fans)
    min_fans_input.grid(row=5, column=6, columnspan=2, sticky='w')

    stop_msg = tk.Button(window, text='停止发消息', command=end_batch)
    stop_msg.grid(row=7, column=0, columnspan=3, sticky='w')

    auto_btn = tk.Button(window, text='自动收集达人', command=do_auto)
    auto_btn.grid(row=8, column=0, columnspan=2, sticky='w')

    label_prefix = tk.Label(window, text="搜索长度")
    label_prefix.grid(row=8, column=2, columnspan=2, sticky='w')

    prefix_input = tk.Entry(window, textvariable=prefix_len)
    prefix_input.grid(row=8, column=4, columnspan=1, sticky='w')

    label_max_cnt = tk.Label(window, text="最大次数")
    label_max_cnt.grid(row=8, column=5, columnspan=1, sticky='w')

    input_max_cnt = tk.Entry(window, textvariable=max_cnt)
    input_max_cnt.grid(row=8, column=6, columnspan=1, sticky='w')

    reset_btn = tk.Button(window, text='重置浏览器', command=do_reset)
    reset_btn.grid(row=9, column=0, columnspan=3, sticky='w')

    creator_manager_btn = tk.Button(window, text='达人管理', command=do_show_creators)
    creator_manager_btn.grid(row=10, column=0, columnspan=3, sticky='w')

    window.mainloop()
