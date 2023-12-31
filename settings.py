# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import os

JOB_LIST = [
    {
        'name': '+79165097308',
        'name_browser': 'timepad2',
        'channels': ['https://t.me/SvetoforSevernoe', ''],
        'search_word': 'контейнер',
        'date': '01.09.2023',
        'organization': ['org1', 'org2']
    },
    {
        'name': '+79165111',
        'name_browser': 'timepad3',
        'channels': ['https://t.me/SvetoforSevernoe', ''],
        'search_word': '',
        'date': '01.09.2023',
        'organization': ['org1', 'org2']
    }
]

dir_project = os.getcwd()

sessions_path = os.path.join(dir_project, 'src', 'sessions')

IS_ACTIVE_BROWSER = True

BLACK_LIST = ['СВО', 'политика']

STOP_DATE = '1.09.2023'

count_message_new_chat = 12  # ограничения на "глубину" сообщений в новом чате

ADMIN = ['@mao13132']

API_ID = 10127986  # API ID от аккаунта-userbot

API_HASH = 'aa82ee4486b373a2e2e4516c68c3916f'  # API hash от аккаунта-userbot
