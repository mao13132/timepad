# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logic.clear_price import clear_price


def search_price(text_msg):
    row_list = text_msg.split('\n')

    price = 0

    for row in row_list:
        if 'тоимость' in row or 'Цена' in row:
            price_ = row

            if 'есплатно' in row:
                price = 0

            else:

                price = clear_price(price_)

    for row in row_list:
        if 'Вход свободный' in row:
            price = 0

    return price
