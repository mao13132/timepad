# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def close_banner(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[@class='cyandexbanner']/button").click()
    except:

        return False

    return True
