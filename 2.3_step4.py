from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
time.sleep(5)
alert = browser.switch_to.alert
alert.accept()
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
subm = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
print(browser.switch_to.alert.text)


time.sleep(10)
browser.quit()
