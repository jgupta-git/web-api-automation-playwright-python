from pathlib import Path

from playwright.sync_api import Page


class downloadReportPage:
    def __init__(self, page: Page):
        self.page = page

    # Navigate to Reports
    def navigateToReports(self):
        self.page.get_by_role("link", name="PIM").click()
        self.page.locator("text=Reports").click()
        self.page.wait_for_load_state("networkidle")

    # View the report
    def viewReport(self):
        self.page.locator("button:has(i.bi-file-text-fill)").first.click()
        self.page.wait_for_load_state("networkidle")

    # Export as PDF
    def exportAsPDF(self) -> bytes:
        # page.pdf() needs the folder to exist, so create it first
        Path("downloads").mkdir(exist_ok=True)
        pdf = self.page.pdf(path="downloads/report.pdf")
        return pdf
