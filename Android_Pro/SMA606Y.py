from appium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from time import sleep


class Test:
    def __init__(self):
        self.email= 'frank.chen@keeda.com.tw'
        self.passwd = 'aPPLEPLOKM123'
        self.driver = None
        self.caps = {
         'deviceName': 'R58MC1Y2WYF',
         'platformName': 'Android',
         'platformVersion': '11',
         'appPackage': 'com.keeda.keeda_app',
         'appActivity': 'com.keeda.keeda_app.MainActivity',
     }
    def switch_account(self):
        self.email  = 'frank.chen+2@keeda.com.tw'
        self.passwd = 'aPPLEPLOKM123'
    def connect_to_device(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)

    def random_number(self):
        return random.randint(1, 999999999999999)

    def login(self):
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]').click()
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]').send_keys(self.email)
        time.sleep(2)
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[2]').click()
        self.driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[2]').send_keys(self.passwd)
        self.driver.find_element(By.XPATH,'//android.view.View[@content-desc="或"]').click()
        self.driver.find_element(By.ID,'登入').click()
        time.sleep(5)
Test().__init__()
Test().connect_to_device()
Test().random_number()
Test().login()

