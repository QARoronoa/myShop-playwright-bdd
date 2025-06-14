from playwright.sync_api import Page, expect


class CreateAccountPage:

    def __init__(self, page: Page):
        self.page = page

    #locators
        self.gender_mrs = page.locator('#id_gender1')
        self.firstName = page.locator("#customer_firstname")
        self.lastName = page.locator("#customer_lastname")
        self.password = page.locator("#passwd")
        self.dayBirth = page.locator('#days')
        self.monthBirth = page.locator('#months')
        self.yearBirth = page.locator('#years')
        self.register_button = page.locator("#submitAccount")
        self.success_message = page.locator("p.alert.alert-success")

    #methodes

    def fill_account_form(self, firstName, lastName,pwd,day, month,years):
        self.gender_mrs.click()
        self.firstName.fill(firstName)
        self.lastName.fill(lastName)
        self.password.fill(pwd)
        self.dayBirth.select_option(value=day)
        self.monthBirth.select_option(value=month)
        self.yearBirth.select_option(value=years)
        self.register_button.click()

    def verify_success_mess_account_created(self):
        expect(self.success_message).to_have_text("Your account has been created.")


