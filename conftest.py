import json
from getopt import getopt

import pytest
from playwright.sync_api import Playwright


def get_data():
    with open("data.json") as f:
        data= json.load(f)
        return data

@pytest.fixture(scope="session")
def page(playwright:Playwright):

    data = get_data()

    if data["browser_name"] == "chromium":
        browser= playwright.chromium.launch(headless=False)
    elif data["browser_name"] == "firefox":
        browser= playwright.firefox.launch(headless=False)

    page=browser.new_page()
    page.goto(data["url"])
    yield page
    browser.close()




