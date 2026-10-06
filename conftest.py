from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

def setup_driver():
    chrome_options = Options()
    
    if os.getenv("HEADLESS") == "1":
        chrome_options.add_argument("--headless")
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--single-process")  # Optional: use with caution
    
    driver = webdriver.Chrome(options=chrome_options)
    return driver