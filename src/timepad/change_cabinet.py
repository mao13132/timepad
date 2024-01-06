# ---------------------------------------------
# Program by @developer_telegrams
#
#
# Version   Date        Info
# 1.0       2023    Initial Version
#
# ---------------------------------------------
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from src.timepad.close_popup import close_popup


class ChangeCabinet:
    def __init__(self, settings):
        self.settings = settings

        self.driver = settings['driver']

    def lower_value(self, value: str):
        try:
            value = value.lower()
        except:
            pass

        return value

    def get_cabinet_name(self):
        self.move_popup()

        try:
            org_name = self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'org-name')]").text
        except:
            return False

        return org_name

    def move_popup(self):
        for _try in range(3):
            try:
                panel = self.driver.find_element(by=By.XPATH, value=f"//*[contains(@aria-describedby,'popup-1')]")
            except:
                time.sleep(1)

                continue

            try:
                ActionChains(self.driver).move_to_element(panel).perform()
            except:
                time.sleep(1)

                continue

            return True

        print(f'Не смог открыть меню с организациями')

        return False


    def check_status_popup(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'popup-hovered-trigger')]")
        except:
            return False

        return True

    def click_change_menu_item(self):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'dropdow')]"
                                                        f"//*[contains(@class, 'change')]").click()
        except:
            return False

        return True

    def click_org_name(self, organization):
        try:
            self.driver.find_element(by=By.XPATH, value=f"//*[contains(@class,'dropdow')]"
                                                        f"//*[contains(@class, 'org') and "
                                                        f"contains(text(), '{organization}')]").click()
        except:
            return False

        return True

    def _change_cabinet(self, organization):
        for _try in range(2):
            move_popup = self.move_popup()

            if not move_popup:
                time.sleep(1)

                continue

            is_open = self.check_status_popup()

            if not is_open:
                time.sleep(1)

                continue

            open_change_item = self.click_change_menu_item()

            if not open_change_item:
                time.sleep(1)

                continue

            time.sleep(2)

            click_org = self.click_org_name(organization)

            if not click_org:
                print(f'Не могу найти организацию "{organization}"')

                time.sleep(1)

                continue

            return True

    def loop_change(self, organization):
        for _try in range(2):

            site_org = self.get_cabinet_name()

            site_org = self.lower_value(site_org)

            _organization = self.lower_value(organization)

            if _organization not in site_org:
                change_res = self._change_cabinet(organization)

                time.sleep(1)

                continue

            return True

        print(f'Все попытки сменить организацию на "{organization}" исчерпаны')

        return False

    def start_change(self, organization):
        res_chane_cabinet = self.loop_change(organization)

        return res_chane_cabinet
