from playwright.sync_api import Page

class CheckoutCompletePage:
    def __init__(self, page: Page):
        self.page = page
        self.complete_header = page.locator(".complete-header")
        self.back_home_button = page.locator("#back-to-products")
    