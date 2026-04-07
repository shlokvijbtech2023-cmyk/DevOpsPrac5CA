from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

print("Starting script...")

try:
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print("Browser opened")

    driver.get("file:///Users/shlokvij/DevOpsCA2/index.html")
    print("Page opened")

    wait = WebDriverWait(driver, 20)

    # wait for name field directly
    name = wait.until(EC.presence_of_element_located((By.ID, "name")))
    print("Form ready")

    name.send_keys("Shlok Vij")

    driver.find_element(By.ID, "email").send_keys("test@gmail.com")
    driver.find_element(By.ID, "mobile").send_keys("9876543210")

    Select(driver.find_element(By.ID, "dept")).select_by_visible_text("CSE")
    driver.find_elements(By.NAME, "g")[0].click()

    driver.find_element(By.ID, "fb").send_keys(
        "Symbiosis Institute of Technology Nagpur provides amazing opportunities for all students to shine and grow. The faculty is very supportive and the environment encourages innovation and learning."
    )

    print("Form filled")

    driver.find_element(By.ID, "submit").click()
    print("Submit clicked")
    print("Test executed successfully")

    time.sleep(2)

except Exception as e:
    print("ERROR OCCURRED:", e)

finally:
    driver.quit()
