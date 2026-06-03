from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time

# Headless mode for Jenkins (no display needed)
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Edge(options=options)

driver.get("https://www.google.com")
title = driver.title
assert "Google" in title, f"Expected 'Google' in title but got: {title}"

search_box = driver.find_element(By.NAME, "q")
search_box.click()
search_box.send_keys("Selenium Python")

print("Attribute (name):", search_box.get_attribute("name"))
print("Is Enabled:", search_box.is_enabled())
print("Tag Name:", search_box.tag_name)

driver.save_screenshot("google_page.png")
time.sleep(2)

search_box.clear()
search_box.send_keys("Automation Testing")
search_box.submit()
time.sleep(3)

driver.quit()
print("Test Passed Successfully!")
