# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By

from src.timepad.close_popup import close_popup


def open_panel(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@name, 'event_category_ids')]").click()
    except:
        print(f'Не смог открыть панель для выбора категории')

        return False

    return True


def click_category(driver, category):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//option[contains(text(), '{category}')]").click()
    except:
        print(f'Не смог кликнуть на необходимую категорию')

        return False

    return True


def write_category_(driver, category):
    close_popup(driver)

    is_open = open_panel(driver)

    if not is_open:
        return False

    res_click = click_category(driver, category)

    close_popup(driver)

    return res_click
