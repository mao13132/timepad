# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logic.clear_age import clear_age

category_list = ['Концерты', 'Искусство и культура', 'Экскурсии и путешествия', 'Вечеринки',
                 'Для детей', 'Театры', 'Бизнес', 'Психология и самопознание', 'Наука', 'ИТ и интернет',
                 'Другие события', 'Спорт', 'Выставки', 'Интеллектуальные игры', 'Хобби и творчество',
                 'Кино', 'Другие развлечения', 'Красота и здоровье', 'Еда', 'Иностранные языки',
                 'Гражданские проекты', 'Образование за рубежом']


def search_category_(text_msg):
    category = 'Искусство и культура'

    if text_msg is None:
        return category

    for cat in category_list:
        if cat.lower() in text_msg.lower():
            category = cat

    return category
