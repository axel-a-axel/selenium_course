from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.XPATH, '//span[@id="input_value"]')
    y = calc(x_element.text)
    button = browser.find_element(By.XPATH, '//button')
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.execute_script("window.scrollBy(0, 100);")

    form = browser.find_element(By.XPATH, '//input[@id="answer"]')
    form.send_keys(y)
    checkbox = browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]')
    checkbox.click()
    radiob = browser.find_element(By.XPATH, '//label[@for="robotsRule"]')
    radiob.click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()