import os
import platform

import undetected_chromedriver as uc

import getpass

from settings import dir_project


class CreatBrowser:

    def __init__(self, name_profile):
        options = uc.ChromeOptions()

        options.add_argument("start-maximized")

        options.add_argument('--no-sandbox')

        options.add_argument('--disable-dev-shm-usage')

        options.add_argument('ignore-certificate-errors')

        options.add_argument("--log-level=3")

        path_dir = (f'{dir_project}\\src\\browser\\profile\\{name_profile}')

        options.add_argument(f'--user-data-dir={path_dir}')

        _patch = f"{dir_project}\\src\\browser\\chromedriver.exe"

        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/120.0.0.0 Safari/537.36")

        try:
            self.driver = uc.Chrome(driver_executable_path=_patch, options=options)
        except Exception as es:
            error = (f'Ошибка создания браузера "{es}"')

            print(error)

            self.driver = False

        if self.driver:

            try:
                browser_version = self.driver.capabilities['browserVersion']

                driver_version = self.driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]

                print(f"\nБраузер: {browser_version} драйвер: {driver_version}")

            except:

                print(f'\nНе получилось определить версию uc браузера')
