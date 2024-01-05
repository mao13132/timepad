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


def open_panel(driver):
    try:
        driver.find_element(by=By.XPATH, value=f'//button[contains(text(), "Загрузить")]').click()
    except:
        return False

    return True


def status_loading(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f'//button[contains(text(), "Загружается...")]')
    except:
        return False

    return True


def loop_status_loading(driver):
    for _try in range(60):
        loading = status_loading(driver)

        if loading:
            time.sleep(1)

            continue

        return True

    print(f'Не могу дождаться загрузки изображения')

    return False


def popup_is_open(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f'//div[contains(@class, "uploadcare") and contains(@class, "container")]')
    except:
        return False

    return True


def loop_popup_is_open(driver):
    for _try in range(5):
        res_ = popup_is_open(driver)

        if not res_:
            time.sleep(1)

            continue

        return True

    print(f'Не открылась окно с заливкой фото')

    return False


def click_link(driver):
    try:
        driver.find_element(by=By.XPATH, value=f'//*[contains(@class, "item") and contains(@title, "Ссылка")]').click()
    except:
        print(f'Не могу кликнуть на "Ссылка" в окне с заливкой изображения')

        return False

    return True


def write_link(driver, link):
    try:
        driver.find_element(by=By.XPATH, value=f'//*[contains(@class, "tab") and '
                                               f'contains(@class, "content")]//input').send_keys(link)
    except:
        print(f'Не могу вставить ссылку на изображение в окне с выбором изображения')

        return False

    return True


def get_status_panel_popup(driver):
    try:
        status = driver.find_element(by=By.XPATH, value=f'//div[contains(@class, "uploadcare") and '
                                                        f'contains(@class, "panel__menu")]').get_attribute(
            'data-current')
    except:
        print(f'Не могу проверить открылась ли меню "Ссылка" в окне с заливкой изображения')

        return False

    return status


def upload_click(driver):
    try:
        driver.find_element(by=By.XPATH,
                            value=f'//*[contains(@class, "tab") and contains(@class, "content")]'
                                  f'//button[contains(text(), "агрузить")]').click()
    except:
        print(f'Не могу нажать на кнопку загрузить в окне с изображением')

        return False

    return True


def insert_image_(driver, link):
    for _try in range(3):
        res_click = open_panel(driver)

        if not res_click:
            time.sleep(1)

            continue

        is_open = loop_popup_is_open(driver)

        if not is_open:
            time.sleep(1)

            continue

        click_link(driver)

        time.sleep(1)

        status = get_status_panel_popup(driver)

        if status != 'url':
            time.sleep(1)

            continue

        res_write = write_link(driver, link)

        if not res_write:
            time.sleep(1)

            continue

        res_click = upload_click(driver)

        if not res_click:
            time.sleep(1)

            continue

        time.sleep(2)

        is_open = popup_is_open(driver)

        if is_open:
            time.sleep(1)

            continue

        is_upload = loop_status_loading(driver)

        if not is_upload:
            time.sleep(1)

            continue

        return True

    print(f'Все попытки указать изображение закончились')

    return False
