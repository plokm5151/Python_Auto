from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

def random_number():
    return random.randint(1, 999999999999999)


class Test():
    def __init__(self, driver):
        self.frank6_email = 'frank.chen+6@keeda.com.tw'
        self.passWD = 'aPPLEPLOKM123'
        self.driver = driver
        self.caps = {
            'deviceName': 'emulator-5556',
            'platformName': 'Android',
            'platformVersion': '13',
            'appPackage': 'com.keeda.keeda_app',
            'appActivity': 'com.keeda.keeda_app.MainActivity',
        }

    def connect_to_device(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)

    def find_element_XPATH(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def find_element_ID(self, ID):
        return self.driver.find_element(By.ID, ID)

    def login(self,driver):
        time.sleep(5)
        self.wait =  WebDriverWait(self.driver,10)