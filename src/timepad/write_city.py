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


def write_city_(driver, city):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@class, 'city-selector')]"
                                  f"//*[contains(@id, 'react-select-2-input')]") \
            .send_keys(city)
    except:
        print(f'Не смог выбрать город')

        return False

    for _try in range(3):
        try:
            driver.find_element(by=By.XPATH,
                                value=f"//*[contains(@class, 'city-selector')]//*[contains(@class, '-menu')]"
                                      f"//*[contains(@id, 'select')]").click()

            return True

        except:
            time.sleep(1)

            continue

    return False
