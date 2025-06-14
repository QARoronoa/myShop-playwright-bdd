from playwright.sync_api import Page, expect


class SearchPage:
    def __init__(self, page: Page):
        self.page = page

    #locators
        self.search_result_found = page.locator('.heading-counter')

    #methodes
    def verify_search_page_title(self):
        expect(self.page).to_have_title("Search - My Shop")

    def verify_search_result(self, result):
        expect(self.search_result_found).to_contain_text(result)