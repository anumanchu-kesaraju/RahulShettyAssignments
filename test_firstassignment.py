from playwright.sync_api import Page, expect


#The core library provides only the raw browser automation APIs,
# playwright / test (Playwright Test) is a comprehensive end-to-end testing framework that packages those APIs with a powerful, built- in test runner
def test_firstAssignment(page:Page):
    #EventHub login page
    page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.get_by_placeholder("you@email.com")).to_be_visible()
    expect(page.locator("#login-btn")).to_have_text("Sign In")


