Feature: Navigation & Search


  Scenario: Search an existing item
    Given the user is on the home page
    When the user enters "t-shirt" in the search bar
    And clicks the search button
    Then search results for "t-shirt" should be displayed

  Scenario: Search an nonexistent item
    Given the user is on the home page
    When the user enters "bermuda" in the search bar
    And clicks the search button
    Then search results for "bermuda" zero results have been found

  Scenario: The user explores the “Women > Tops > T-shirts” section
    Given the user is on the home page
    When the user mouss over women category
    Then the user see Tops
    When the user click on tshirt link
    Then the user see tshirt page





