# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from selenium.webdriver.common.by import By


def change_frame(driver):
    try:
        _frame = driver.find_element(by=By.XPATH,
                                     value=f"//iframe")
    except:
        return False

    try:
        driver.switch_to.frame(_frame)
    except:
        return False

    return True


def _check_spam(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//input[@type='checkbox']").click()
    except:

        return False

    return True


def check_block(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(text(), 'Одну секундочку')]")
    except:
        return False

    return True


def check_spam_(driver):
    is_block = check_block(driver)

    if not is_block:
        return False

    for _try in range(8):
        change_ = change_frame(driver)

        is_spam = _check_spam(driver)

        driver.switch_to.default_content()

        time.sleep(30)

        is_block = check_block(driver)

        if not is_block:
            return True

    print(f'Не смог пройти антиспам систему')

    return True
