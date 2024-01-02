# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
from selenium.webdriver.common.by import By


def change_frame(driver):
    try:
        _frame = driver.find_element(by=By.XPATH,
                                     value=f"//*[contains(@class, 'mform_')]//iframe")
    except:
        return False

    try:
        driver.switch_to.frame(_frame)
    except:
        return False

    return True


def write_desc(driver, desc):
    try:
        insert_element = driver.find_element(by=By.XPATH,
                                             value=f"//body/p")
    except:
        return False
    try:
        insert_element.click()
    except:
        return False

    try:
        driver.execute_script(
            f'''
                               const text = `{desc}`;
                               const dataTransfer = new DataTransfer();
                               dataTransfer.setData('text', text);
                               const event = new ClipboardEvent('paste', {{
                                 clipboardData: dataTransfer,
                                 bubbles: true
                               }});
                               arguments[0].dispatchEvent(event)
                               ''',
            insert_element)

    except Exception:

        print(f"Не смог вписать текст desc")
        return False

    return True


def loop_write_desc(driver, desc):
    res_change_frame = change_frame(driver)

    if not res_change_frame:
        return False

    res_write = write_desc(driver, desc)

    driver.switch_to.default_content()

    return res_write
