# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from src.timepad.change_cabinet import ChangeCabinet
from src.timepad.create_event import CreateEvent
from src.timepad.go_site import GoSite


class IterOrganizations:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

        self.account = settings['account']

    async def _iter_organizations(self):
        change_core = ChangeCabinet(self.settings)

        event_core = CreateEvent(self.settings)

        for organization in self.account['organization']:

            res_change = change_core.start_change(organization)

            if not res_change:
                continue

            posts = self.account['posts']

            search_word = self.account['search_word']

            res_create = event_core.start_create(posts, search_word)

            print()

    async def start_iter(self):
        in_site = GoSite(self.settings).start_go()

        if not in_site:
            print(f'Не смог зайти на сайт')

            return False

        res = await self._iter_organizations()

        print()
