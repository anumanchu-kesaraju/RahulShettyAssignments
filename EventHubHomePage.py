from playwright.sync_api import Page


class EventHubHomePage():
    def __init__(self,page):
        self.page= page

    def get_by_text(self):
        self.page.locator("span").filter(has_text="Browse Events").click()
