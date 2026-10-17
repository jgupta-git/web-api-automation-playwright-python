import random

import pytest

from src.services.input import EmployeeData, TestData


@pytest.fixture(scope="module")
def shared_page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture(scope="session")
def employee_data() -> EmployeeData:
    random_id = random.randrange(100000)
    TestData.initialize_employee_data(random_id)
    print(f"✓ Employee ID initialized: {random_id}")
    return TestData.EMPLOYEE_DATA
