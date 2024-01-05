# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

month_dict = {
    'Январь': 1,
    'Февраль': 2,
    'Март': 3,
    'Апрель': 4,
    'Май': 5,
    'Июнь': 6,
    'Июль': 7,
    'Август': 8,
    'Сентябрь': 9,
    'Октябрь': 10,
    'Ноябрь': 11,
    'Декабрь': 12
}

month_dict_reverse = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
}


def get_month(driver):
    try:
        month_site = driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'nav-month')]").text
    except:
        return False

    try:
        count_month = month_dict[month_site]
    except Exception as es:
        print(f'Не смог определить месяц "{es}" "{month_site}"')

        return False

    return count_month


def open_panel_date(driver):
    try:
        driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'mcalendar') and "
                                               f"contains(@class, 'from')]").click()

    except:
        print(f'Не смог кликнуть на начальную дату')

        return False

    return True


def move_calendar(driver):
    for _try in range(3):

        try:
            panel = driver.find_element(by=By.XPATH,
                                        value=f"//button[contains(@title, 'event_action')]")
        except:
            time.sleep(1)

            continue

        try:
            ActionChains(driver).move_to_element(panel).perform()
        except:
            time.sleep(1)

            continue

        return True

    print(f'Не смог навестись ниже календаря')

    return False


def get_value_from_date(count, date):
    try:
        date_ = date.split('.')[count]

        if date_[0] == '0':
            date_ = date_[1:]

    except Exception as es:
        print(f'Не могу вытащить дату "{date}" по номеру "{count}" "{es}"')

        return False

    date_ = int(date_)

    return date_


def change_mont(driver, count, target):
    for _try in range(count):

        try:
            driver.find_elements(by=By.XPATH,
                                 value=f"//*[contains(@class, 'mdatepicker__drop--show')]"
                                       f"//*[contains(@data-qa, 'description-calendar.navigation')]//a")[target].click()
        except:
            print(f'Не смог переключить месяц')

            return False

    return True


def insert_day(driver, date):
    try:
        driver.find_element(by=By.XPATH,
                            value=f"//*[contains(@class, 'mdatepicker__drop--show')]"
                                  f"//*[contains(@data-date, '{date}')]").click()
    except:
        print(f'Не смог выбрать день')

        return False

    return True


def insert_mont(month, site_month, driver):
    if site_month < month:
        count_click = month - site_month

        res_ = change_mont(driver, count_click, 1)

    else:
        count_click = site_month - month

        res_ = change_mont(driver, count_click, 0)

    return res_


def write_date_(driver, date):
    res_move = move_calendar(driver)

    is_open = open_panel_date(driver)

    if not is_open:
        return False

    day = get_value_from_date(0, date)

    month = get_value_from_date(1, date)

    site_month = get_month(driver)

    if month != site_month:
        insert_mont(month, site_month, driver)

    res_day = insert_day(driver, date)

    return True
