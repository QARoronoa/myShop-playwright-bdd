from playwright.sync_api import Page, expect


class ItemDetailPage:
    def __init__(self, page: Page):
        self.page = page



    #locators
        self.item_title = page.locator("h1")
        self.white_color = page.locator('#color_8')
        self.text_item_not_in_stock = page.locator('#availability_value')
        self.addToCart_button = page.get_by_role('button', name="Add to cart")
        self.button_proceesToCheckout_popin = page.locator('a.button-medium')
        self.frame_locator = page.locator('#fancybox-frame1749069329376')

    #methodes
    def verify_redirection_to_item_detail_page(self, title):
        expect(self.item_title).to_have_text(title)

    def click_on_white_color(self):
        self.white_color.click()
        expect(self.text_item_not_in_stock).not_to_contain_text("This product is no longer in stock")

    def verify_button_add_to_cart_is_visible(self):
        expect(self.addToCart_button).to_be_visible()
        expect(self.addToCart_button).to_be_enabled()

    def click_on_add_to_cart(self):
        self.addToCart_button.click()

    def verify_item_is_in_cart(self):
        expect(self.page.locator('span.ajax_cart_product_txt', has_text="There is 1 item in your cart.")).to_be_visible()

    def click_on_proceed_to_checkout(self):
        expect(self.button_proceesToCheckout_popin).to_be_visible()
        self.button_proceesToCheckout_popin.click()

    def click_add_to_cart_in_frame(self):
        self.frame_locator = self.page.frame_locator('iframe.fancybox-iframe')
        self.white_color = self.frame_locator.locator('#color_8')
        self.addToCart_button = self.frame_locator.get_by_role('button', name="Add to cart")

        self.white_color.click()
        expect(self.addToCart_button).to_be_visible()
        expect(self.addToCart_button).to_be_enabled()
        self.addToCart_button.click()
        expect(self.button_proceesToCheckout_popin).to_be_enabled()
        self.button_proceesToCheckout_popin.click()
