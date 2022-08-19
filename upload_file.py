from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os


link = 'http://suninjuly.github.io/file_input.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    field1 = browser.find_element(By.XPATH, '//input[@name="firstname"]')
    field1.send_keys('a')
    field2 = browser.find_element(By.XPATH, '//input[@name="lastname"]')
    field2.send_keys('b')
    field3 = browser.find_element(By.XPATH, '//input[@name="email"]')
    field3.send_keys('c')
    field4 = browser.find_element(By.XPATH, '//input[@name="file"]')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    field4.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()