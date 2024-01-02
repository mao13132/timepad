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


def write_title(driver, title):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[@name='event_name']").send_keys(title)
    except:
        return False

    return True


def get_title(driver):
    try:
        title_text = driver.find_element(by=By.XPATH,
                                         value=f"//*[@name='event_name']").get_attribute('value')
    except:
        return False

    return title_text


def loop_write_title(driver, title):
    for _try in range(3):
        site_title = get_title(driver)

        if not site_title or 'Новое событие' == site_title:
            write_title(driver, title)

            time.sleep(1)

            continue

        return True

    print(f'Попытки написать титле мероприятия закончились')

    return False
