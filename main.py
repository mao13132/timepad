# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import asyncio
import traceback
import sys

from settings import sessions_path, JOB_LIST, dir_project
from src.logic.clear import _clear
from src.sql.bot_connector import BotDB
from src.telegram.monitoring_telegram import MonitoringTelegram
from src.telegram.start_iter_chat import StartIterTgChat
from src.timepad.start_timepad import TimePad


async def main():
    # await _clear(dir_project)
    #
    # telegram_core = await MonitoringTelegram(sessions_path, BotDB).start_tg()
    #
    # if not telegram_core:
    #     print(f'Нет смог подключиться к аккаунту телеграм')
    #
    #     return False
    #
    # await telegram_core._send_admin('Начинаю работу', dir_project)
    #
    # job_dict = JOB_LIST
    #
    # dict_posts = await StartIterTgChat(telegram_core, BotDB, job_dict).start_iter()
    #
    # if not dict_posts:
    #     try:
    #         telegram_core = await MonitoringTelegram(sessions_path, BotDB).start_tg()
    #     except:
    #         return False
    #
    # count_post = sum([len(x['posts']) for x in dict_posts])
    #
    # if count_post == 0:
    #     print(f'Новых постов для публикации нет. Ожидание новых постов в Telegram')
    #
    #     return False
    #
    # if job_dict == []:
    #     print(f'Нет новых постов на публикацию')
    #
    #     return False

    from _temp import job_dict_ as job_dict

    settings = {
        'job_dict': job_dict,
        'BotDB': BotDB,
        'telegram_core': 'telegram_core'
    }

    res_yandex_job = await TimePad(settings).start_job()

    print(f'Закончил, делаю паузу. В ожидании новых постов в Telegram')

    await _clear(dir_project)


if __name__ == '__main__':

    try:
        res = asyncio.run(main())
    except Exception as es:
        print(f"Ошибка при работе главного потока"
              f"{''.join(traceback.format_exception(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]))}")

