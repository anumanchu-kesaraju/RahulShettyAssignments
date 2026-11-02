
class EventHubLoginPage:
    def __init__(self,page,email,password):
        self.page = page
        self.email = email
        self.password = password
    def login(self):
        self.page.locator("#email").fill(self.email)
        self.page.get_by_role("textbox",name="Password").fill(self.password)
        self.page.locator("#login-btn").click()
        return self.page
