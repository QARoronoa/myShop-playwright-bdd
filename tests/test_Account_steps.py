import time

import pytest
from pytest_bdd import scenarios, given, when, then, step, parsers

from pagesObjects.HomePage import HomePage
from pagesObjects.MyAccountPage import MyAccountPage
from tests.test_Authentification_steps import User_enter_mail_and_password, user_click_on_signIn_button


scenarios('../features/Account.feature')

@given('the user is on the home page')
def User_is_on_home_page(browserInstance):
    pass

@when('they click the "Sign in" button')
def User_click_signIn(browserInstance):
    home_page= HomePage(browserInstance)
    home_page.click_on_signIn_button()

@then(parsers.parse('they enter a valid email address {email} and password {password}'))
def user_fill_credentials(browserInstance, email, password):
    User_enter_mail_and_password(browserInstance, email, password)

@step('they click on sign in button')
def user_press_sign_in_button(browserInstance):
    user_click_on_signIn_button(browserInstance)

@then('they are redirected to their account dashboard')
def user_see_account_page(browserInstance):
    myAccount_page = MyAccountPage(browserInstance)
    myAccount_page.verify_title_page("My account - My Shop")

@when('the user click on add my first address')
def user_press_on_link_add_address(browserInstance):
    myAccount_page = MyAccountPage(browserInstance)
    myAccount_page.click_on_add_my_first_address()

@then('they are redirected to address form page')
def user_see_address_form(browserInstance):
    myAccount_page = MyAccountPage(browserInstance)
    myAccount_page.verify_title_page("Address - My Shop")

@when('the user fill form')
def user_add_his_first_address(browserInstance, fill_adresses_form):
    myAccount_page = MyAccountPage(browserInstance)
    myAccount_page.fill_addresses_form_order(fill_adresses_form["address"],
                                             fill_adresses_form["city"],
                                             fill_adresses_form["cp"],
                                             fill_adresses_form["homePhone"],
                                             fill_adresses_form["mobilePhone"])

@step('the user click on save button')
def user_press_on_save_button(browserInstance):
    myAccount_page = MyAccountPage(browserInstance)
    myAccount_page.click_on_save_button()

