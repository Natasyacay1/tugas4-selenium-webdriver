import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE = "https://ultimateqa.com/automation/"

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--window-size=1366,768")

    # Opsi khusus server CI (GitHub Actions)
    if os.getenv("HEADLESS"):
        opts.add_argument("--headless=new")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-gpu")

    grid_url = os.getenv("GRID_URL")
    if grid_url:
        d = webdriver.Remote(command_executor=grid_url, options=opts)
    else:
        d = webdriver.Chrome(options=opts)

    d.get(BASE)
    yield d
    d.quit()
