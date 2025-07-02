import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("pytest selenium github actions")
    search_box.send_keys(Keys.RETURN)
    assert "lang" in browser.page_source.lower()
