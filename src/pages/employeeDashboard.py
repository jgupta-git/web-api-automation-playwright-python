from playwright.sync_api import Page
import re


class employeeDashboard:
    def __init__(self, page: Page):
        self.page = page
        self.dashboard_text = page.locator("div").filter(
            has_text=re.compile(r"^Dashboard$")
        )
        self.profile_picture = page.get_by_role("banner").get_by_role(
            "img", name="profile picture"
        )
        self.logout_dropdown = page.locator(".oxd-userdropdown-img")

    def ret_dashboard_profile_picture(self):
        return self.profile_picture

    def ret_dashboard_text(self):
        return self.dashboard_text

    def ret_logout_dropdown(self):
        return self.logout_dropdown

    # Verify the profile picture is displayed
    def profile_image(self) -> bool:
        self.page.wait_for_load_state("networkidle")
        return self.page.locator(
            'img.oxd-userdropdown-img[alt="profile picture"]'
        ).is_visible()

    # Verify the employee name is displayed
    def find_employee_name(self, first_name: str, last_name: str) -> bool:
        self.page.wait_for_load_state("networkidle")
        employee_name = self.page.locator(
            "p.oxd-userdropdown-name", has_text=f"{first_name} {last_name}"
        )
        return employee_name.is_visible()
