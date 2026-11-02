from playwright.sync_api import expect

from EventHubHomePage import EventHubHomePage
from EventHubLoginPage import EventHubLoginPage
from conftest import get_data


def test_Assignments3(page):
    data= get_data(r"C:\Users\Siri\PycharmProjects\PythonProject\RahulShettyAssignments\logindata.json")
    lp = EventHubLoginPage(page, data["email"], data["password"])
    lp.login()
    hp = EventHubHomePage(page)
    hp.get_by_text()
    expect(page.get_by_text("Find your next unforgettable experience")).to_be_visible()
    assert page.url == "https://eventhub.rahulshettyacademy.com/events"
    title = "World Tech Summit"
    event=page.locator("#event-card").filter(has_text=title)
    expect(event).to_have_count(1)
    print(event.inner_text())
    in_text = event.inner_text().split("\n")
    price =""
    seats =[]
    for text in in_text:
        if "$" in text:
            price = text

        if "seats left!" in text:
            seats=text.split(" ")

    assert price[1:] =="1,500"
    assert int(seats[0]) >0
    event.get_by_role("link",name= "Book Now").click()
    expect(page.locator("h1")).to_have_text(title)
    #expect(page.locator("span").filter().get_by_text(price)).to_have_text(price)
    expect(page.locator("//p[text()='Price per ticket']/following-sibling::p")).to_have_text(price)
    #assert "/events/" in page.url
    page.go_back()
    page.get_by_placeholder("Search events, venues…").clear()
    expect(page.locator("#event-card")).to_have_count(3)
    list_headers= page.locator("#event-card h3").all_inner_texts()
    assert "" not in list_headers
    assert list_headers[0] !=list_headers[2]
    print(list_headers)



