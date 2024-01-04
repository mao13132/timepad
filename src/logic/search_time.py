# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def search_time(text_msg):
    row_list = text_msg.split('\n')

    time = ''

    target = '🕕 '

    for row in row_list:
        if target in row:
            time = row.split(target)[-1]

            time = time.strip()

    return time
