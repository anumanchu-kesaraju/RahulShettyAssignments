import re

from playwright.sync_api import expect


from BaseClass import BaseClass
from BookTicketsPage import BookTicketsPage
from EventHubHomePage import EventHubHomePage
from EventHubLoginPage import EventHubLoginPage
from EventsPage import EventsPage
from conftest import get_data



def test_Assignments3(page):
    data= get_data("Data\\logindata.json")
    lp = EventHubLoginPage(page, data["email"], data["password"])
    lp.login()
    hp = EventHubHomePage(page)
    hp.get_by_text()
    expect(page.get_by_text("Find your next unforgettable experience")).to_be_visible()
    expect(page).to_have_url(re.compile(r".*/events"))
    #expect(page).to_have_url(lambda url: "/events/" in url)
    event_details = BaseClass.load_textfile("Data\\eventdetails.txt")
    title= event_details[0]
    price= event_details[1]
    seats= event_details[2]
    ep=EventsPage(page)
    events=ep.get_event_details()
    event= events.filter(has_text=title)
    expect(event).to_have_count(1)
    in_text = event.inner_text()
    event_details_test=BaseClass.inner_text_tolist(in_text)
    assert title in event_details_test
    assert price in event_details_test
    assert seats in event_details_test
    for line in event_details_test:
        if "seats" in line:
            no_of_seats=line.split(" ")[0]
    assert int(no_of_seats)>0
    ep.book_event(event)
    expect(page).to_have_url(re.compile(r".*/events/"))
    bt= BookTicketsPage(page)
    book_tickets_title =bt.get_event_title()
    assert book_tickets_title.text_content() == title
    book_tickets_price = bt.get_event_price()
    assert book_tickets_price.text_content() == price
    page.go_back()
    expect(page).to_have_url(re.compile(".*/events"))
    expect(ep.clear()).to_be_hidden()
    expect(events).to_have_count(3)
    event_headers=ep.event_headers()
    list_event_headers= event_headers.all_inner_texts()
    assert "" not in list_event_headers
    assert list_event_headers[0] != list_event_headers[2]
    print(list_event_headers)



