# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.timepad.auth import Auth
from src.timepad.check_auth import check_auth
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

        in_site = self._go_site()

        if not in_site:
            return False

        time.sleep(2)

        is_auth = check_auth(self.driver)

        if not is_auth:
            is_auth = Auth(self.settings).start_auth()

        return is_auth
