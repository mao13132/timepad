# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
# from src.browser.createbrowser import CreatBrowser
from src.browser.createbrowser_uc import CreatBrowser
from src.timepad.iter_organizations import IterOrganizations


class TimePad:
    def __init__(self, settings):
        self.settings = settings

        self.job_dict = settings['job_dict']

    async def iter_account(self):
        for account in self.job_dict:
            name_ = account['name']

            name_profile = account['name_browser']

            if not account['posts']:
                print(f'Нет постов для "{name_}"')

                continue

            print(f'Начинаю работу с "{name_}" "{name_profile}"')

            self.settings['account'] = account

            self.settings['name_profile'] = name_profile

            res = await IterOrganizations(self.settings).start_iter()

            print()

        print()

    async def start_job(self):
        res_iter = await self.iter_account()

        print()
