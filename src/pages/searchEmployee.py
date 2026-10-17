import re

from playwright.sync_api import Page


class searchEmployeePage:
    def __init__(self, page: Page):
        self.page = page

    def navigateToEmployeeRecord(self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.wait_for_load_state()

    def fillEmployeeDetailsToSearch(self, firstName: str):
        # First Name to search
        self.page.get_by_role("textbox", name="Type for hints...").first.fill(firstName)
        # Click on Search button
        self.page.get_by_role("button", name="Search").click()

    def verifyEmployeeFound(self, firstName: str, lastName: str) -> bool:
        try:
            self.page.wait_for_load_state("networkidle")

            # Wait up to 15 seconds for the "Record Found" message
            self.page.locator("div").filter(
                has_text=re.compile(r"Records? Found")
            ).first.wait_for(timeout=15000)

            # Get firstName from 3rd column
            table_first_name = self.page.locator(
                "div.oxd-table-body > div > div > div:nth-child(3) > div"
            ).text_content()

            # Get lastName from 4th column
            table_last_name = self.page.locator(
                "div.oxd-table-body > div > div > div:nth-child(4) > div"
            ).text_content()

            # Compare with expected values
            if (table_first_name or "").strip() == firstName and (
                table_last_name or ""
            ).strip() == lastName:
                print(f"✓ Employee found: {firstName} {lastName}")
                return True
            else:
                print(
                    f"❌ Expected: {firstName} {lastName}, "
                    f"Found: {table_first_name} {table_last_name}"
                )
                return False
        except Exception as error:
            print("❌ Error verifying employee:", error)
            return False
