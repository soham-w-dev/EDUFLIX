from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

def test_login():

    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service("chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=options)

    driver.get("http://127.0.0.1:5000/")

    time.sleep(2)

    driver.find_element(By.NAME, "usernamelogin").send_keys("admin")
    driver.find_element(By.NAME, "passwordlogin").send_keys("admin")
    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(3)

    if "search" in driver.current_url.lower():
        print("Login Successful")
        assert True
    else:
        print("Login Failed")
        assert False

    driver.quit()