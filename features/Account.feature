Feature: Account

 @skip
  Scenario Outline: User add his first address
    Given the user is on the home page
    When they click the "Sign in" button
    Then they enter a valid email address <email> and password <password>
    And they click on sign in button
    Then they are redirected to their account dashboard
    When the user click on add my first address
    Then they are redirected to address form page
    When the user fill form
    And the user click on save button


    Examples:
      | email               | password |
      | roronoa12@ymail.com | 123456   |