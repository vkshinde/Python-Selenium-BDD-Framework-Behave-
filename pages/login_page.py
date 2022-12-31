import logging
import time

import selenium.common.exceptions

from pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    TXT_USERNAME = (By.XPATH, "/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input")
    BTN_LOGIN = (By.XPATH, "//button[text()=\"Request OTP\"]")
    BTN_VERIFY = (By.XPATH, "//button[text()=\"Verify\"]")
    """Constructor of CarrersPage class"""
    BTN_CLOSE = (By.XPATH, '//button[text()="✕"]')
    SEARCH_INPUT = (By.XPATH, '//input[contains(@title, "Search for products, brands and more")]')
    FIRST_OPTION = (By.XPATH, '(//form//li//a)[1]')
    # FIRST_RESULT = (By.XPATH, '(//*[@id="container"]//*[contains(text(),"' + product_name + '")])[1]')
    # self.click_element(FIRST_RESULT)
    SELLER_NAME = (By.XPATH, '((//a[@rel="noopener noreferrer"]/parent::*)[2]//div)[1]')
    PRODUCT_NAME = (By.XPATH, '((//a[@rel="noopener noreferrer"]/parent::*)[2]//a)[1]')
    PRODUCT_PRICE = (By.XPATH, '(((//a[@rel="noopener noreferrer"]/parent::*)[2]//a)[2]/div/div)[1]')

    def __init__(self, driver, file):
        super().__init__(driver, file=file)

    def open_page(self, url):
        self.load_url(url)
        time.sleep(2)

    def enter_login_details(self, username):
        self.input_element(self.TXT_USERNAME, username)
        self.click_element(self.BTN_LOGIN)
        time.sleep(60)

    def verify(self, name):
        name_path = (By.XPATH, f"//*[contains(text(), '{name}')]")

        return self.verify_element_displayed(name_path)

    def search_product(self, product_name):

        self.click_element(self.BTN_CLOSE)
        self.input_element(self.SEARCH_INPUT, product_name)

    def record_the_dropdown_option(self):
        self.takeScreenShotOfThePage()
        with open("output.txt", "a+") as file:
            file.writelines("\n\n Drop Down Options \n\n")
            i = 0
            for element in (self.return_list('//form//li//a//div[2]//span')):
                i += 1
                file.writelines(str(i) + "." + element.text + "\n")

    def select_first_option(self):
        self.click_element(self.FIRST_OPTION)

    def check_product_info(self):
        self.takeScreenShotOfThePage()
        with open("output.txt", "a+") as file:
            file.writelines("\n\n Product details \n\n")
            file.writelines("- Product Name:" + self.get_element_text(self.PRODUCT_NAME))
            file.writelines("- Supplier Name:" + self.get_element_text(self.SELLER_NAME))
            file.writelines("- Product Price:" + self.get_element_text(self.PRODUCT_PRICE))
