# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def search_city_func(text_msg):
    if '📍 г.о. ' in text_msg:
        city = text_msg.split('📍 г.о. ')[-1]

        city = city.split(',')[0]

    else:
        print(f'Не могу определить город "{text_msg}"')

        city = ''

    return city
