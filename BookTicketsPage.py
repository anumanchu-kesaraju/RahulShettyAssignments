class BookTicketsPage():
    def __init__(self,page):
        self.page=page
    def get_event_title(self):
        title= self.page.locator("h1")
        return title
    def get_event_price(self):
        return self.page.locator("//p[text()='Price per ticket']/following-sibling::p")