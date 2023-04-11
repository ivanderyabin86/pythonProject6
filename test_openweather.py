import time

from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def test_open_page():
    driver.get('https://openweathermap.org/')
    driver.maximize_window()
    assert 'openweathermap' in driver.current_url
    print(driver.current_url)

# def test_check_page_title():
#     assert driver.title == 'Current weather and forecast - OpenWeatherMap'
#
# def test_fill_search_city_field():
#     search_city_field = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search city']")
#     search_city_field.send_keys('New York')
#     time.sleep(55)

