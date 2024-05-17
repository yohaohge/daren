import time

from util import *
from lxml import etree
from __init__ import *
import re


def get_home_info()->str:

    driver = get_driver()
    switch_to_target("https://affiliate.tiktokglobalshop.com/platform/homepage")
    for _ in range(5):
        try:
            element = driver.find_element(by=By.XPATH,
                                            value="/html/body/div[1]/div/div[1]/div[2]/div/div[4]/div")

            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            html_content = driver.page_source
            all = re.findall('<div class="text-body-m-medium text-neutral-text1">(.*)</div></div></div><div class="text-body-s text-neutral-text4">Shop Code', html_content)
            print(all)
            return all[0]
        except:
            time.sleep(1)

    return ""

def get_template(nation:str)->str:
    driver = get_driver()
    switch_to_target("https://affiliate.tiktokglobalshop.com/connection/target-invitation?shop_region=%s&tab=1"%nation)
    for _ in range(5):
        try:
            element = driver.find_element(by=By.XPATH,
                                          value="/html/body/div[2]/div/div[2]/main/div/div/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div/div/table/tbody/tr/td[1]/div")

            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            all = re.findall("invitation_id=(.*)&enter_from", driver.current_url)
            return all[0]
        except Exception as e:
            print(e)
            time.sleep(2)

    return ""


if __name__ == "__main__":
    print(get_template("PH"))