# 收集达人

from __init__ import driver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from lxml import etree
from db.add_creator import add_creator
from selenium.webdriver.common.action_chains import ActionChains
from util import *


def parse_page(root, nation):
    i = 1
    while True:
        path = "/html/body/div[2]/div/div[2]/main/div/div/div/div/div[5]/div/div/div/div/div[2]/div/div/div/div/div/div[2]/table/tr[%d]" % (
                i * 2)
        creator = root.xpath(path)
        if not creator:
            break
        try:
            creator_name = creator[0].xpath("td[1]/div/span/div/div[2]/div[1]/div/span")[0].text
            category = ""
            for element in creator[0].xpath("td[1]/div/span/div/div[2]/div[2]/div/span"):
                if len(category) > 0:
                    category += "|"
                try:
                    category += element.xpath("div/span/div/div/div")[0].text
                except Exception as e:
                    category = "todo"
            fans = creator[0].xpath("td[2]/div/span/div")[0].text
            if "K" in fans:
                fans = fans.replace("K", "")
                fans = float(fans) * 1000
                fans = int(fans)
            elif "M" in fans:
                fans = fans.replace("M", "")
                fans = float(fans) * 1000000
                fans = int(fans)

            views = creator[0].xpath("td[3]/div/span/div")[0].text
            if "K" in views:
                views = views.replace("K", "")
                views = float(views) * 1000
                views = int(views)
            elif "M" in views:
                views = views.replace("M", "")
                views = float(views) * 1000000
                views = int(views)

            gmp = creator[0].xpath("td[4]/div/span/div/span/div[1]/div/span")[0].text + " " + \
                  creator[0].xpath("td[4]/div/span/div/span/div[2]/div/span")[0].text
            print(creator_name, category, fans, views, gmp)
            # 插入到数据库
            try:
                add_creator((creator_name, category, fans, views, gmp, '', nation))
            except Exception as e:
                print("插入失败", e)
        except Exception as e:
            print(e)

        i = i + 1


def collect_creator(nation:str):
    try:

        switch_to_target("https://affiliate.tiktokglobalshop.com/connection/creator?shop_region=%s"%nation)
        if not check_login():
            return False

        time.sleep(1)  #
        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[4]/div[1]/div/div/div/div/div/div[2]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

        # 下拉10次加载更多数据
        # for i in range(1, 10):
        #     element = driver.find_element(by=By.XPATH,
        #                                   value="/html/body/div[2]/div/div[2]/main/div/div")
        #     ActionChains(driver).move_to_element(to_element=element).scroll_by_amount(0, 500 * i).perform()
        #     time.sleep(1)

        html_content = driver.page_source
        root = etree.HTML(html_content)
        parse_page(root,nation)
    except Exception as e:
        print("收集失败", e)
    return

def auto_collect(nation:str, key:str):
    try:

        switch_to_target("https://affiliate.tiktokglobalshop.com/connection/creator?shop_region=%s"%nation)
        if not check_login():
            return False

        time.sleep(1)  #
        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[4]/div[1]/div/div/div/div/div/div[2]")
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
        element.send_keys(key)
        element.send_keys(Keys.RETURN)

        element = driver.find_element(by=By.XPATH,
                                      value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[4]/div[1]/div/div/div/div/div/div[2]")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(3)

        # 下拉10次加载更多数据
        # for i in range(1, 10):
        #     element = driver.find_element(by=By.XPATH,
        #                                   value="/html/body/div[2]/div/div[2]/main/div/div")
        #     ActionChains(driver).move_to_element(to_element=element).scroll_by_amount(0, 500 * i).perform()
        #     time.sleep(1)

        html_content = driver.page_source
        root = etree.HTML(html_content)
        parse_page(root,nation)
    except Exception as e:
        print("收集失败", e)
    return
