import time

from __init__ import *


def switch_to_target(url:str) -> bool:
    try:
        for tab in driver.window_handles:
            driver.switch_to.window(tab)
            if url in driver.current_url:
                return True

        # 没有找到，打开新的页面

        # 切换新打开的tab页面
        driver.execute_script("window.open();")
        windows = driver.window_handles
        driver.switch_to.window((windows[-1]))
        driver.get(url)
        time.sleep(3)

        return True
    except Exception as e:
        return False