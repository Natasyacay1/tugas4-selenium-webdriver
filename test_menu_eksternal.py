import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "https://ultimateqa.com/automation/"

EKSTERNAL = ["Projects", "Newsletter"]


@pytest.mark.parametrize("menu", EKSTERNAL)
def test_menu_eksternal(driver, menu):
    link = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, menu))
    )
    href = link.get_attribute("href")
    assert href.startswith("http")

    link.click()
    WebDriverWait(driver, 30).until(lambda d: d.current_url != BASE)
    assert driver.title != ""
