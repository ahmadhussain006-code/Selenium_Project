from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")

# Launch browser
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# 1️⃣ Open website
driver.get("https://www.saucedemo.com/")

# 2️⃣ Login
wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# 3️⃣ Handle popup if it appears
try:
    ok_button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.='OK']"))
    )
    ok_button.click()
except:
    print("No popup appeared")

# 4️⃣ Wait for inventory page
wait.until(EC.url_contains("inventory"))

# 5️⃣ Add Sauce Labs Bike Light to cart
bike_light = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item']//button")
    )
)
bike_light.click()

# 6️⃣ Click cart icon
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))).click()

# 7️⃣ Click Checkout
wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# 8️⃣ Fill checkout details
wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("hussain")
driver.find_element(By.ID, "last-name").send_keys("ahmad")
driver.find_element(By.ID, "postal-code").send_keys("123456")

# Click continue
driver.find_element(By.ID, "continue").click()

# 9️⃣ Click Finish
wait.until(EC.element_to_be_clickable((By.ID, "finish"))).click()

print("Test completed successfully")

# Close browser
driver.quit()