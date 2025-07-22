from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    print(x_element)
    x = x_element.text
    print(x)
    y = calc(x)
    print(y)
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    option2 = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    option3 = browser.find_element(By.CSS_SELECTOR, '[type ="submit"]').click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
