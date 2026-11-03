import pytest
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import new_context

from conftest import get_data


@pytest.mark.smoke
def test_secondassignmentstep1(page):
    assert "EventHub" in page.title()
    expect(page.get_by_role("textbox",name="Email")).to_be_visible()
    expect(page.locator("#login-btn").filter(has_text="Sign In")).to_be_visible()

@pytest.mark.smoke
def test_secondassignmentstep2(page,browser):
    page.get_by_placeholder("you@email.com").fill("beginner@sample.com")
    expect( page.get_by_placeholder("you@email.com")).to_have_value("beginner@sample.com")
    print("first page",page.get_by_role("textbox", name="Email").input_value())
    context = browser.new_context()
    page1 = context.new_page()
    data= get_data(r"/Data/data.json")
    page1.goto(data["url"])
    expect(page1.get_by_text(" Sign in to EventHub")).to_be_visible()
    assert page1.get_by_role("textbox",name="Email").input_value() == ""
    page1.close()
