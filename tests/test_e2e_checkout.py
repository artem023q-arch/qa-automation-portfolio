from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.checkout_complete_page import CheckoutCompletePage


def test_complete_purchase_flow(page: Page):
    login_page = LoginPage(page)
    Inventory_page = InventoryPage(page)
    checkout_page = CheckoutPage(page)
    complete_page = CheckoutCompletePage(page)

    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")

    expect(Inventory_page.page_title).to_have_text("Products")
    Inventory_page.add_backpack_to_cart()
    Inventory_page.go_to_cart()

    expect(page.locator(".title")).to_have_text("Your Cart")
    expect(page.locator(".inventory_item_name")).to_have_text("Sauce Labs Backpack")

    page.locator("#checkout").click()

    expect(page.locator(".title")).to_have_text("Checkout: Your Information")
    checkout_page.fill_checkout_info("John", "Doe", "12345")

    expect(page.locator(".title")).to_have_text("Checkout: Overview")
    checkout_page.finish_checkout()

    expect(page.locator(".title")).to_have_text("Checkout: Complete!")
    expect(complete_page.complete_header).to_have_text("Thank you for your order!")