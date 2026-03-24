from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

def test_login():

    options = Options()

    # ✅ VERY IMPORTANT (FIX)
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

    driver.get("http://127.0.0.1:5000/login")

    time.sleep(2)

    username = driver.find_element(By.NAME, "usernamelogin")
    password = driver.find_element(By.NAME, "passwordlogin")

    username.send_keys("testuser")
    password.send_keys("1234")

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    # ✅ SUCCESS CHECK
    if "home" in driver.current_url.lower():
        print("✅ Login Successful")
        assert True
    else:
        print("❌ Login Failed")
        assert False

    driver.quit()