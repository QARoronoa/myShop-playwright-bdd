
Feature: Create account

  Scenario: create an account with new valid credentials
    Given the user is on the home page
    When they click the "Sign in" button
    Then Authentification title is visible
    When Enter new adress email <email>
    And they click on button create account
    When they fill form create account and they click on button Create account
    Then The user see the success message account created

    Scenario: create an account with with field email address empty
      Given the user is on the home page
      When they click the "Sign in" button
      Then Authentification title is visible
      And they click on button create account
      Then The user see the error message invalid email address

    Scenario Outline: create an account with an existing email
      Given the user is on the home page
      When they click the "Sign in" button
      Then Authentification title is visible
      When Enter an existing email <email>
      And they click on button create account
      Then The user see the error message account created

      Examples:
        |email              |
        |roronoa12@ymail.com|