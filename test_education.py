import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
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


def hover_education(driver):
    edu = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Education"))
    )
    ActionChains(driver).move_to_element(edu).perform()


# Submenu yang tetap di ultimateqa.com
EDU_INTERNAL = [
    ("Selenium Resources", "best-selenium-webdriver-resources"),
    ("Automation Exercises", "ultimateqa.com/automation"),
]

# Submenu yang pindah ke situs lain
EDU_EKSTERNAL = ["Free Courses", "Selenium Java", "Video courses", "Selenium C#"]


@pytest.mark.parametrize("menu,url", EDU_INTERNAL)
def test_education_internal(driver, menu, url):
    hover_education(driver)
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, menu))
    ).click()
    WebDriverWait(driver, 30).until(EC.url_contains(url))
    assert url in driver.current_url


@pytest.mark.parametrize("menu", EDU_EKSTERNAL)
def test_education_eksternal(driver, menu):
    hover_education(driver)
    link = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, menu))
    )
    assert link.get_attribute("href").startswith("http")

    link.click()
    WebDriverWait(driver, 30).until(lambda d: d.current_url != BASE)
    assert driver.title != ""