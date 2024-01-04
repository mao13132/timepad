# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from src.logic.clear_age import clear_age


def search_age(text_msg):
    row_list = text_msg.split('\n')

    age = ''

    for row in row_list:
        if 'озраст' in row:
            age = row.split()[-1]

            age = clear_age(age)

    return age
