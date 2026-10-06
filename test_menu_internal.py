import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://ultimateqa.com/automation/"


@pytest.fixture
def driver():
    d = webdriver.Chrome()
    d.maximize_window()
    d.get(BASE)
    yield d
    d.quit()


INTERNAL = [
    ("Services", "ultimateqa.com/consulting"),
    ("Case Studies", "ultimateqa.com/case-studies"),
    ("Blog", "ultimateqa.com/blog"),
]


@pytest.mark.parametrize("menu,url", INTERNAL)
def test_menu_internal(driver, menu, url):
    link = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, menu))
    )
    link.click()
    WebDriverWait(driver, 15).until(EC.url_contains(url))
    assert url in driver.current_url