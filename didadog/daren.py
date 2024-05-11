# 收集达人数据
import time
from selenium.webdriver.common.action_chains import ActionChains

from __init__ import *

url = "https://didadog.com/talent/square"
driver.get(url)
time.sleep(2000)


# 切换到目标站点
element = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[1]/div[1]/div/div[1]/div/div[2]/label[3]/span[2]")
driver.execute_script("arguments[0].click();", element)
time.sleep(5)

for _ in range(0,10):
    element = driver.find_element(by=By.XPATH,
                                  value="/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/ul/li[9]/a")
    actions = ActionChains(driver)
    actions.scroll_to_element(element).perform()
    time.sleep(1)
    element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/ul/li[9]/a")
    driver.execute_script("arguments[0].click();", element)
    # 滑动到底部
    time.sleep(3)



#/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/ul/li[3]/a
#/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/ul/li[9]/a
#/html/body/div[1]/div/div[1]/div/section/section/main/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/ul/li[9]/a