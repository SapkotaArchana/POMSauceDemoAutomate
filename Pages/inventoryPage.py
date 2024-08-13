from selenium.webdriver.common.by import By
from BasePage.basePage import BasePage
from miscellaneous.LoggingDemo import logger


class InventoryPage(BasePage):
    product_sort_dropdown = (By.CLASS_NAME, "product_sort_container")
    product_titles = (By.CLASS_NAME, "inventory_item_name")
    add_to_cart_button = (By.XPATH, "//button[text()='Add to cart']")
    remove_button = (By.XPATH, "//button[text()='Remove']")
    cart_button = (By.ID, "shopping_cart_container")
    product_low_to_high = (By.XPATH, "//option[text()='Price (low to high)']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_product_names(self):
        return [element.text for element in self.wait_for_elements(self.product_titles)]

    def hover_over_element(self, index):
        product_titles_elements = self.wait_for_elements(self.product_titles)
        if index < len(product_titles_elements):
            logger.info("Hover succeed.")
            element = product_titles_elements[index]
            actions = self.get_action_chains()
            actions.move_to_element(element).perform()
        else:
            logger.info("Hover is not successful.")
            raise IndexError("Index out of range for product titles")

    def add_first_product_to_cart(self):
        self.click_element(self.add_to_cart_button)

    def is_remove_button_displayed(self):
        return self.wait_for_element(self.remove_button).is_displayed()

    def remove_first_product(self):
        return self.wait_for_element(self.remove_button)

    def go_to_cart(self):
        self.click_element(self.cart_button)

    def sort_products_low_to_high(self):
        self.click_element(self.product_low_to_high)

    def add_multiple_products_to_cart(self, number_of_products):
        add_buttons_locator = self.add_to_cart_button
        add_buttons = self.driver.find_elements(add_buttons_locator[0], add_buttons_locator[1])
        for i in range(min(number_of_products, len(add_buttons))):
            add_buttons[i].click()

    def remove_multiple_products_from_cart(self, indices):
        remove_buttons_elements = self.wait_for_elements(self.remove_button)
        for index in indices:
            if index < len(remove_buttons_elements):
                remove_buttons_elements[index].click()
            else:
                raise IndexError(f"Index {index} out of range for remove buttons")