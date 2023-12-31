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
        'channels': ['https://t.me/SvetoforSevernoe', 'test'],
        'search_word': '',
        'date': '01.09.2023',
    }
]

dir_project = os.getcwd()

sessions_path = os.path.join(dir_project, 'src', 'sessions')

IS_ACTIVE_BROWSER = True

BLACK_LIST = ['СВО', 'политика']

count_message_new_chat = 12  # ограничения на "глубину" сообщений в новом чате

ADMIN = ['@mao13132']

API_ID = 23275230  # API ID от аккаунта-userbot

API_HASH = '4ade579ef577f1458d85a295c1eab66c'  # API hash от аккаунта-userbot
