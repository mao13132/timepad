# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def search_date(text_msg):
    row_list = text_msg.split('\n')

    date = ''

    target = '📆 '

    for row in row_list:
        if target in row:
            date_ = row.split(target)[-1]

            date = date_.split()[0]

    return date
