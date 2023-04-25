from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading



class Test:
    email = 'frank.chen+6@keeda.com.tw'
    passwd = 'aPPLEPLOKM123'
    caps = {
        'deviceName': 'RF8N71V1A3N',
        'platformName': 'Android',
        'platformVersion': '12',
        'appPackage': 'com.example.dev_keeda',
        'appActivity': 'com.example.dev_keeda.MainActivity',
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)

    def switch_account(self,driver):
        email  = 'frank.chen+11@keeda.com.tw'
        passwd = 'aPPLEPLOKM123'

    def random_number(self):
        return random.randint(1, 999999999999999)

    def login(self,driver):
        time.sleep(3)
        driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").click()
        driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").send_keys(self.email)
        time.sleep(2)
        driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").click()
        driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").send_keys(self.passwd)
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="或"]').click()
        driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(5)

    def navigate_to_event(self,driver):
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="活動"]').click()
        time.sleep(5)

    def navigate_to_chat(self,driver):
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="聊天"]').click()
        time.sleep(5)

    def navigate_to_post(self,driver):
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="貼文"]').click()
        time.sleep(5)

    def navigate_to_settings(self,driver):
        driver.find_element(By.XPATH, '//android.view.View[@content-desc="設定"]').click()
        time.sleep(5)

    def navigate_to_personal_settings(self,driver):
        driver.find_element(By.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]').click()
        driver.find_element(By.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View/android.view.View/android.widget.Button[3]').click()
        time.sleep(2)
        driver.find_element(By.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)

    def select_photo(self,driver):
        driver.tap([(113, 1751), (967, 1877)], 500)
        driver.tap([(113, 1751), (967, 1877)], 500)
        time.sleep(2)

    def select_done(self,driver):
        driver.tap([(1006, 145)], 50)
        time.sleep(3)

    def change_id(self,driver):
        driver.find_element(By.CLASS_NAME,'android.widget.EditText').click()
        driver.find_element(By.CLASS_NAME,'android.widget.EditText').clear()
        driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys(self.random_number())
        driver.tap([(151, 418)], 50)