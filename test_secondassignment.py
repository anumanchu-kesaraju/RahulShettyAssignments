from playwright.sync_api import expect


def test_secondassignmentstep1(page):
    assert "EventHub" in page.title()
    expect(page.get_by_role("textbox",name="Email")).to_be_visible()
    expect(page.locator("#login-btn").filter(has_text="Sign In")).to_be_visible()
def test_secondassignmentstep2(page):
    page.get_by_placeholder("you@email.com").fill("beginner@sample.com")
    expect( page.get_by_placeholder("you@email.com")).to_have_value("beginner@sgit ample.com")