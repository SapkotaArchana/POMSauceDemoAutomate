import csv
import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


class DataReader:
    @staticmethod
    def read_data_from_csv(file_name):
        dir_path = Path(__file__).parent  # Directory of the current script
        path = dir_path / file_name
        print(f"Trying to open file: {path}")
        with open(path, mode='r') as file:
            reader = csv.DictReader(file)
            data = [row for row in reader]
        return data


class LoginTest:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def test_login_with_csv_data(csv_file):
        data_reader = DataReader()
        data_reader.read_data_from_csv(csv_file)


@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    time.sleep(3)
    driver.quit()


def test_login_with_csv_data(driver):
    csv_file = "swag_labs_test_data.csv"
    LoginTest.test_login_with_csv_data(csv_file)
