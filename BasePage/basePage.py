import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from miscellaneous.LoggingDemo import logger


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, by_locator):
        logger.info(f"Waiting for element by locator: {by_locator}")
        return WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))

    def wait_for_elements(self, by_locator):
        logger.info(f"Waiting for elements by locator: {by_locator}")
        return WebDriverWait(self.driver, 50).until(EC.presence_of_all_elements_located(by_locator))

    def click_element(self, by_locator):
        logger.info(f"Clicking element by locator: {by_locator}")
        element = self.wait_for_element(by_locator)
        element.click()

    def enter_text(self, by_locator, text):
        logger.info(f"Entering text '{text}' in element by locator: {by_locator}")
        element = self.wait_for_element(by_locator)
        element.clear()
        element.send_keys(text)

    def scroll_to_end(self):
        logger.info("Scrolling to the end of the page")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    def assert_any(self, title):
        logger.info("Asserting for element")
        assert title in self.driver.title

    def navigate_back(self):
        logger.info("Navigating back")
        self.driver.back()
        print("Navigating back works")

    def get_action_chains(self):
        logger.info("Getting action chains")
        return ActionChains(self.driver)

    def get_attribute_value(self, by_locator, name):
        logger.info(f"Getting attribute '{name}' value from element by locator: {by_locator}")
        element = WebDriverWait(self.driver, 50).until(EC.visibility_of_element_located(by_locator))
        return element.get_attribute(name)

