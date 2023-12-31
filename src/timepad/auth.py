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


class Auth:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.account = settings['account']

    def click_sign_in(self):

        try:
            self.driver.find_element(by=By.XPATH,
                                     value=f"//*[contains(text(), 'Войти')]").click()
        except:
            return False

        return True

    def check_popup(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f'//*[contains(text(), "Вход и регистрация")]')
        except:
            return False

        return True

    def loop_open_window(self):
        for _try in range(3):

            is_open = self.check_popup()

            if is_open:
                return True

            self.click_sign_in()

            is_open = self.check_popup()

            if not is_open:
                time.sleep(1)

                continue

            return True

        print(f'Закончились попытки открыть окно авторизации')

        return False

    def formate_number(self):
        if '+7' in self.account['name']:
            self.account['name'] = self.account['name'].replace('+7', '')

        return True

    def write_login(self):

        try:
            self.driver.find_element(by=By.XPATH, value=f"//input[contains(@name, 'phone')]") \
                .send_keys(self.account['name'])
        except:
            print(f'Не смог написать логин')

            return False

        return True

    def click_login(self):

        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Получить код')]").click()
        except:
            print(f'Не смог нажать на кнопку получить код')

            return False

        return True

    def start_auth(self):
        res_click = self.loop_open_window()

        if not res_click:
            return False

        self.formate_number()

        res_phone = self.write_login()

        if not  res_phone:
            return False

        res_click = self.click_login()

        if not res_click:
            return False

        print(f'Выслал смс на номер. Введите код и после перезапустите программу')

        time.sleep(600)

        return True
