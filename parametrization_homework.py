import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math



@pytest.mark.parametrize('lesson_id', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_hint_should_be_correct(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)

    in_field = browser.find_element(By.XPATH, "//textarea")
    answer = math.log(int(time.time()))
    in_field.send_keys(answer)
    submit = browser.find_element(By.XPATH, '//button[@class="submit-submission"]')
    submit.click()
    hint = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]')
    assert hint.text == 'Correct!'



