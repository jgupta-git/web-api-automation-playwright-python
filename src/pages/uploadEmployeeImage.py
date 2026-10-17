import re

from playwright.sync_api import Page


class uploadEmployeeImagePage:
    def __init__(self, page: Page):
        self.page = page

    def uploadEmployeeImage(self, imagePath: str) -> bool:
        try:
            self.page.wait_for_load_state("networkidle")

            # Check if "Record Found" message appears
            record_found = (
                self.page.locator("div")
                .filter(has_text=re.compile(r"Record Found"))
                .first.is_visible()
            )

            if not record_found:
                print("❌ No record found message displayed")
                return False

            # Get edit icon to click on the employee record
            self.page.locator("div.oxd-table-cell-actions button:nth-child(1)").click()
            self.page.wait_for_load_state("networkidle")

            # Click on the profile picture to open the upload dialog
            self.page.get_by_role("img", name="profile picture").nth(1).click()

            # Upload the image
            self.page.locator(
                "button.oxd-icon-button.oxd-icon-button--solid-main.employee-image-action"
            ).click()
            self.page.get_by_role("button", name="Choose File").set_input_files(
                imagePath
            )

            # Click Save button
            self.page.get_by_role("button", name="Save").click()

            # Wait for upload to complete
            self.page.wait_for_load_state("networkidle")

            return True

        except Exception as error:
            print("❌ Error uploading employee image:", error)
            return False
