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
        'name_browser': 'timepad',  # Указывайте под каждый новый номер (аккаунт timepad) новое название учётки
        'channels': ['https://t.me/chekhov_events', ''],
        'search_word': '',
        'date': '1.01.2024',
        'organization': ['Мероприятия Чехов', 'Серпухов'],
    },
    {
        'name': '+79165097308',
        'name_browser': 'timepad',  # Указывайте под каждый новый номер (аккаунт timepad) новое название учётки
        'channels': ['', ''],
        'search_word': '',
        'date': '1.01.2024',
        'organization': ['', ''],
    }
]

IS_ACTIVE_BROWSER = True

BLACK_LIST = ['СВО', 'политика']

STOP_DATE = '1.01.2024'

count_message_new_chat = 12  # ограничения на "глубину" сообщений в новом чате

ADMIN = ['@mao13132']

API_ID = 10127986  # API ID от аккаунта-userbot

API_HASH = 'aa82ee4486b373a2e2e4516c68c3916f'  # API hash от аккаунта-userbot

dir_project = os.getcwd()

sessions_path = os.path.join(dir_project, 'src', 'sessions')

server_ftp = f'chehovlife.beget.tech'

login_ftp = f'chehovlife_bot'

password_ftp = f'Salatik11@'

url_site = 'https://chehov-life.ru/data/'
