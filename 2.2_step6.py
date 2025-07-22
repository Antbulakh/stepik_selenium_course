from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
print(y)
input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
Cbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
browser.execute_script("window.scrollBy(0, 150);")
rbutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
Subm = browser.find_element(By.TAG_NAME, "button").click()


time.sleep(10)
browser.quit()
