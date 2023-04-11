import time

from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# browser.get('https://suninjuly.github.io/xpath_examples')
# # def test_open():
# #     browser.get('https://suninjuly.github.io/xpath_examples')
# # time.sleep(5)

def open_page():
    browser.get('http://suninjuly.github.io/cats.html')

    bullet_cat = browser.find_element(By.XPATH, "//*[contains(text(), 'Bullet cat')]")
    print(bullet_cat)

    view_buttons = browser.find_elements(By.XPATH, "//*[contains(text(), 'View')]")
    print(view_buttons)
    assert len(view_buttons) == 6, 'wrong length'

def test_open_page():
    open_page()