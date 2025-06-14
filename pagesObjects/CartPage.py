from playwright.sync_api import Page, expect


class CartPage:
    def __init__(self, page: Page):
        self.page = page



    #locators
        self.shopping_cart_title = page.locator('#cart_title')
        self.page_title = page.locator('h1.page-heading')
        self.product_name = page.locator('.cart_description p')
        self.delete_button = page.locator('.icon-trash')
        self.alert_message_car_empty = page.locator('p.alert-warning')
        self.proceed_to_checkout_link = page.get_by_role('link', name='Proceed to checkout')
        self.proceed_to_checkout_button = page.get_by_role('button', name='Proceed to checkout')
        self.address_step3 = page.locator('li.third')
        self.terms_of_service_button = page.get_by_role("checkbox", name="I agree to the terms of service and will adhere to them unconditionally.")



    #methodes
    def verify_shopping_cart_summuary_is_visble(self):
        expect(self.shopping_cart_title).to_contain_text("Shopping-cart summary")

    def verify_page_title_is_visible(self, title):
        expect(self.page_title).to_contain_text(title)

    def verify_item_is_visible(self, name):
        expect(self.product_name).to_have_text(name)

    def click_on_delete_button(self):
        expect(self.delete_button).to_be_visible()
        self.delete_button.click()

    def verify_message_empty_card_is_visible(self):
        expect(self.alert_message_car_empty).to_have_text("Your shopping cart is empty.")

    def click_proceed_to_checkout_link(self):
        expect(self.proceed_to_checkout_link).to_be_visible()
        self.proceed_to_checkout_link.click()

    def click_proceed_to_checkout_button(self):
        expect(self.proceed_to_checkout_button).to_be_visible()
        self.proceed_to_checkout_button.click()

    def verify_step(self, step_title):
        expect(self.address_step3).to_contain_text(step_title)

    def click_on_radio_button_terms_of_service(self):
        expect(self.terms_of_service_button).not_to_be_checked()
        self.terms_of_service_button.check()
        expect(self.terms_of_service_button).to_be_checked()







