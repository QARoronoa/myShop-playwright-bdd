import time
from pytest_bdd import scenarios, given, when, then, parsers, step
from pagesObjects.AccountPage import AccountPage
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage
from pagesObjects.CreateAccountPage import CreateAccountPage

scenarios("../features/createAccount.feature")

@given('the user is on the home page')
def User_is_on_home_page(browserInstance):
    pass

@when('they click the "Sign in" button')
def User_click_signIn(browserInstance):
    home_page= HomePage(browserInstance)
    home_page.click_on_signIn_button()

@then('Authentication title is visible')
def User_visualise_authentication_title(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.visualiser_le_titre_authentification()

@when(parsers.parse('Enter new address email {email}'))
def User_enter_new_address_email(browserInstance, saisir_email_create_account):
    login_page = LoginPage(browserInstance)
    login_page.enter_email_create_acount(saisir_email_create_account["email"])

@when(parsers.parse('Enter an existing email {email}'))
def User_enter_existing_email(browserInstance, email):
    login_page = LoginPage(browserInstance)
    login_page.enter_email_create_acount_with_existing_email(email)

@when(parsers.parse('Enter an invalid email {email}'))
def user_enter_an_invalid_email(browserInstance, email):
    login_page = LoginPage(browserInstance)
    login_page.enter_email_create_acount_with_existing_email(email)


@step('they click on button create account')
def User_click_on_button_create_account(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.click_on_button_create_account()

@when(parsers.parse('they fill form create account and they click on button Create account'))
def User_fill_form_creat_account(browserInstance, remplir_form_create_account):
    createAccouunt_page = CreateAccountPage(browserInstance)
    createAccouunt_page.fill_account_form(remplir_form_create_account["firstName"],
                                          remplir_form_create_account["lastName"],
                                          remplir_form_create_account["pwd"],
                                          remplir_form_create_account["day"],
                                          remplir_form_create_account["month"],
                                          remplir_form_create_account["years"])

@then('The user see the success message account created')
def User_see_success_message_create_account(browserInstance):
    createAccouunt_page = CreateAccountPage(browserInstance)
    createAccouunt_page.verify_success_mess_account_created()

@then('The user see the error message account created')
def User_see_error_message_create_account(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_error_message_create_account("An account using this email address has already been registered. Please enter a valid password or request a new one. ")

@then('The user see the error message "invalid address"')
def User_see_error_invalid_address(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_error_message_create_account("Invalid email address.")
@then('The user see the error message invalid email address')
def User_see_error_message_invalid_address(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_error_message_create_account("Invalid email address.")
