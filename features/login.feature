@login_feature
Feature: Login to The Amazon Account and search products and get their Prices.

  Background:
    Given Launch the browser
    When Open the https://amazon.in website
    Then The login portal has been opened

  @search_product
  Scenario: Search the products on Amazon
    Given User is on the Amazon Website
    When When a user enters "Sun Glasses" in the search field,
    Then The autocomplete section of the search field displays various keywords related to that keyword
    When User selects the first option from the autocomplete section
    Then User sees the price and the product details of that product


  @Login
  Scenario: Login To Amazon.in
    Given User is on the Amazon Website
    When User enters valid user credentials and clciks the login button
    Then User sees personal home page of the amazon.in website

  @apply_filters
  Scenario: Login to the account, search the products and add the product to the card.
    Given User is on the Amazon Website
    When User enters valid user credentials and clciks the login button
    Then User sees personal home page of the amazon.in website
    When When a user enters "Sun Glasses" in the search field,
    Then The autocomplete section of the search field displays various keywords related to that keyword
    When User selects the first option from the autocomplete section
    Then User sees the price and the product details of that product
    When User applies filter as per the following data
      | Type         | Name         |
      | Delivery Day | Get It Today |
      | Prime        | Amazon Prime |
      | Reviews      | 5            |
      | Brand        | Fastrack     |
      | Discount     | 60%          |