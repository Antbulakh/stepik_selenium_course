from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

a_element = browser.find_element(By.CSS_SELECTOR, "#num1")
a = int(a_element.text)
print(a)
b_element = browser.find_element(By.CSS_SELECTOR, "#num2")
b = int(b_element.text)
print(b)
c = str(a + b)
print(c)
select = Select(browser.find_element(By.CSS_SELECTOR, "#dropdown"))
select.select_by_visible_text(c)
option = browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
