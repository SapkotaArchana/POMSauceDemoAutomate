import sys
import os
import time
import pytest
from selenium import webdriver
from Pages.loginPage import LoginPage
from Pages.inventoryPage import InventoryPage

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def inventory_page(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("standard_user")
    login_page.enter_password("secret_sauce")
    login_page.click_login()
    inventory_page = InventoryPage(driver)
    yield inventory_page
