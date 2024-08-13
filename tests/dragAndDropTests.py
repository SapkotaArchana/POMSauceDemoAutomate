import time
import pytest
from selenium import webdriver
from Pages.dragAndDropPage import DragAndDrop


@pytest.fixture()
def driver_load():
    driver_load = webdriver.Chrome()
    driver_load.maximize_window()
    yield driver_load
    driver_load.quit()


@pytest.fixture()
def some_page(driver_load):
    page = DragAndDrop(driver_load)
    return page


def test_drag_and_drop(some_page):
    some_page.drag_and_drop()
    time.sleep(2)
