import pytest
from playwright.sync_api import Page, expect


#The core library provides only the raw browser automation APIs,
# playwright / test (Playwright Test) is a comprehensive end-to-end testing framework that packages those APIs with a powerful, built- in test runner
@pytest.mark.smoke
def test_firstAssignment(page:Page):
    #EventHub login page
    page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.get_by_placeholder("you@email.com")).to_be_visible()
    expect(page.locator("#login-btn")).to_have_text("Sign In")
@pytest.mark.smoke
def test_firstassignmentstep2(page):
    # EventHub login page
    #for assignment 2 createda fixture to got page
    #page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.get_by_role("textbox", name="password")).to_be_visible()
    #Better to sure expect as it might take some time to load the page
    expect(page).to_have_url("https://eventhub.rahulshettyacademy.com/login")
    #assert "/login" in page.url


