# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def close_popup(driver):
    try:
        driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'body')]").click()
    except:
        return False

    return True
