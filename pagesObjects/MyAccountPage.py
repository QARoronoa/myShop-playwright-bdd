from playwright.sync_api import Page, expect


class MyAccountPage:
    def __init__(self, page: Page):
        self.page = page

    #locators
        self.link_add_my_first_address = page.get_by_role('link', name='Add my first address')
        self.addresses1_field = page.locator('#address1')
        self.city_field = page.locator('#city')
        self.state_field = page.locator('#id_state')
        self.zipCode_field = page.locator('#postcode')
        self.country_field = page.locator('#id_country')
        self.homePhone_field = page.locator('#phone')
        self.mobilePhone_field = page.locator('#phone_mobile')
        self.addresses_reference = page.locator('#alias')
        self.save_button = page.locator('#submitAddress')

    #methodes

    def verify_title_page(self,title):
        expect(self.page).to_have_title(title)

    def click_on_add_my_first_address(self):
        expect(self.link_add_my_first_address).to_be_enabled()
        self.link_add_my_first_address.click()

    def fill_addresses_form_order(self, address, city, cp, homePhone, mobilePhone):
        self.addresses1_field.fill(address)
        self.city_field.fill(city)
        self.state_field.select_option(value="4")
        self.zipCode_field.clear()
        self.zipCode_field.fill(cp)
        self.homePhone_field.fill(homePhone)
        self.mobilePhone_field.fill(mobilePhone)
        self.addresses_reference.fill("myAddress")

    def click_on_save_button(self):
        expect(self.save_button).to_be_enabled()
        self.save_button.click()

