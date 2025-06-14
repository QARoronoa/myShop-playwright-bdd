import time
from pytest_bdd import scenarios, given, when, then, parsers, step
from pagesObjects.SearchPage import SearchPage
from pagesObjects.HomePage import HomePage
from  pagesObjects.ProductPage import ProductPage


scenarios("../features/Navigation_Search.feature")

@given('the user is on the home page')
def User_is_on_home_page(browserInstance):
    pass

@when('the user enters "t-shirt" in the search bar')
def User_enter_item_in_search_bar(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.enter_item_in_search_bar("T-shirt")

@when('the user enters "bermuda" in the search bar')
def User_enter_item_in_search_bar(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.enter_item_in_search_bar("bermuda")

@step('clicks the search button')
def user_click_on_search_button(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.click_on_search_button()

@then('search results for "t-shirt" should be displayed')
def User_see_1_result_found(browserInstance):
    search_page = SearchPage(browserInstance)
    search_page.verify_search_page_title()
    search_page.verify_search_result("1 result has been found.")

@then('search results for "bermuda" zero results have been found')
def User_see_zero_result_found(browserInstance):
    search_page = SearchPage(browserInstance)
    search_page.verify_search_page_title()
    search_page.verify_search_result("0 results have been found.")

@when('the user mouss over women category')
def User_mouss_over_women_category(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.mouss_over_element(home_page.link_women_category)

@then('the user see Tops')
def User_see_tops_category(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.element_is_visible(home_page.link_Tops)

@when('the user click on tshirt link')
def user_click_on_tshirt_links(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.click_on_tshirt_link()

@then('the user see tshirt page')
def user_navigate_to_tshirt_page(browserInstance):
    product_page = ProductPage(browserInstance)
    product_page.verify_title_page("T-shirts - My Shop")


