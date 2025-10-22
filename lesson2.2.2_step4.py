from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import os
import time


link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    # Заполняем обязательные поля по уникальным селекторам
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']").send_keys("ivan.petrov@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # текущая директория
    file_path = os.path.join(current_dir, 'file.txt')

    # Создаём файл, если его нет
    with open(file_path, 'w') as file:
        file.write("")

    # Загружаем файл
    file_input = browser.find_element(By.CSS_SELECTOR, "#file")
    file_input.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
