import time

from __init__ import  *

driver = get_driver()

driver.get("https://seller.tiktokglobalshop.com/order?selected_sort=6&tab=completed&shop_region=PH")

# 获取搜有玩家

time.sleep(3)

for i in range(10):
    try:
        element = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/section/div/main/div[2]/div[2]/main/div/div[2]/div/table/tbody/tr[1]/td/div/div[1]/div[2]/div/span")
        driver.execute_script("arguments[0].click();", element)
        break
    except Exception as e:
        time.sleep(3)
        print(e)

time.sleep(200)