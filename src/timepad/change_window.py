# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------


async def change_windows(driver, select_window):
    try:
        driver.switch_to.window(driver.window_handles[select_window])
    except Exception as es:
        print(f'Runner: Не могу сменить окно ({select_window}) "{es}"')

        return False

    return True
