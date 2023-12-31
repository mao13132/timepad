# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from settings import BLACK_LIST


class CheckBlack:
    @staticmethod
    def check_black(msg_text):

        for black in BLACK_LIST:
            try:
                if black.lower() in msg_text.lower():

                    print(f'Найдено стоп слово "{black}" пропускаю пост "{msg_text}"')

                    return True
            except Exception as es:
                print(f'При проверки на блек слова исключение "{es}" - игнорирую')

        return False
