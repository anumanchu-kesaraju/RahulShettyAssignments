

class EventsPage():
    def __init__(self,page):
        self.page = page
    def search_event(self, title, category, city):
        self.page.get_by_placeholder("Search events, venues…").fill(title)
        self.page.locator("select").nth(0).select_option(category)
        self.page.locator("select").nth(1).select_option(city)
    def clear(self):
        clear_filter =self.page.get_by_role("button", name="Clear filters")
        return clear_filter
    def get_event_details(self):
        events =self.page.locator("#event-card")
        return events
    def event_headers(self):
        event_headers =self.page.locator("#event-card h3")
        return event_headers

    def book_event(self,event):
        event.get_by_role("link", name="Book Now").click()