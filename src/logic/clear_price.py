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

    try:
        price = float(price)
    except:
        print(f'\nУстанавливаю 0 цену т.к. не могу вытащить её из "{value}"\n')

        price = 0

    return price
