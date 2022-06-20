from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    robotCheckbox = browser.find_element(By.ID, 'robotCheckbox')
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, 'robotsRule')
    robotsRule.click()

    sumbit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    sumbit_btn.click()

finally:
    time.sleep(30)
    browser.quit()