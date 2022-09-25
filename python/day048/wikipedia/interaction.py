from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '../chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
articles_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a").text

print(articles_count)
