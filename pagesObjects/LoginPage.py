from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        #locators
        self.authentification_title = page.locator(".page-heading")
        self.email_field = page.locator("#email")
        self.password_field = page.locator("#passwd")
        self.signIn_button = page.locator("#SubmitLogin")
        self.mess_authentification_failed = page.locator("div.alert.alert-danger ol li")
        self.email_create_account = page.locator('#email_create')
        self.create_account_button =  page.locator('#SubmitCreate')
        self.error_message_create_account = page.locator('#create_account_error li')
        self.forgot_your_password_link = page.get_by_role("link", name="Forgot your password?")
        self.email_field_forgot_pwd = page.locator("#email")
        self.retrieve_password_button = page.get_by_role('button', name='Retrieve Password')
        self.alert_message_forgot_password = page.locator('.alert')


        #methodes

    def verify_title_page(self, title):
        expect(self.page).to_have_title(title)
    def visualiser_le_titre_authentification(self):
        expect(self.authentification_title).to_contain_text("Authentication")

    def enter_user_credentials(self, email,password):
        self.email_field.fill(email)
        self.password_field.fill(password)

    def enter_email_create_acount(self, email):
        self.email_create_account.fill(email)

    def enter_email_create_acount_with_existing_email(self,email):
        self.email_create_account.fill(email)

    def click_on_button_create_account(self):
        self.create_account_button.click()

    def click_on_signin_button(self):
        self.signIn_button.click()

    def verifier_la_presence_message_erreur(self):
        expect(self.mess_authentification_failed).to_have_text("Authentication failed.")

    def verify_error_message_create_account(self, message):
        expect(self.error_message_create_account).to_contain_text(message)

    def click_on_forgot_password_link(self):
        expect(self.forgot_your_password_link).to_be_visible()
        expect(self.forgot_your_password_link).to_be_enabled()
        self.forgot_your_password_link.click()

    def fill_emailAddress_field_forgot_password(self, email):
        expect(self.email_field_forgot_pwd).to_be_visible()
        expect(self.email_field_forgot_pwd).to_be_empty()
        self.email_field_forgot_pwd.fill(email)

    def click_on_retrieve_password_button(self):
        expect(self.retrieve_password_button).to_be_enabled()
        self.retrieve_password_button.click()

    def verify_alert_message_forgot_password(self, text):
        expect(self.alert_message_forgot_password).to_be_visible()
        expect(self.alert_message_forgot_password).to_contain_text(text)
