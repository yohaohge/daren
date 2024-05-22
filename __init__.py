import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 启动程序， 打开登录页面


driver_manager = {}


def get_driver():
    if "Chrome" in driver_manager:
        return driver_manager["Chrome"]
    else:
        option = webdriver.ChromeOptions()
        option.add_argument("--user-data-dir=" + r"/Users/ouge/Library/Application Support/Google/Chrome/Profile 3/")
        driver = webdriver.Chrome(options=option)
        driver_manager["Chrome"] = driver
        # 进入登录窗口
        driver.get("https://seller.tiktokglobalshop.com/account/login")
        return driver_manager["Chrome"]


def reload_driver():
    if "Chrome" in driver_manager:
        driver_manager["Chrome"].quit()
        driver_manager.clear()
    get_driver()

