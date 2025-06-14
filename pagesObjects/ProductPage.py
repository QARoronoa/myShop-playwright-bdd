import time

from playwright.sync_api import Page, expect


class ProductPage:
    def __init__(self, page: Page):
        self.page = page


    #locators
        self.quick_view_button= page.locator('.quick-view')
        self.blouse_image = page.locator(".product-container")

    #methodes

    def verify_title_page(self,title):
        expect(self.page).to_have_title(title)

    def click_on_quick_view_button(self):
        self.blouse_image.hover()
        self.page.wait_for_timeout(500)
        self.quick_view_button.click(force=True)
        time.sleep(2)




