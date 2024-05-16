from __init__ import driver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import traceback
from util import *
from db.update_invite import *


def send_msg(creator: str, nation: str, msg: str) -> bool:
    try:
        # 查找达人页面
        switch_to_target("https://affiliate.tiktokglobalshop.com/connection/creator?shop_region=%s" % nation)

        if not check_login():
            return False

        # 搜索达人
        for i in range(0, 10):
            try:
                element = driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[4]/div[1]/div/div/div/div/div/div[1]")
                driver.execute_script("arguments[0].click();", element)
                time.sleep(1)  #

                element = driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div/span/span/input")
                driver.execute_script(
                    '''
                    arguments[0].value = arguments[1];
                    '''
                    , element,
                    '')
                element = driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[3]/div/div/div/div[1]/div/div/div/div/span/span/input")
                element.send_keys(creator)
                element.send_keys(Keys.RETURN)
                time.sleep(2)

                element = driver.find_element(by=By.XPATH,
                                              value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[5]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tr[2]/td[5]/div/span/div/button[3]")
                driver.execute_script("arguments[0].click();", element)
                time.sleep(2)
                break
            except Exception as e:
                print("搜索达人失败", e)
                traceback.print_exc()
                time.sleep(2)
                if i == 9:
                    return False

        # 切换到新页面
        switch_to_target("https://affiliate.tiktokglobalshop.com/seller/im")
        for j in range(0, 10):
            try:
                if creator in driver.page_source:
                    element = driver.find_element(by=By.XPATH,
                                                  value="/html/body/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div/textarea")

                    driver.execute_script(
                        '''
                        arguments[0].value = arguments[1];
                        '''
                        , element,
                        msg)
                    element = driver.find_element(by=By.XPATH,
                                                  value="/html/body/div[2]/div/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div/textarea")
                    element.send_keys(' ')
                    element.send_keys(Keys.RETURN)
                    update_invite(creator)
                    break
                else:
                    print("加载中")
                    time.sleep(0.5)
            except Exception as e:
                print("发送消息失败", e)
                traceback.print_exc()
                time.sleep(2)
                if j == 9:
                    return False

        return True
    except BaseException as err:
        print(err)
        return False
