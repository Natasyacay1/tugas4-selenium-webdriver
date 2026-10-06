import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE = "https://ultimateqa.com/automation/"

@pytest.fixture
def driver():
    opts = Options()
    opts.add_argument("--window-size=1366,768")
    if os.getenv("HEADLESS"):
        opts.add_argument("--headless=new")

    grid_url = os.getenv("GRID_URL")
    if grid_url:
        d = webdriver.Remote(command_executor=grid_url, options=opts)
    else:
        d = webdriver.Chrome(options=opts)

    d.get(BASE)
    yield d
    d.quit()