from __init__ import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from util import *

def copy_invitation(creator:str)-> bool:
    try:
        from_url = "https://affiliate.tiktokglobalshop.com/connection/target-invitation?shop_region=PH&tab=1"
        switch_to_target(from_url)
        target_url = "https://affiliate.tiktokglobalshop.com/connection/target-invitation/create?invitation_id=7366929733075896070&enter_from=target_invitation_list&enter_method=duplicate&shop_region=PH"
        # 复制第一个
        driver.get(target_url)
        time.sleep(5)
        for i in range(0, 10):
            try:
                element = driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/span/span/input")
                element.send_keys(creator)
                element.send_keys(Keys.RETURN)

                time.sleep(1)                #
                element = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div/div/div/div/span/div/div/div/div/div/div/div[1]/div/div/div")
                driver.execute_script("arguments[0].click();", element)
                break
            except:
                print("搜索失败")
                time.sleep(2)

        element = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[4]/div/div/div[1]/div[1]/div/div[1]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(0.5)

        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div/div/div/span/span/input")
        element.send_keys("我的邀请")
        element.send_keys(Keys.RETURN)


        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[1]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div/div[1]/input")
        # 鼠标点击
        ActionChains(driver).click(on_element=element).perform()
        # 输入内容
        element.send_keys("05/23/2024")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        time.sleep(0.5)

        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[2]/div/form/div/div/div[1]/div[2]/button[2]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[1]/div[1]/div/div[1]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        # 切回来
        driver.get(from_url)
        return True
    except BaseException as err:

        print(err)
        return False

