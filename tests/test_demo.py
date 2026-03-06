from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def test_demo():

    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Added for CI/CD environments
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    wait = WebDriverWait(driver, 10)

    # Open website
    driver.get("https://www.saucedemo.com/")

    # Login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Handle popup
    try:
        ok_button = WebDriverWait(driver, 3).until(
            EC.element_to_be_clickable((By.XPATH, "//button[.='OK']"))
        )
        ok_button.click()
    except Exception:
        print("No popup appeared")

    # Wait inventory page
    wait.until(EC.url_contains("inventory"))

    # Add product
    bike_light = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']//button")
        )
    )
    bike_light.click()

    # Cart
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

    # Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

    # Fill details
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("hussain")
    driver.find_element(By.ID, "last-name").send_keys("ahmad")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    # Finish
    wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

    print("Test completed successfully")
    print("Hussain")

    driver.quit()