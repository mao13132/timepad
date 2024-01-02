# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import requests


class TimePadApi:
    def __init__(self, settings):
        self.category = ['Нет', 'Концерты', 'Искусство и культура', 'Экскурсии и путешествия', 'Вечеринки',
                         'Для детей', 'Театры', 'Бизнес', 'Психология и самопознание', 'Наука', 'ИТ и интернет',
                         'Другие события', 'Спорт', 'Выставки', 'Интеллектуальные игры', 'Хобби и творчество',
                         'Кино', 'Другие развлечения', 'Красота и здоровье', 'Еда', 'Иностранные языки',
                         'Гражданские проекты', 'Образование за рубежом']

        self.settings = settings

        self.url = f'https://api.timepad.ru/'

    def start_add_post(self):
        category = self.settings['category'] if self.settings['category'] in self.category else 'Искусство и культура'

        url = f'{self.url}v1/events'

        header_ = {'Content-Type': 'application/json',
                   'Authorization': f'Bearer {self.settings["api_key"]}'
                   }

        # data = {
        #     'organization': {
        #         'id': self.settings['organization']
        #     },
        #     'starts_at': self.settings['start_date'],
        #     'name': self.settings['name'],
        #     'categories': [
        #         {
        #             'name': category
        #         }
        #     ]
        # }

        data = {"organization": {
            "id": self.settings['organization'],
            "subdomain": "laboratoriya-event.timepad.ru"
        },
            "starts_at": "2024-01-12T11:28:30.293Z",
            # "ends_at": "2024-01-02T11:28:30.293Z",
            "name": self.settings['name'],
            "categories": [
                {
                    "id": 525,
                    "name": category
                }]
        }

        try:
            response = requests.post(url, headers=header_, json=data)

            data_response = response.json()

            if response.status_code == 200 and data_response == []:
                print(f'OZON INFO PRODUCTS: Нулевой ответ от серверов')

        except Exception as es:
            print(f'OZON INFO PRODUCTS: Ошибка при получение информации по продуктам "{es}"')

            return '-1'

        return data_response


if __name__ == '__main__':
    settings = {
        'api_key': 'f4017e3910c3809dc7e12bb4ba5fd672f7b6a8be',
        'organization': 370017,
        'start_date': '2024-01-12',
        'name': 'тестовое событие',
        'category': 'Искусство и культура'
    }

    TimePadApi(settings).start_add_post()
