from playwright.sync_api import Page, expect

def test_successful_login(page: Page):
    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("standart_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click

    expect(page.locator(".title")).to_have_text("Products")


def test_login_locked_out_user(page: Page):

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sause")

    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_test("Sorry, this user has been locked out")