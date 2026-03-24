from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.maximize_window()

    # Your Flask app URL
    driver.get("http://127.0.0.1:5000/")   # change if needed

    wait = WebDriverWait(driver, 10)

    # Locate fields using NAME (important)
    username = wait.until(EC.presence_of_element_located((By.NAME, "usernamelogin")))
    password = driver.find_element(By.NAME, "passwordlogin")

    # Enter data
    username.send_keys("admin")      # your test username
    password.send_keys("admin")       # your test password

    # Click login button
    login_btn = driver.find_element(By.TAG_NAME, "button")
    login_btn.click()

    # Wait for redirect (since AJAX is used)
    wait.until(EC.url_changes("http://127.0.0.1:5000/"))

    # Assertion (VERY IMPORTANT)
    assert "dashboard" in driver.current_url.lower() or "home" in driver.current_url.lower()

    driver.quit()