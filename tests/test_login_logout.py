from playwright.sync_api import Page, expect
from src.pages.login import loginPage
from src.pages.logout import logoutPage
from src.pages.employeeDashboard import employeeDashboard
from src.services.input import TestData


def test_login(shared_page):
    user_login_page = loginPage(shared_page)
    dashboard_page = employeeDashboard(shared_page)

    # Perform login
    user_login_page.navigate_to_login_page(shared_page)
    user_login_page.user_login(
        shared_page, TestData.VALID_USER.username, TestData.VALID_USER.password
    )

    # Verify that the dashboard is visible after login
    expect(dashboard_page.ret_dashboard_text()).to_be_visible()
    expect(dashboard_page.ret_dashboard_profile_picture()).to_be_visible()


def test_logout(shared_page):
    user_login_page = loginPage(shared_page)
    dashboard_page = employeeDashboard(shared_page)
    logout_page = logoutPage(shared_page)

    # Perform logout
    dashboard_page.ret_logout_dropdown().click()
    logout_page.click_logout().click()

    # Verify that the login page is visible after logout
    expect(user_login_page.ret_user_name()).to_be_visible()
