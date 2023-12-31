# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def check_auth(driver):
    try:
        driver.find_element(by=By.XPATH,
                             value=f"//div[contains(@class, 'mmainmenu')]")
    except:
        return False

    return True
