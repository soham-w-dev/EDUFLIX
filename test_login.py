from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def test_login():
    # 🔥 Add headless mode (IMPORTANT for Jenkins)
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # ❌ Remove maximize (not needed in headless)
    # driver.maximize_window()

    # Your Flask app URL
    driver.get("http://127.0.0.1:5000/")

    wait = WebDriverWait(driver, 10)

    # Locate fields using NAME
    username = wait.until(EC.presence_of_element_located((By.NAME, "usernamelogin")))
    password = driver.find_element(By.NAME, "passwordlogin")

    # Enter data
    username.send_keys("admin")
    password.send_keys("admin")

    # Click login button
    driver.find_element(By.TAG_NAME, "button").click()

    # Wait for redirect (AJAX handling)
    wait.until(EC.url_changes("http://127.0.0.1:5000/"))

    # Assertion
    assert "dashboard" in driver.current_url.lower() or "home" in driver.current_url.lower()

    driver.quit()