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
def main_menu():
    print("Welcome to the Command Line Menu")
    print("1. 登录")
    print("2. 发送消息")
    print("3. 收集达人")
    print("4. 批量邀请")

    choice = input("Please enter your choice: ")

    if choice == '1':
        print("登录")
        login()
        # 在这里执行 Option 1 的操作
    elif choice == '2':
        print("发送消息")
        send_msg("zengtrillo")
        print("You selected Option 2")
    elif choice == '3':
        collect_creator()
    elif choice == '4':
        batch()
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    # 打开网页
    while True:
        main_menu()



