from playwright.sync_api import Page, expect


class AccountPage:

    def __init__(self, page: Page):
        self.page = page

    #locators
        self.myAccount_title = page.locator(".page-heading")


    #methodes
    def visualiser_le_titre_My_account(self):
        expect(self.myAccount_title).to_contain_text("My account")
