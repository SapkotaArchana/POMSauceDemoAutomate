import time

from miscellaneous.LoggingDemo import logger


def test_inventory_page_loaded(inventory_page):
    logger.info("Test: inventory_page_loaded")
    product_names = inventory_page.get_product_names()
    assert len(product_names) > 0  # Ensuring that product names are loaded
    logger.info("Inventory page loaded successfully with products")


def test_hover_over_product(inventory_page):
    logger.debug("Test: hover_over_product")
    inventory_page.hover_over_element(3)
    time.sleep(2)
    logger.debug("Hovered over product successfully")


def test_navigate_back(inventory_page):
    inventory_page.navigate_back()
    time.sleep(10)


def test_add_first_product_to_cart(inventory_page):
    inventory_page.add_first_product_to_cart()
    assert inventory_page.is_remove_button_displayed()


def test_go_to_cart(inventory_page):
    logger.critical("Test: Go_to_Cart page")
    inventory_page.go_to_cart()
    time.sleep(2)
    logger.critical("Test: Go_to_Cart page seen successfully")


def test_remove_first_product(inventory_page):
    inventory_page.add_first_product_to_cart()
    time.sleep(3)
    inventory_page.remove_first_product()
    time.sleep(1)


def test_sort_products_low_to_high(inventory_page):
    inventory_page.sort_products_low_to_high()
    time.sleep(3)


def test_add_multiple_products_to_cart(inventory_page):
    inventory_page.add_multiple_products_to_cart(3)  # Change the number to add as many as needed
    time.sleep(2)


def test_remove_multiple_products(inventory_page):
    indices = [0, 1, 2]
    inventory_page.add_multiple_products_to_cart(3)
    time.sleep(2)
    inventory_page.remove_multiple_products_from_cart(indices)
    time.sleep(2)




