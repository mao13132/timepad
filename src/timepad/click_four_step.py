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

from src.logic.check_load import check_load


def _click_publish_(driver):
    for _try in range(3):

        try:
            driver.find_element(by=By.XPATH,
                                value=f"//button[contains(@title, 'event_action')]").click()
        except:
            time.sleep(2)

            continue

        return True

    print(f'Не смог нажать на кнопку продолжить на 3й странице')

    return False


def click_four_step_(driver):
    click_button = _click_publish_(driver)

    res_load = check_load(driver, '//*[contains(text(), "Настройки публикации")]')

    return res_load
