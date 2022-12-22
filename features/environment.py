from configuration.config import TestData
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def before_feature(context, feature):
    if TestData.BROWSER == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        # options.headless = True
        context.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    elif TestData.BROWSER == 'firefox':

        context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        context.driver = None

        raise ValueError('Browser is not supported')


def after_scenario(context, scenario):
    context.driver.close()
