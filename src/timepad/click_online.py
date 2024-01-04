# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def click_online(driver):
    try:
        driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Оффлайн')]").click()
    except:
        print(f'Не смог нажать на кнопку Оффлайн')

        return False

    return True
