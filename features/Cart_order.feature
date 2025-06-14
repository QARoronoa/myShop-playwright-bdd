Feature: Cart & Order

    Scenario: User adds an item to the cart from the item detail page
      Given the user is on the home page
      When the user clicks on the "Best Sellers" button
      And the user clicks on the "More" button of one item
      And the user is redirected to the item detail page
      And the user selects a color for the item
      Then the "Add to Cart" button should be displayed
      When the user clicks on the "Add to Cart" button
      And the user clicks on proceed to checkout button
      Then the "Shopping Cart" title should be visible
      And the selected item should be present in the cart

  Scenario: User adds an item to the cart from the item detail page and remove it
      Given the user is on the home page
      When the user clicks on the "Best Sellers" button
      And the user clicks on the "More" button of one item
      And the user is redirected to the item detail page
      And the user selects a color for the item
      Then the "Add to Cart" button should be displayed
      When the user clicks on the "Add to Cart" button
      And the user clicks on proceed to checkout button
      Then the "Shopping Cart" title should be visible
      And the selected item should be present in the cart
      And the user click on delete button
      Then the user see message "Your shopping cart is empty."


  Scenario Outline: User adds an item to the cart until payment page
    Given the user is on the home page
    When the user mouss over women category
    Then the user see Tops
    When the user click on blouses link
    Then the user see blouses page
    When the user click on quick view
    And the user click on add to cart button and proceed to checkout button in popin
    Then the user see title shopping cart summary
    When the user click to proceed to checkout
    Then the user see authentication page and logs in <email> <password>
    And the user click on sign in button
    When the user redirected to step 3 address and click to proceed to checkout
    And the user redirected to step 4 shipping
    And the user accept terms of service and click to proceed to checkout
    Then the user redirected to payment page


    Examples:
      | email               | password |
      | roronoa12@ymail.com | 123456   |





