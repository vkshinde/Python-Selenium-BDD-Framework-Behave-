from behave import given
from behave import when
from behave import then
from behave import *


@given(u'Launch the browser')
def step_impl(context):
    print(u'STEP: Given Launch the browser')


@when(u'Open the https://amazon.in website')
def step_impl(context):
    print(u'STEP: When Open the https://amazon.in website')


@then(u'The login portal has been opened')
def step_impl(context):
    print(u'STEP: Then The login portal has been opened')


@given(u'User is on the Amazon Website')
def step_impl(context):
    print(u'STEP: Given User is on the Amazon Website')


@when(u'When a user enters "Sun Glasses" in the search field,')
def step_impl(context):
    print(u'STEP: When When a user enters "Sun Glasses" in the search field,')


@then(u'The autocomplete section of the search field displays various keywords related to that keyword')
def step_impl(context):
    print(
        u'STEP: Then The autocomplete section of the search field displays various keywords related to that keyword')


@when(u'User selects the first option from the autocomplete section')
def step_impl(context):
    print(u'STEP: When User selects the first option from the autocomplete section')


@then(u'User sees the price and the product details of that product')
def step_impl(context):
    print(u'STEP: Then User sees the price and the product details of that product')


@when(u'User enters valid user credentials and clciks the login button')
def step_impl(context):
    print(u'STEP: When User enters valid user credentials and clciks the login button')


@then(u'User sees personal home page of the amazon.in website')
def step_impl(context):
    print(u'STEP: Then User sees personal home page of the amazon.in website')


@when(u'User applies filter as per the following data')
def step_impl(context):
    print(u'STEP: When User applies filter as per the following data')
