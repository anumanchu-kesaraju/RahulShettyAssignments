import json
from getopt import getopt

import pytest
from playwright.sync_api import Playwright


def get_data(path):
    with open(path) as f:
        data= json.load(f)
        return data

@pytest.fixture(scope="module")
def page(playwright:Playwright):

    data = get_data("Data/data.json")

    if data["browser_name"] == "chromium":
        browser= playwright.chromium.launch(headless=False)
    elif data["browser_name"] == "firefox":
        browser= playwright.firefox.launch(headless=False)
    page=browser.new_page()
    page.goto(data["url"])
    yield page
    browser.close()




