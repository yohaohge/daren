import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 启动程序， 打开登录页面

class WebManager:
    def __init__(self):
        option = webdriver.ChromeOptions()
        option.add_argument("--user-data-dir="+r"/Users/ouge/Library/Application Support/Google/Chrome/Profile 3/")
        driver = webdriver.Chrome(options=option)   # 打开chrome浏览器
        time.sleep(200)

def LoadWeb():
    webManger = WebManager()