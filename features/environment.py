from configuration.config import TestData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = None


def before_scenario(context, feature):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        # options.add_argument('--start-fullscreen')
        options.add_argument('--single-process')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--incognito")
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument("disable-infobars")
        options.add_experimental_option("prefs", {"profile.default_content_setting_values.cookies": 2})
        # options.headless = True
        context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif TestData.BROWSER == 'firefox':

        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        context.driver = None

        raise ValueError('Browser is not supported')
    driver = context.driver


def after_scenario(context, scenario):
    context.driver.close()
