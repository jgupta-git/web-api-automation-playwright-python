from pathlib import Path
from playwright.sync_api import Page, expect
from src.pages.login import loginPage
from src.pages.logout import logoutPage
from src.pages.employeeDashboard import employeeDashboard
from src.pages.createNewEmployee import createEmployeePage
from src.pages.searchEmployee import searchEmployeePage
from src.pages.uploadEmployeeImage import uploadEmployeeImagePage
from src.services.input import TestData


def test_create_employee(shared_page, employee_data):
    user_login_page = loginPage(shared_page)
    addEmployee = createEmployeePage(shared_page)

    # Perform login
    user_login_page.navigate_to_login_page(shared_page)
    user_login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )

    # navigate to employee transaction page
    addEmployee.navigateTomployeeCreation().click()

    addEmployee.fillEmployeeDetails(
        employee_data.first_name,
        employee_data.last_name,
        employee_data.username,
        employee_data.password,
    )
    addEmployee.saveEmployeeProfile()

    dashboard_page = employeeDashboard(shared_page)
    logout_page = logoutPage(shared_page)

    # Perform logout
    dashboard_page.ret_logout_dropdown().click()
    logout_page.click_logout().click()

    # Verify that the login page is visible after logout
    expect(user_login_page.ret_user_name()).to_be_visible()


def test_search_employee(shared_page, employee_data):
    search_page = searchEmployeePage(shared_page)
    user_login_page = loginPage(shared_page)

    # Perform login
    user_login_page.navigate_to_login_page(shared_page)
    user_login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )

    search_page.navigateToEmployeeRecord()
    search_page.fillEmployeeDetailsToSearch(employee_data.first_name)

    assert search_page.verifyEmployeeFound(
        employee_data.first_name, employee_data.last_name
    )
    dashboard_page = employeeDashboard(shared_page)
    logout_page = logoutPage(shared_page)

    # Perform logout
    dashboard_page.ret_logout_dropdown().click()
    logout_page.click_logout().click()


def test_upload_employee_image(shared_page, employee_data):
    search_employee = searchEmployeePage(shared_page)
    login_page = loginPage(shared_page)
    upload_employee_image = uploadEmployeeImagePage(shared_page)

    # Login to HRM application using valid credentials
    login_page.navigate_to_login_page(shared_page)
    login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )

    # Navigate to employee record and search for the employee
    search_employee.navigateToEmployeeRecord()
    search_employee.fillEmployeeDetailsToSearch(employee_data.first_name)

    shared_page.wait_for_timeout(10000)  # Wait for search results to load

    photo_path = str(Path.cwd() / "src" / "assets" / "av1.png")
    upload_employee_image.uploadEmployeeImage(photo_path)

    dashboard_page = employeeDashboard(shared_page)
    logout_page = logoutPage(shared_page)

    # Perform logout
    dashboard_page.ret_logout_dropdown().click()
    logout_page.click_logout().click()


def test_login_as_new_employee_check_uploaded_image(shared_page, employee_data):
    login_page = loginPage(shared_page)
    dashboard_page = employeeDashboard(shared_page)

    # Login as the new employee
    login_page.navigate_to_login_page(shared_page)
    login_page.user_login(shared_page, employee_data.username, employee_data.password)
    expect(shared_page.get_by_role("heading", name="Dashboard")).to_be_visible()

    # Check if the uploaded image is displayed on the employee dashboard
    assert dashboard_page.profile_image()
    assert dashboard_page.find_employee_name(
        employee_data.first_name, employee_data.last_name
    )
