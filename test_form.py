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

def test_isi_form(driver):
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Fill out forms"))
    ).click()

    nama = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "et_pb_contact_name_0"))
    )
    nama.send_keys("Praktikum Testing")

    pesan = driver.find_element(By.ID, "et_pb_contact_message_0")
    pesan.send_keys("Pengujian otomatisasi Selenium WebDriver.")

    assert nama.get_attribute("value") == "Praktikum Testing"
    assert pesan.get_attribute("value") == "Pengujian otomatisasi Selenium WebDriver."
