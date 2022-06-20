from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(y)

    sumbit_btn = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    sumbit_btn.click()

finally:
    time.sleep(30)
    browser.quit()