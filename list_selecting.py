from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


link = 'http://suninjuly.github.io/selects2.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    n1 = browser.find_element(By.XPATH, '//span[@id="num1"]').text
    n2 = browser.find_element(By.XPATH, '//span[@id="num2"]').text
    res = int(n1) + int(n2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(res))
    button = browser.find_element(By.XPATH, '//button')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()