# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import os
import traceback
import sys

from settings import sessions_path
from src.browser.createbrowser import CreatBrowser
from src.logic.clear import _clear
from src.sql.bot_connector import BotDB


def main():
    patch_project = os.path.dirname(__file__)

    await _clear(patch_project)

    telegram_core = await MonitoringTelegram(sessions_path, BotDB).start_tg()

    if not telegram_core:
        print(f'Нет смог подключиться к аккаунту телеграм')

        return False

    await telegram_core._send_admin('Начинаю работу', patch_project)



    # browser = CreatBrowser()
    #
    # if not browser.driver:
    #     return False
    #
    # settings = {
    #     'driver': browser.driver
    # }
    #
    # print()


if __name__ == '__main__':

    try:
        main()
    except Exception as es:
        print(f"Ошибка при работе главного потока"
              f"{''.join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))}")

    finally:

        browser.driver.quit()
