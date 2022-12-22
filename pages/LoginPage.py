import logging
import time

import selenium.common.exceptions

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TXT_USERNAME = (By.XPATH, "//div[@class=\"desk\"]//input[@id=\"email\"][@placeholder=\"Email\"]")
    TXT_PASSWORD = (By.XPATH, "//div[@class=\"desk\"]//input[@id=\"password\"]")
    BTN_LOGIN = (By.XPATH, "//div[@class=\"landing_white_button\"][text()=\"Log in\"]")
    BTN_After_LOGIN = (By.XPATH, "//div[@id=\"login_button_desktop\"]")

    BTN_LOGOUT = (By.XPATH, '//div[@class="desk"]//b[text()="Logout"]')

    BTN_DASHBOARD = (By.XPATH, '//b[text()="Dashboard"]')

    BTN_DASHBOARD_JS = "changePage('/dashboard');"

    """Constructor of CarrersPage class"""

    def __init__(self, driver):
        super().__init__(driver)

