import os
import platform
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import zipfile

import getpass

from settings import dir_project, IS_ACTIVE_BROWSER


class CreatBrowser:
    def __init__(self):

        name_profile = 'timepad'

        options = webdriver.ChromeOptions()

        user_system = getpass.getuser()

        options.add_argument(
            f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/120.0.0.0 Safari/537.36")

        path_dir = (f'{dir_project}\\src\\browser\\profile\\{name_profile}')

        _patch = f"{dir_project}\\src\\browser\\chromedriver.exe"

        s = Service(executable_path=_patch)

        options.add_argument(f'--user-data-dir={path_dir}')

        if not IS_ACTIVE_BROWSER:
            options.add_argument("--headless")

        prefs = {"enable_do_not_track": True}

        options.add_experimental_option("prefs", prefs)

        options.add_argument("--disable-blink-features=AutomationControlled")

        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        options.add_argument("--disable-infobars")

        options.add_argument("--disable-bundled-ppapi-flash")

        options.add_argument("--disable-application-cache")

        options.add_argument("window-size=1920,939")

        options.add_argument("--dns-prefetch-disable")
        options.add_argument("--disable-gpu")

        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('ignore-certificate-errors')
        options.add_argument("--log-level=3")
        tz_params = {'timezoneId': 'Asia/Almaty'}

        try:

            self.driver = webdriver.Chrome(service=s, options=options)

        except Exception as es:
            print(f'Ошибка при создания браузера "{es}"')

            self.driver = False

        self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            'source': '''
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
                        delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
                  '''
        })

        self.driver.execute_cdp_cmd('Emulation.setTimezoneOverride', tz_params)

        try:
            browser_version = self.driver.capabilities['browserVersion']
            driver_version = self.driver.capabilities['chrome']['chromedriverVersion'].split(' ')[0]
            print(
                f'\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} Браузер: {browser_version} драйвер: {driver_version}')
        except:
            print(f'\nНе получилось определить версию uc браузера')
