# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def write_address_(driver, address):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@name, 'event_place')]") \
            .send_keys(address[1:])

    except:
        print(f'Не смог выбрать адрес')

        return False

    return True
