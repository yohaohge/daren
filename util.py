import time

from __init__ import *


def check_login() -> bool:
    driver = get_driver()
    if "login" in driver.current_url:
        return False
    return True


def switch_to_target(url: str) -> bool:
    driver = get_driver()
    try:

        if url in driver.current_url:
            return True

        for tab in driver.window_handles:
            driver.switch_to.window(tab)
            if url in driver.current_url:
                return True
        # 切换新打开的tab页面
        driver.execute_script("window.open();")
        windows = driver.window_handles
        driver.switch_to.window((windows[-1]))
        driver.get(url)
        time.sleep(3)

        return True
    except Exception as e:
        reload_driver()
        get_driver().get(url)
        time.sleep(3)
        return False
