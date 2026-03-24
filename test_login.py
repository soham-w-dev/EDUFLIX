from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login():
    driver = webdriver.Edge()   # since you use Edge
    driver.maximize_window()

    # Your local Flask app URL
    driver.get("http://127.0.0.1:5000/login")

    # Locate fields (using NAME from your HTML)
    username = driver.find_element(By.NAME, "usernamelogin")
    password = driver.find_element(By.NAME, "passwordlogin")

    # Enter data
    username.send_keys("admin")
    password.send_keys("admin")

    # Submit form
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    # Assertion (VERY IMPORTANT)
    assert "Login" not in driver.page_source   # or check dashboard text

    driver.quit()