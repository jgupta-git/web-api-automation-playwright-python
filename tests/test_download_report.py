from src.pages.downloadReports import downloadReportPage
from src.pages.login import loginPage
from src.services.input import TestData


def test_download_report(shared_page):
    login_page = loginPage(shared_page)
    download_report_page = downloadReportPage(shared_page)

    # Login to HRM application using valid credentials
    login_page.navigate_to_login_page(shared_page)
    login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )

    # Navigate to the Reports page and view a specific report
    download_report_page.navigateToReports()
    download_report_page.viewReport()

    # Export the report as a PDF
    pdf = download_report_page.exportAsPDF()
    assert pdf
