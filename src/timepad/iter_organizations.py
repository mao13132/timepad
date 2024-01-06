# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.logic.sort_posts import sort_posts
from src.timepad.create_event import CreateEvent


class IterOrganizations:
    def __init__(self, settings):
        self.settings = settings

        self.account = settings['account']

    async def _iter_organizations(self):

        event_core = CreateEvent(self.settings)

        for organization in self.account['organization']:

            print(f'Начинаю обработку "{organization}"')

            posts = self.account['posts']

            search_word = self.account['search_word']

            _posts = sort_posts(posts, search_word, self.settings['BotDB'], organization)

            res_create = event_core.start_create(_posts, organization)

            if res_create == 'no_login':
                time.sleep(600)

                return 'no_login'

            print(f'Закончил обработку "{organization}"\n')

        return True

    async def start_iter(self):

        res = await self._iter_organizations()

        return res
