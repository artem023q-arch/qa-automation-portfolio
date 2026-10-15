from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page

        self.add_to_cart_backpack = page.locator("#add-to-cart-sauce-labs-backpack")

        self.cart_icon = page.locator(".shopping_cart_link")

        self.page_title = page.locator(".title")

    def add_backpack_to_cart(self):
        self.add_to_cart_backpack.click()

    def go_to_cart(self):
        self.cart_icon.click()