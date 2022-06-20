# import time
#
# # webdriver это и есть набор команд для управления браузером
# from selenium import webdriver
#
# # импортируем класс By, который позволяет выбрать способ поиска элемента
# from selenium.webdriver.common.by import By
#
# # инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
# driver = webdriver.Chrome()
#
# # команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
# time.sleep(5)
#
# # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)
#
# # Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# # Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# # Ищем поле для ввода текста
# textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
#
# # Напишем текст ответа в найденное поле
# textarea.send_keys("get()")
# time.sleep(5)
#
# # Найдем кнопку, которая отправляет введенное решение
# submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
#
# # Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
# submit_button.click()
# time.sleep(5)
#
# # После выполнения всех действий мы должны не забыть закрыть окно браузера
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
# browser = webdriver.Chrome()
# browser.get(link)
# button = browser.find_element(By.ID, "submit_button")
# button.click()
#
# # закрываем браузер после всех манипуляций
# browser.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "http://suninjuly.github.io/cats.html"
# browser.get(link)
# browser.find_element(By.ID, "button")
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
# говорим WebDriver ждать все элементы в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait2.html")

button = browser.find_element(By.ID, "verify")
button.click()
message = browser.find_element(By.ID, "verify_message")

assert "successful" in message.text