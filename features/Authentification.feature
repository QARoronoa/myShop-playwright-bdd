
Feature: Authentification

  Scenario Outline: Se connecter avec des credentials valides
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When they enter a valid email address <email> and password <password>
    And they click on sign in button
    Then they are redirected to their account dashboard

    Examples:
      | email              | password |
      | roronoa12@ymail.com|123456    |


   Scenario Outline: Se connecter avec des credentials invalides
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When they enter a invalid email address <email> and password <password>
    And they click on sign in button
    Then error message is visible

    Examples:
      | email                 | password |
      | roronosssa12@ymail.com|123ss456  |

  Scenario Outline: Se connecter avec un email inexistant
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When they enter a invalid email address <email> and password <password>
    And they click on sign in button
    Then error message is visible

    Examples:
      | email                 | password |
      | roronosssa@ymail.com|123456  |

    Scenario Outline: user click on logout button after login
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When they enter a valid email address <email> and password <password>
    And they click on sign in button
    Then they are redirected to their account dashboard
    When user click on sign out button
    Then Authentication title is visible

    Examples:
      | email              | password |
      | roronoa12@ymail.com|123456    |

  Scenario: user click on "forgot your password link"
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When the user click on forgot your password
    Then the user he redirected to forgot your password
    When the user enter an email address
    And the user clicks on "Retrieve Password" button
    Then the user sees a message confirming that an email has been sent

   Scenario: user click on "forgot your password link" and enter an email nonexistent
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentication title is visible
    When the user click on forgot your password
    Then the user he redirected to forgot your password
    When the user enter an nonexistent email address
    And the user clicks on "Retrieve Password" button
    Then the user sees a message confirming email is not registered