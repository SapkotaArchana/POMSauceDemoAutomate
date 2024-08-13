import time
import pytest
from selenium import webdriver
from Pages.loginPage import LoginPage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver  # Return the driver to the test function
    driver.quit()


@pytest.fixture()
def login_page(driver):
    # Initialize the LoginPage
    return LoginPage(driver)


def test_login_success(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    login_page.assert_any("Swag Labs")


def test_login_failure(login_page):
    login_page.enter_username("invalid_user")
    login_page.enter_password("wrong_password")
    login_page.click_login()
    assert login_page.error_displayed()


def test_empty_fields(login_page):
    login_page.click_login()
    assert login_page.error_displayed()
    time.sleep(2)


def test_login_blank_username(login_page):
    login_page.enter_username("")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    assert login_page.error_displayed()
    time.sleep(2)


def test_login_blank_password(login_page):
    login_page.enter_username("standard_user")
    login_page.enter_password("")
    login_page.click_login()
    assert login_page.error_displayed()
    time.sleep(2)


def test_username_placeholder(login_page):
    placeholder_text = login_page.get_username_placeholder()
    assert placeholder_text == "Username"
    time.sleep(2)


def test_password_placeholder(login_page):
    placeholder_text = login_page.get_password_placeholder()
    assert placeholder_text == "Password"
