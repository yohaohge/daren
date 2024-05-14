import time
import tkinter as tk
import _thread

window = tk.Tk()

window.title("达人邀请")

window.geometry("500x300")

def login():
    print("登录")


def print_info():
    for i in range(100):
        print(i)
        time.sleep(1)

def collect():
    print("收集达人信息")
    _thread.start_new_thread(print_info,())


def msg():
    print("批量给达人发送消息")


login_btn = tk.Button(window, text='登录tk账号', font=("Arial", 12), width=10, height=1,command=login)
login_btn.pack()

collect_daren = tk.Button(window, text='收集达人信息', font=("Arial", 12), width=10, height=1,command=collect)
collect_daren.pack()

send_msg = tk.Button(window, text='批量给达人发送消息', font=("Arial", 12), width=10, height=1,command=msg)
send_msg.pack()

window.mainloop()