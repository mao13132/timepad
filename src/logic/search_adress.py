# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def search_address(text_msg):
    row_list = text_msg.split('\n')

    address = ''

    for row in row_list:
        if '📍' in row:
            address = row

            return address

    for row in row_list:
        if 'г.' in row:
            address = row

            return address

    print(f'\nАдрес не обнаружен "{text_msg}"\n')

    return ''
