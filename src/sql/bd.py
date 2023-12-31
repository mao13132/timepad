import datetime
import sqlite3
from datetime import datetime


class BotDB:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __init__(self, db_file):
        try:

            self.conn = sqlite3.connect(db_file, timeout=30)
            print('Подключился к SQL DB:', db_file)
            self.cursor = self.conn.cursor()
            self.check_table()
        except Exception as es:
            print(f'Ошибка при работе с SQL {es}')

    def check_table(self):

        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS "
                                f"monitoring (id_pk INTEGER PRIMARY KEY AUTOINCREMENT, "
                                f"id_chat TEXT, id_msg TEXT, organization TEXT, date_post DATETIME, date DATETIME, other TEXT)")

        except Exception as es:
            print(f'SQL исключение check_table monitoring {es}')

    def exist_message(self, id_chat, id_msg, date_post, organization):
        result = self.cursor.execute(f"SELECT * FROM monitoring "
                                     f"WHERE id_chat='{id_chat}' AND id_msg='{id_msg}' "
                                     f"AND date_post='{date_post}' AND organization='{organization}'")

        response = result.fetchall()

        if response == []:
            return False

        return True

    def add_message(self, id_chat, id_msg, date_post, organization):

        now_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        self.cursor.execute("INSERT OR IGNORE INTO monitoring ('id_chat',"
                            "'id_msg', 'organization', "
                            "'date', 'date_post') VALUES (?,?,?,?,?)",
                            (id_chat, id_msg, organization,
                             now_date, date_post,))

        self.conn.commit()
        return True

    def close(self):
        # Закрытие соединения
        self.conn.close()
        print('Отключился от SQL BD')
