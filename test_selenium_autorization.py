from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_selenium_auth():
    email = ""
    password = ""
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    driver = webdriver.Chrome(
        options=options
    )

    driver.get('https://passport.yandex.ru/auth/')
    time.sleep(2)

    email_input = driver.find_element(By.ID, "passp-field-login")
    email_input.clear()
    email_input.send_keys(email)

    driver.find_element(By.ID, "passp:sign-in").click()
    time.sleep(2)

    password_input = driver.find_element(By.ID, "passp-field-passwd")
    password_input.clear()
    password_input.send_keys(password)

    driver.find_element(By.ID, "passp:sign-in").click()
    time.sleep(2)

    if "пуш" in driver.find_element(By.CSS_SELECTOR, "h1").text:
        assert "пуш" in driver.find_element(By.CSS_SELECTOR, "h1").text

    elif "контрольный" in driver.find_element(By.CSS_SELECTOR, "h1").text:
        assert "контрольный" in driver.find_element(By.CSS_SELECTOR, "h1").text
    else:

        driver.find_element(By.CLASS_NAME, "UserID-Avatar").click()
        time.sleep(2)

        iframe = driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[1]/header/div/div[2]/div/div/iframe')
        driver.switch_to.frame(iframe)
        time.sleep(2)
        exit_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div/div[6]/a[2]')

        assert exit_button is not None

        exit_button.click()
        time.sleep(2)

    driver.close()
