from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = '../chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
events_ul = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
events_li = events_ul.find_elements(By.TAG_NAME, 'li')
print()

events = {}

for index, event in enumerate(events_li):
    events[index] = {
        "time": event.find_element(By.TAG_NAME, 'time').text,
        "title": event.find_element(By.TAG_NAME, 'a').text
    }

print(events)

driver.quit()
