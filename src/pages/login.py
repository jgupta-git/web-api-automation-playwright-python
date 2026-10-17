from playwright.sync_api import Page


class loginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.get_by_role("textbox", name="Username")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")

    def navigate_to_login_page(self, page: Page) -> None:
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def user_login(self, page: Page, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def ret_user_name(self):
        return self.username_input
