# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def search_city_func(text_msg):
    row_list = text_msg.split('\n')

    for row in row_list:
        if 'г.о. ' in row:
            city = text_msg.split('г.о. ')[-1]

            if ',' in city:
                city = city.split(',')[0]

            if '\n' in city:
                city = city.split('\n')[0]

            return city

        if 'г. ' in row:
            city = text_msg.split('г. ')[-1]

            if ',' in city:
                city = city.split(',')[0]

            if '\n' in city:
                city = city.split('\n')[0]

            return city

    print(f'\nНе могу определить город "{text_msg}"')

    city = ''

    return city
