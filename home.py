
from util import *
from lxml import etree

def get_home_info()->str:
    switch_to_target("https://seller.tiktokglobalshop.com/profile/seller-profile?tab=seller_information")
    time.sleep(5)
    html_content = driver.page_source
    root = etree.HTML(html_content)
    element = root.xpath("/html/body/div[1]/section/section/div/main/section/div/div/div[2]/div/div[1]/div/section[1]/div/div/div[1]/div/div[2]/span")
    print(element[0].text)
    return element[0].text

#get_home_info()