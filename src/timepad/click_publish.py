# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By

from src.logic.check_load import check_load


def _click_publish_(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//button[contains(@title, 'event_action')]").click()
    except:
        print(f'Не смог нажать на кнопку продолжить на 1й странице')

        return False

    return True


def click_publish_(driver):
    click_button = _click_publish_(driver)

    res_load = check_load(driver, '//*[contains(text(), "Регистрация на событие")]')

    return res_load
