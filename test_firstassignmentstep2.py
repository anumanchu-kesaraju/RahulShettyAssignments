from playwright.async_api import Page
from playwright.sync_api import expect


def test_firstassignmentstep2(page):
    # EventHub login page

    #for assignment 2 createda fixture to got page
    #page.goto("https://eventhub.rahulshettyacademy.com")
    expect(page.get_by_role("textbox", name="password")).to_be_visible()
    assert "/login" in page.url
