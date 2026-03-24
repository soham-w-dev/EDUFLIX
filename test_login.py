from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options

def test_login():
    options = Options()

    # 🔥 Edge binary path (VERY IMPORTANT)
    options.binary_location = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"

    # Headless mode
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    service = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=options)

    driver.get("http://127.0.0.1:5000/")

    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.presence_of_element_located((By.NAME, "usernamelogin")))
    password = driver.find_element(By.NAME, "passwordlogin")

    username.send_keys("admin")
    password.send_keys("admin")

    driver.find_element(By.TAG_NAME, "button").click()

    wait.until(EC.url_changes("http://127.0.0.1:5000/"))

    assert "dashboard" in driver.current_url.lower() or "home" in driver.current_url.lower()

    driver.quit()