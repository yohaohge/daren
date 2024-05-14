
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# 启动程序， 打开登录页面
option = webdriver.ChromeOptions()
option.add_argument("--user-data-dir="+r"/Users/ouge/Library/Application Support/Google/Chrome/Profile 3/")
driver = webdriver.Chrome(options=option)