from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
import time

def test_login():

    options = Options()

    # ✅ MUST for Jenkins
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")

    # ✅ IMPORTANT (fix crash)
    options.add_argument("--user-data-dir=C:/temp/edge-profile")

    service = Service("msedgedriver.exe")

    driver = webdriver.Edge(service=service, options=options)

    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    username = driver.find_element(By.NAME, "usernamelogin")
    password = driver.find_element(By.NAME, "passwordlogin")

    username.send_keys("admin")
    password.send_keys("admin")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    if "home" in driver.current_url.lower():
        print("✅ Login Successful")
        assert True
    else:
        print("❌ Login Failed")
        assert False

    driver.quit()