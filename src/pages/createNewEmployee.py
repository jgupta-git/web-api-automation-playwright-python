from playwright.sync_api import Page


class createEmployeePage:
    def __init__(self, page: Page):
        self.page = page
        self.pimLink = page.get_by_role("link", name="PIM")
        self.addEmployeeLink = page.get_by_role("listitem").filter(
            has_text="Add Employee"
        )
        self.fnameLink = page.get_by_role("textbox", name="First Name")
        self.lnameLink = page.get_by_role("textbox", name="Last Name")
        self.idLink = page.get_by_role("textbox").nth(4)
        self.enableLink = page.locator(".oxd-switch-input")
        self.usernameLink = page.get_by_role("textbox").nth(5)
        self.firstPasswordLink = page.locator('input[type="password"]').first
        self.confirmPasswordLink = page.locator('input[type="password"]').nth(1)
        self.saveLink = page.get_by_role("button", name="Save")

    def navigateTomployeeCreation(self):
        return self.pimLink

    def fillEmployeeDetails(
        self, firstName: str, lastName: str, userName: str, password: str
    ):
        # click Add employee
        self.addEmployeeLink.click()
        # add first and last name
        self.fnameLink.fill(firstName)
        self.lnameLink.fill(lastName)
        # Enable Login Credentials
        self.enableLink.click()
        # Add use name and password. confirm password again
        self.usernameLink.fill(userName)
        self.firstPasswordLink.fill(password)
        self.confirmPasswordLink.fill(password)
        self.saveLink.click()
        self.page.wait_for_load_state("networkidle")

    def saveEmployeeProfile(self):
        self.page.get_by_role("button", name="Save").nth(1).click()
        self.page.wait_for_load_state("networkidle")
