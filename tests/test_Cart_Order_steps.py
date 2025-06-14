import time

from pytest_bdd import scenarios, given, when, step, then, parsers

from pagesObjects.CreateAccountPage import CreateAccountPage
from pagesObjects.ProductPage import ProductPage
from pagesObjects.HomePage import HomePage
from pagesObjects.ItemDetailPage import ItemDetailPage
from pagesObjects.CartPage import CartPage
from tests.test_Authentification_steps import User_enter_mail_and_password, user_click_on_signIn_button
from tests.test_Create_account_steps import User_fill_form_creat_account
from tests.test_Navigation_Search_steps import User_mouss_over_women_category, User_see_tops_category

scenarios('../features/Cart_order.feature')

@given('the user is on the home page')
def user_is_in_home_page(browserInstance):
    pass

@when('the user clicks on the "Best Sellers" button')
def user_click_on_best_sellers_button(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.click_on_best_sellers_button()

@step('the user clicks on the "More" button of one item')
def user_click_on_more_button(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.scroll_into_item("Blouse")
    home_page.click_on_more_button("Blouse")

@step('the user is redirected to the item detail page')
def user_redirected_to_item_page(browserInstance):
    itemDetail_page = ItemDetailPage(browserInstance)
    itemDetail_page.verify_redirection_to_item_detail_page("Blouse")
    time.sleep(1)

@step('the user selects a color for the item')
def user_click_on_white_button(browserInstance):
    itemDetail_page = ItemDetailPage(browserInstance)
    itemDetail_page.click_on_white_color()


@then('the "Add to Cart" button should be displayed')
def user_see_add_to_cart_button(browserInstance):
    itemDetail_page = ItemDetailPage(browserInstance)
    itemDetail_page.verify_button_add_to_cart_is_visible()

@when('the user clicks on the "Add to Cart" button')
def user_click_on_add_to_cart_button(browserInstance):
    itemDetail_page = ItemDetailPage(browserInstance)
    itemDetail_page.click_on_add_to_cart()
    itemDetail_page.verify_item_is_in_cart()

@step('the user clicks on proceed to checkout button')
def user_click_on_proceed_to_checkout(browserInstance):
    itemDetail_page = ItemDetailPage(browserInstance)
    itemDetail_page.click_on_proceed_to_checkout()

@then('the "Shopping Cart" title should be visible')
def user_see_shopping_cart_title(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_shopping_cart_summuary_is_visble()

@step('the selected item should be present in the cart')
def user_see_item_in_card(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_item_is_visible("Blouse")

@step('the user click on delete button')
def user_click_on_delete_button(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.click_on_delete_button()

@then('the user see message "Your shopping cart is empty."')
def user_see_message_cart_empty(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_message_empty_card_is_visible()

@when('the user mouss over women category')
def user_hovers_over_mouss_category(browserInstance):
    User_mouss_over_women_category(browserInstance)

@then('the user see Tops')
def user_see_subcategory_tops(browserInstance):
    User_see_tops_category(browserInstance)

@when('the user click on blouses link')
def user_click_on_blouses_links(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.click_on_Blouses_link()

@then('the user see blouses page')
def user_redirected_to_blouse_page(browserInstance):
    product_page = ProductPage(browserInstance)
    product_page.verify_title_page("Blouses - My Shop")

@when('the user click on quick view')
def user_click_on_quick_view(browserInstance):
    product_page = ProductPage(browserInstance)
    product_page.click_on_quick_view_button()


@step('the user click on add to cart button and proceed to checkout button in popin')
def user_add_item_in_cart_from_popin(browserInstance):
    itmeDetail_page = ItemDetailPage(browserInstance)
    itmeDetail_page.click_add_to_cart_in_frame()

@then('the user see title shopping cart summary')
def user_see_title_shopping_cart(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_shopping_cart_summuary_is_visble()

@when('the user click to proceed to checkout')
def user_see_proceed_to_checkout_button(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.click_proceed_to_checkout_link()

@then(parsers.parse('the user see authentication page and logs in {email} {password}'))
def user_logs(browserInstance, email, password):
    User_enter_mail_and_password(browserInstance, email, password)

@step('the user click on sign in button')
def user_see_signIn_button_and_click_it(browserInstance):
    user_click_on_signIn_button(browserInstance)

@when('the user redirected to step 3 address and click to proceed to checkout')
def user_see_step3_address(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_step("Address")
    cart_page.click_proceed_to_checkout_button()


@step('the user redirected to step 4 shipping')
def user_see_title_addresses(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_page_title_is_visible("Shipping:")

@step('the user accept terms of service and click to proceed to checkout')
def user_accept_terms_of_service(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.click_on_radio_button_terms_of_service()
    cart_page.click_proceed_to_checkout_button()

@then('the user redirected to payment page')
def user_see_payment_page(browserInstance):
    cart_page = CartPage(browserInstance)
    cart_page.verify_page_title_is_visible("Please choose your payment method")
















