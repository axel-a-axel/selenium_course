from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element(By.XPATH, '//button[@id="book"]')
    label = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), '$100'))
    button.click()
    x_element = browser.find_element(By.XPATH, '//label/span[2]')
    y = calc(x_element.text)
    form = browser.find_element(By.XPATH, '//input[@id="answer"]')
    form.send_keys(y)
    button2 = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button2.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(6)
    # закрываем браузер после всех манипуляций
    browser.quit()