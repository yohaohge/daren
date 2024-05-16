import time
from selenium.webdriver.common.action_chains import ActionChains
from lxml import etree

from __init__ import *

url = "https://didadog.com/video/search"
driver.get(url)
time.sleep(2)
html_content = driver.page_source
root = etree.HTML(html_content)
country = root.xpath("/html/body/div[1]/div/div[1]/div/section/section/main/div/div[1]/div[2]/div[2]/div[1]/span")[0]

title = root.xpath("/html/body/div[1]/div/div[1]/div/section/section/main/div/div[1]/div[2]/div[2]/div[2]/span")[0]
print(title.text)

price = root.xpath("/html/body/div[1]/div/div[1]/div/section/section/main/div/div[1]/div[2]/div[2]/div[3]/span[2]")[0]
print(price.text)

element = driver.find_element(by=By.XPATH,value="/html/body/div[1]/div/div[1]/div/section/section/main/div/div[1]/div[2]/div[2]/div[6]/span[3]")
driver.execute_script("arguments[0].click();", element)
time.sleep(1)
tabs = driver.window_handles
driver.switch_to.window(tabs[-1])
current_url = driver.current_url
while "tiktok" not in current_url:
    time.sleep(2)
    current_url = driver.current_url
    print(current_url)

print(driver.current_url)

time.sleep(2000)
