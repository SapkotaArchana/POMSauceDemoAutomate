from selenium.webdriver.common.by import By
from BasePage.basePage import BasePage


class DragAndDrop(BasePage):
    source_element_locator = (By.XPATH, "//div[@id='column-a']")
    target_element_locator = (By.XPATH, "//div[@id='column-b']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    def drag_and_drop(self):
        source_element = self.wait_for_element(self.source_element_locator)
        target_element = self.wait_for_element(self.target_element_locator)
        actions = self.get_action_chains()
        actions.drag_and_drop(source_element, target_element).perform()
