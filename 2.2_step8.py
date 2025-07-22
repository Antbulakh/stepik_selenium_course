from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
from faker import Faker

fake = Faker()

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element(By.NAME, "firstname").send_keys(fake.first_name())
input2 = browser.find_element(By.NAME, "lastname").send_keys(fake.last_name())
input3 = browser.find_element(By.NAME, "email").send_keys(fake.email())
current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file.txt"
file_path = os.path.join(current_dir, file_name)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)
subm = browser.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
time.sleep(10)

browser.quit()
