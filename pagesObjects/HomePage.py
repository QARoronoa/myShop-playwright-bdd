from playwright.sync_api import Page, expect
import logging

class HomePage:

    def __init__(self, page: Page):
        self.page = page


    #locators
        self.signin_button = page.locator(".login")
        self.search_bar = page.locator('#search_query_top')
        self.search_button = page.locator("button[name='submit_search']")
        self.best_sellers_button = page.get_by_role('link', name="Best Sellers")
        self.more_button = page.locator("a[class='button lnk_view btn btn-default']")
        self.image_item = page.locator('.replace-2x')
        self.link_women_category = page.get_by_role("link", name="Women")
        self.link_Tops = page.get_by_role("link", name= "Tops")
        self.link_Tshirt = page.locator("ul.submenu-container li a", has_text="T-shirts")
        self.link_Blouses = page.locator("ul.submenu-container li a", has_text="Blouses")
        self.link_account = page.locator('.account')
        self.signout_button = page.locator('.logout')



    #methodes

    def click_on_signIn_button(self):
        expect(self.signin_button).to_be_visible()
        self.signin_button.click()

    def enter_item_in_search_bar(self, article):
        self.search_bar.fill(article)

    def click_on_search_button(self):
        expect(self.search_button).to_be_visible()
        self.search_button.click()

    def click_on_best_sellers_button(self):
        expect(self.best_sellers_button).to_be_visible()
        self.best_sellers_button.click()
        expect(self.image_item).to_have_count(6)

    def scroll_into_item(self,text):
        self.page.locator(f'a.product-name[title="{text}"]').scroll_into_view_if_needed()

    def click_on_more_button(self, item):
        self.page.locator(f"li.ajax_block_product:has-text('{item}') a.button:has-text('More')").click()
        expect(self.page).to_have_title(f"{item} - My Shop")

    def mouss_over_element(self, locator):
       locator.first.hover()

    def element_is_visible(self, locator):
        expect(locator).to_be_visible()

    def click_on_tshirt_link(self):
        self.link_Tshirt.click()

    def click_on_Blouses_link(self):
        self.link_Blouses.click()

    def click_on_accunt_link(self):
        expect(self.link_account).to_be_enabled()
        self.link_account.click()

    def click_on_signOut_button(self):
        expect(self.signout_button).to_be_enabled()
        self.signout_button.click()
