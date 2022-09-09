from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

class TestAbs(unittest.TestCase):
    def test_reg1(self):
        try:
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
            first_name.send_keys('a')

            last_name = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
            last_name.send_keys('a')

            email = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
            email.send_keys('a')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'not equal 1?')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()

    def test_reg2(self):
        try:
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element(By.XPATH, '//input[@class="form-control first" and @required]')
            first_name.send_keys('a')

            last_name = browser.find_element(By.XPATH, '//input[@class="form-control second" and @required]')
            last_name.send_keys('a')

            email = browser.find_element(By.XPATH, '//input[@class="form-control third" and @required]')
            email.send_keys('a')
            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            time.sleep(1)

            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text, 'not equal 2?')

        finally:
            # ожидание чтобы визуально оценить результаты прохождения скрипта
            time.sleep(3)
            # закрываем браузер после всех манипуляций
            browser.quit()
if __name__ == "__main__":
    pytest.main()