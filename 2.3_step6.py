from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)
button = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
x = x_element.text
y = calc(x)
input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
subm = browser.find_element(By.CSS_SELECTOR, '[type = "submit"]').click()
print(browser.switch_to.alert.text)


time.sleep(2)
browser.quit()
