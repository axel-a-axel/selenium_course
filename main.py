from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//img')
    y = calc(x_element.get_attribute('valuex'))
    form = browser.find_element(By.XPATH, '//input[@id="answer"]')
    form.send_keys(y)
    checkbox = browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]')
    checkbox.click()
    radiob = browser.find_element(By.XPATH, '//input[@id="robotsRule"]')
    radiob.click()
    button = browser.find_element(By.XPATH, '//button')
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()