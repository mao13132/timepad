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

age_site_list = [0, 6, 12, 16, 18]


def open_panel(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//select[contains(@name, 'age_limit')]").click()
    except:
        print(f'Не смог открыть меню выбора возрастных ограничений')

        return False

    return True


def _write_age(driver, age):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//select[contains(@name, 'age_limit')]/option[@value='{age}']").click()
    except:
        print(f'Не смог выбрать возрастные ограничения в "{age}"')

        return False

    return True


def counter_age_item(age):
    for _age in age_site_list:
        if age <= _age:
            return _age

    return 0


def write_age_(driver, age):

    age_item = counter_age_item(age)

    close_popup(driver)

    is_open = open_panel(driver)

    if not is_open:
        return False

    res_write = _write_age(driver, age_item)

    close_popup(driver)

    return res_write
