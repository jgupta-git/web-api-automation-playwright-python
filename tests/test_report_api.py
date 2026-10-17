import pytest
from playwright.sync_api import expect

from src.pages.login import loginPage
from src.services.input import TestData
from src.services.report_api import ReportApi

REPORT_ID = 5


@pytest.fixture(scope="module")
def report_api(shared_page):
    # Log in once through the UI; the browser cookie authenticates the API calls
    login_page = loginPage(shared_page)
    login_page.navigate_to_login_page(shared_page)
    login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible()

    return ReportApi(shared_page.request)


def test_defined_report_details(report_api):
    report = report_api.get_defined_report(REPORT_ID)
    assert report["name"]  # Report name is not empty


def test_generate_report_data(report_api):
    rows = report_api.get_report_data(REPORT_ID)
    assert len(rows) > 0, "Report returned no rows"
    assert all("empNumber" in row for row in rows)
