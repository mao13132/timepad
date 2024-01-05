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
from selenium.webdriver.common.action_chains import ActionChains

from src.browser.createbrowser import CreatBrowser
from src.logic.check_load import check_load
from src.timepad.change_cabinet import ChangeCabinet

from src.timepad.click_finish_step import click_finish_step
from src.timepad.click_four_step import click_four_step_
from src.timepad.click_online import click_online
from src.timepad.click_three_step import click_three_step
from src.timepad.click_two_step import click_two_step
from src.timepad.close_banner import close_banner
from src.timepad.go_site import GoSite
from src.timepad.write_address import write_address_
from src.timepad.write_age import write_age_
from src.timepad.write_category import write_category_
from src.timepad.write_city import write_city_
from src.timepad.write_date import write_date_
from src.timepad.write_desc import loop_write_desc
from src.timepad.write_price import write_price_
from src.timepad.write_time import write_times
from src.timepad.write_title import loop_write_title


class CreateEvent:
    def __init__(self, settings):
        self.settings = settings

        self.driver = False

        self.name_profile = settings['name_profile']

    def click_create_event_button(self):
        try:
            panel = self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class, 'corg-menu')]"
                                                                f"//a[contains(@href,'/events/')]")
        except:
            return False

        try:
            ActionChains(self.driver).move_to_element(panel).perform()
        except:
            return False

        try:
            panel.click()
        except:
            return False

        return True

    def click_button_create_event(self):
        try:
            panel = self.driver.find_element(by=By.XPATH, value=f"//*[contains(text(), 'Создать событие')]").click()
        except:
            return False

        return True

    def loop_load_page(self):
        for _try in range(3):
            res_click = self.click_create_event_button()

            if not res_click:
                time.sleep(1)

                continue

            res_load = check_load(self.driver, '//*[contains(text(), "Редактирование названия")]', 15)

            if not res_load:
                no_events = check_load(self.driver, '//*[contains(text(), "У вас пока нет событий") or '
                                                    'contains(text(), "Все события")]')

                if not no_events:
                    continue

                res_button = self.click_button_create_event()

                if not res_button:
                    time.sleep(1)

                    continue

                res_load = check_load(self.driver, '//*[contains(text(), "Редактирование названия")]')

                if not res_load:
                    time.sleep(1)

                    continue

            return True

        print(f'Все попытки зайти в меню создания нового события закончились')

        return False

    def iter_posts(self, posts, organization):

        for post in posts:
            browser_core = CreatBrowser(self.name_profile)

            if not browser_core.driver:
                print(f'Не могу создать браузер пропускаю аккаунт "{self.name_profile}"')

                return False

            self.driver = browser_core.driver

            self.settings['driver'] = self.driver

            in_site = GoSite(self.settings).start_go()

            if not in_site:
                print(f'Не смог зайти на сайт')

                self.driver.quit()

                continue

            res_change = ChangeCabinet(self.settings).start_change(organization)

            if not res_change:
                self.driver.quit()

                continue

            res_load = self.loop_load_page()

            if not res_load:
                self.driver.quit()

                continue

            time.sleep(2)

            close_banner(self.driver)

            title = post['title']

            write_title = loop_write_title(self.driver, title)

            print(f'Результат написания заголовка: "{write_title}"')

            time.sleep(2)

            desc = post['text']

            write_desc = loop_write_desc(self.driver, desc)

            print(f'Результат написания описания: "{write_desc}"')

            time.sleep(2)

            click_offline = click_online(self.driver)

            write_city = write_city_(self.driver, post['city'])

            print(f'Результат написания города: "{write_city}"')

            time.sleep(2)

            write_address = write_address_(self.driver, post['address'])

            print(f'Результат написания адреса: "{write_address}"')

            time.sleep(2)

            write_date = write_date_(self.driver, post['date_event'])

            print(f'Результат выбора даты: "{write_date}"')

            time.sleep(2)

            write_time = write_times(self.driver, post['time_event'], 0)

            print(f'Результат написания времени начала: "{write_time}"')

            write_time = write_times(self.driver, '23:59', 1)

            print(f'Результат написания времени окончания: "{write_time}"')

            time.sleep(2)

            write_category = write_category_(self.driver, post['category'])

            print(f'Результат выбора категории: "{write_category}"')

            time.sleep(2)

            click_next = click_two_step(self.driver)

            time.sleep(5)

            click_next2 = click_three_step(self.driver)

            time.sleep(5)

            if post['price'] != 0:
                res_price = write_price_(self.driver, post['price'])

                print(f'Результат установки стоимости: "{res_price}"')

                time.sleep(2)

            click_next3 = click_four_step_(self.driver)

            time.sleep(5)

            write_age = write_age_(self.driver, post['age'])

            print(f'Результат установки возрастных ограничений: "{write_age}"')

            time.sleep(2)

            finish = click_finish_step(self.driver)

            print(f'Результат опубликование события: "{finish}"')

            self.settings['BotDB'].add_message(post['chat_id'], post['title'], post['date_post'], organization)

            print(f'Перезапускаю браузер')

            self.driver.quit()

            time.sleep(10)

        return True

    def start_create(self, posts, organization):

        res_write = self.iter_posts(posts, organization)

        return res_write
