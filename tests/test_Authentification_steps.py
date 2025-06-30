import time
from pytest_bdd import scenarios, given, when, then, parsers, step
from pagesObjects.AccountPage import AccountPage
from pagesObjects.HomePage import HomePage
from pagesObjects.LoginPage import LoginPage

scenarios("../features/Authentification.feature")

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

@when(parsers.parse('they enter a valid email address {email} and password {password}'))
def User_enter_mail_and_password(browserInstance, email, password):
    login_page = LoginPage(browserInstance)
    login_page.enter_user_credentials(email, password)

@when(parsers.parse('they enter a invalid email address {email} and password {password}'))
def User_enter_mail_and_password(browserInstance, email, password):
    login_page = LoginPage(browserInstance)
    login_page.enter_user_credentials(email, password)

@step('they click on sign in button')
def user_click_on_signIn_button(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.click_on_signin_button()

@then('they are redirected to their account dashboard')
def user_are_redirected_on_account_dashbord(browserInstance):
    account_page = AccountPage(browserInstance)
    account_page.visualiser_le_titre_My_account()

@then('error message is visible')
def user_visualize_error_message(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.visualiser_le_titre_authentification()

@when('user click on sign out button')
def user_click_on_signOut_button(browserInstance):
    home_page = HomePage(browserInstance)
    home_page.click_on_signOut_button()


@when('the user click on forgot your password')
def user_click_on_forgot_your_password(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.click_on_forgot_password_link()

@then('the user he redirected to forgot your password')
def user_see_forgot_your_password_title(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_title_page("Forgot your password - My Shop")

@when('the user enter an email address')
def user_fill_emailAddress_forgot_password(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.fill_emailAddress_field_forgot_password("roronoa12@ymail.com")

@when('the user enter an nonexistent email address')
def user_fill_emailAddress_forgot_password(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.fill_emailAddress_field_forgot_password("cddf@ymail.com")

@step('the user clicks on "Retrieve Password" button')
def user_click_on_Retrieve_Password_button(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.click_on_retrieve_password_button()

@then('the user sees a message confirming that an email has been sent')
def user_see_cinfirming_message(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_alert_message_forgot_password("A confirmation email")

@then('the user sees a message confirming email is not registered')
def user_see_cinfirming_message(browserInstance):
    login_page = LoginPage(browserInstance)
    login_page.verify_alert_message_forgot_password("There is 1 error")




