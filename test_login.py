from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

def test_login():

    # Edge setup
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Edge(options=options)

    # Your local Flask app URL
    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    # Locate fields (based on your HTML)
    username = driver.find_element(By.NAME, "usernamelogin")
    password = driver.find_element(By.NAME, "passwordlogin")

    # Enter credentials
    username.send_keys("admin")
    password.send_keys("admin")

    # Click login button
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    # ✅ Check success (IMPORTANT)
    if "home" in driver.current_url.lower():
        print("✅ Login Successful")
        assert True
    else:
        print("❌ Login Failed")
        assert False

    driver.quit()