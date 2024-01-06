# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def clear_age(value: str):
    age = ''

    for x in value:
        if x.isdigit():
            age += x

    try:
        age = int(age)
    except:
        age = 0

    return age
