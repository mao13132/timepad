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

from src.logic.check_load import check_load

from src.logic.sort_posts import sort_posts
from src.timepad.write_desc import loop_write_desc
from src.timepad.write_title import loop_write_title


class CreateEvent:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

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
                no_events = check_load(self.driver, '//*[contains(text(), "У вас пока нет событий")]')

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

    def iter_posts(self, posts):
        for post in posts:
            title = post['title']

            write_title = loop_write_title(self.driver, title)

            print(f'Результат написания заголовка: "{write_title}"')

            desc = post['text']

            write_desc = loop_write_desc(self.driver, desc)

            print(f'Результат написания описания: "{write_desc}"')

            print()

    def start_create(self, posts, search_word):
        res_load = self.loop_load_page()

        if not res_load:
            return False

        _posts = sort_posts(posts, search_word)

        res_write = self.iter_posts(posts)

        print()

        return True
