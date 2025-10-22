from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 =int(browser.find_element(By.ID, "num2").text)
    num_sum = num1 + num2

    select_element = browser.find_element(By.ID, "dropdown")
    select = Select(select_element)
    select.select_by_value(str(num_sum))

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
