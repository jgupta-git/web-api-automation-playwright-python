import pytest
import random
from playwright.sync_api import expect

from src.pages.login import loginPage
from src.services.employee_api import EmployeeApi
from src.services.input import TestData


@pytest.fixture(scope="module")
def employee_api(shared_page):
    # Log in once through the UI; the browser cookie authenticates the API calls
    login_page = loginPage(shared_page)
    login_page.navigate_to_login_page(shared_page)
    login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible()

    return EmployeeApi(shared_page.request)


def test_create_employee_via_api(employee_api, employee_data):
    first_name = f"Api{employee_data.id}"
    employee_id = f"{random.randrange(10**9):09d}"
    employee = employee_api.create_employee(
        first_name, employee_data.last_name, employee_id
    )

    assert employee["empNumber"]
    assert employee["firstName"] == first_name
    assert employee["lastName"] == employee_data.last_name
    assert employee["employeeId"] == employee_id
