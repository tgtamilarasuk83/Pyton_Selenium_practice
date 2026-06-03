from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Edge()

driver.get("https://www.google.com")
driver.maximize_window()
title = driver.title
assert "Google" in title


search_box = driver.find_element(By.NAME, "q")
# search_box = driver.find_element(By.XPATH())
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