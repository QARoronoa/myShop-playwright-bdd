import pytest
from data.data_login import Login
from data.data_Addresses import Addresses


@pytest.fixture(scope="function")
def browserInstance(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("http://www.automationpractice.pl/index.php")
    yield page

    context.close()
    browser.close()


@pytest.fixture(scope="function")
def saisir_email_create_account():
    return Login.createAccountEmail()

@pytest.fixture(scope="function")
def remplir_form_create_account():
    return Login.form_information()

@pytest.fixture(scope="function")
def fill_adresses_form():
    return Addresses.adresses_form()