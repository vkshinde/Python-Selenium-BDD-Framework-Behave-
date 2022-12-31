@login_feature
Feature: Login to The flipkart Account and search products and get their Prices.



  @Login
  Scenario: Login To flipkart.com
    Given User is on the homepage of the flipkart Website
    When User enters valid user credentials as per the "loginDetails" sheet and clciks the login button
      | column Name |
      | UserName   |
    Then User sees "Vishal"'s profile on the home page of the flipkart.com website


  @search_product
  Scenario: Login to the account, search the products and add the product to the card.
    Given User is on the homepage of the flipkart Website
    When User enters "Sun Glasses" in the search field
    Then The autocomplete section of the search field displays various keywords related to that keyword
    When User selects the first option from the autocomplete section
    Then User sees the price and the product details of first recommended product
