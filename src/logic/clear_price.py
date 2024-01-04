# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
def clear_price(value: str):
    symbol = [',', '.']

    price = ''

    for x in value:
        if x.isdigit() or x in symbol:
            price += x

    price = float(price)

    return price
