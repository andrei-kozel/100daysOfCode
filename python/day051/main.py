from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

load_dotenv()

PROMISED_DOWN: int = 1000
PROMISED_UP: int = 1000
CHROME_DRIVER_PATH = "./chromedriver.exe"

service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self):
        self.promised_down = PROMISED_DOWN,
        self.promised_up = PROMISED_UP,
        self.driver = webdriver.Chrome(service=service)
        self.down_speed = 0
        self.up_speed = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/')
        try:
            privacy_window = self.driver.find_element(By.ID, "onetrust-consent-sdk")
            accept_button = privacy_window.find_element(By.ID, "onetrust-accept-btn-handler")
            accept_button.click()
        except:
            print("Privacy window was not found.")

        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(60)
        self.down_speed = self.driver.find_element(By.CLASS_NAME,
                                                   "download-speed")
        self.up_speed = self.driver.find_element(By.CLASS_NAME,
                                                 "upload-speed")
        print(f"{self.down_speed}down")
        print(f"{self.up_speed}up")


speed_bot = InternetSpeedTwitterBot()
speed_bot.get_internet_speed()
