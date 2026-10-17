from playwright.sync_api import Page


class logoutPage:
    def __init__(self, page: Page):
        self.page = page
        self.logout_button = self.page.get_by_text("Logout")

    def click_logout(self):
        return self.logout_button
