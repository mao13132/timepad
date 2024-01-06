# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------

from selenium.webdriver.common.by import By


def apply_cookies(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@class, 'ccookie')]"
                                  f"//button[contains(text(), 'Хорошо')]").click()

    except:
        return False

    return True
