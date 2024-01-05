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
from selenium.webdriver.common.keys import Keys

from src.timepad.close_popup import close_popup


def open_panel(driver, count):
    try:
        driver.find_elements(by=By.XPATH,
                             value=f"//*[@class='mtimepicker']")[count].click()

    except:
        print(f'Не смог нажать на смену времени')

        return False

    return True


def write_time(driver, time_, count):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"(//*[@class='mtimepicker'])[{count + 1}]/input").send_keys(time_)

    except:
        print(f'Не смог написать время')

        return False

    return True


def get_time(driver, count):
    try:
        time_ = driver.find_element(by=By.XPATH,
                                    value=f"(//*[@class='mtimepicker'])[{count + 1}]/input").get_attribute('value')

    except:
        print(f'Не смог получить время с сайта')

        return ''

    return time_


def _clear_value(driver, count_value, count):
    for _try in range(count_value):

        try:
            driver.find_element(by=By.XPATH,
                                value=f"//*[@class='mtimepicker'][{count + 1}]/input").send_keys(Keys.BACKSPACE)
        except:
            return False

    return True


def clear_value(driver, count):
    time_ = get_time(driver, count)

    count_value = len(time_)

    clear_ = _clear_value(driver, count_value, count)

    return True


def write_times(driver, times, count):
    is_open = open_panel(driver, count)

    if not is_open:
        return False

    clear_ = clear_value(driver, count)

    time.sleep(2)

    res_write = write_time(driver, times, count)

    # close_popup(driver)

    return True
