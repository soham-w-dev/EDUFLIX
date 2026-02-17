from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

def test_login():

    # Launch Browser
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()

    # Open EDUFLIX
    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    # Locate Elements
    username = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")

    # Enter Data
    username.send_keys("testuser")
    password.send_keys("123456")

    # Click Login
    login_btn.click()

    time.sleep(3)

    # Assertion (Very Important – as per PPT) :contentReference[oaicite:3]{index=3}
    assert "Home" in driver.page_source

    print("Login Test Passed ✅")

    driver.quit()
