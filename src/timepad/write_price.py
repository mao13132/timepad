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

from src.timepad.close_popup import close_popup


def open_panel(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@id, 'rice_container')]").click()
    except:
        print(f'Не смог открыть меню выбора стоимости')

        return False

    return True


def _write_price(driver, price):
    try:
        driver.find_element(by=By.XPATH,
                                 value=f"//input[contains(@id, 'price')]").send_keys(price)
    except:
        print(f'Не смог установить стоимость')

        return False

    return True


def write_price_(driver, price):
    is_open = open_panel(driver)

    if not is_open:
        return False

    res_write = _write_price(driver, price)

    # close_popup(driver)

    return res_write
