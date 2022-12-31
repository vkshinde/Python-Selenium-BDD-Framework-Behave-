import logging
import time

from behave import *

from pages.login_page import LoginPage


@given(u'User is on the homepage of the flipkart Website')
def step_impl(context):
    context.login_page = LoginPage(context.driver, "Test_required_data/FlipkartTesting.xlsx")
    context.login_page.load_url("https://www.flipkart.com/")


@when(u'User enters "{product_name}" in the search field')
def step_impl(context, product_name):
    context.login_page.search_product(product_name)


@then(u'The autocomplete section of the search field displays various keywords related to that keyword')
def step_impl(context):
    context.login_page.record_the_dropdown_option()

@when(u'User selects the first option from the autocomplete section')
def step_impl(context):
    context.login_page.select_first_option()


@then(u'User sees list of the products')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then User sees list of the products')


@when(u'User selects first product, a new page will be opened')
def step_impl(context):
    raise NotImplementedError(u'STEP: When User selects first product, a new page will be opened')


@given(u'User is on the flipkart Website')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given User is on the flipkart Website')


@when(u'User enters valid user credentials as per the "{data}" sheet and clciks the login button')
def step_impl(context, data):
    excel_data = context.login_page.read_data(data)
    username = excel_data[str(context.table[0][0])][0]
    context.login_page.enter_login_details(username)

    with open("output.txt", 'a+') as file:
        file.writelines(str(username) + "\n")


@then(u'User sees "{name}"\'s profile on the home page of the flipkart.com website')
def step_impl(context, name):
    logging.info("Name is : "+ str(name)+" : "+context.login_page.verify('Vishal'))
    assert context.login_page.verify('Vishal'), "User not logged in."





@then(u'User sees the price and the product details of first recommended product')
def step_impl(context):
    context.login_page.check_product_info()

