import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    """Fixture global untuk Selenium WebDriver."""
    options = Options()
    
    # Mode headless untuk CI/CD
    if os.getenv("HEADLESS") == "1":
        options.add_argument("--headless=new")
    
    # Flag wajib untuk lingkungan Linux / CI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    # Jika Anda menggunakan Selenium Grid, logika GRID_URL tetap bisa dipakai di sini
    grid_url = os.getenv("GRID_URL")
    if grid_url:
        d = webdriver.Remote(command_executor=grid_url, options=options)
    else:
        d = webdriver.Chrome(options=options)

    # Membuka BASE URL langsung dari fixture jika repository Anda menggunakan variabel BASE
    base_url = os.getenv("BASE_URL", "https://example.com") # Sesuaikan dengan URL bawaan repo Anda
    d.get(base_url)
    
    yield d
    d.quit()