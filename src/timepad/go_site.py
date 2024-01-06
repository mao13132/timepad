# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.timepad.apply_cookie import apply_cookies
from src.timepad.auth import Auth
from src.timepad.check_auth import check_auth
from src.timepad.check_spam import check_spam_
from src.timepad.click_create_event import loop_click_create_event
from src.timepad.load_page import LoadPage


class GoSite:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def _go_site(self):
        self.settings['url'] = 'https://timepad.ru'

        self.settings['xpath'] = '//*[contains(@class, "mheaderbar")]'

        res_open = LoadPage(self.settings).loop_load_page()

        return res_open

    def start_go(self):

        for _spam_try in range(2):

            in_site = self._go_site()

            if not in_site:
                return False

            time.sleep(5)

            is_auth = check_auth(self.driver)

            time.sleep(5)

            if not is_auth:
                is_auth = Auth(self.settings).start_auth()

            spam = check_spam_(self.driver)

            if spam:
                continue

            res_apply = apply_cookies(self.driver)

            res_create_event = loop_click_create_event(self.driver)

            if res_create_event == 'spam':
                continue

            if res_create_event == 'no_login':
                print(f'Пройдите вторую авторизацию и перезапустите браузер')

                return 'no_login'

            return res_create_event
