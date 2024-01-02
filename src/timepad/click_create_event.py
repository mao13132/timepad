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


def click_create_event(driver):
    try:
        driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Создать событие')]").click()
    except:
        print(f'Не смог нажать на кнопку Создать событие')

        return False

    return True


def loop_click_create_event(driver):
    for _try in range(3):
        res_click = click_create_event(driver)

        if not res_click:
            time.sleep(1)

            continue

        res_load = check_load(driver, '//*[contains(@class, "mpaidtariffdesc")]')

        if not res_load:
            time.sleep(1)

            continue

        return True

    print(f'Все попытки перейти в меню "создать событие закончились"')

    return False
