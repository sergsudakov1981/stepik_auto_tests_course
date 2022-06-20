from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'num1')
    y_element = browser.find_element(By.ID, 'num2')
    x = x_element.text
    y = y_element.text
    s = int(x) + int(y)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(s))

    sumbit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    sumbit_btn.click()

finally:
    time.sleep(30)
    browser.quit()