from appium import webdriver
from selenium.webdriver.common.by import By
import time
import random



class Test:
    def __init__(self):
        self.passwd = 'aPPLEPLOKM123'
        self.driver = None
        self.caps = {
            'deviceName': 'RF8N71V1A3N',
            'platformName': 'Android',
            'platformVersion': '12',
            'appPackage': 'com.example.dev_keeda',
            'appActivity': 'com.example.dev_keeda.MainActivity',
        }

    def connect_to_device(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)

    def random_number(self):
        return random.randint(1, 999999999999999)

    def login(self):
        self.driver.find_element_by_xpath('//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(3)
        self.driver.find_element_by_xpath(" //*[@text='電子郵件'] ").click()
        self.driver.find_element_by_xpath(" //*[@text='電子郵件'] ").\
            send_keys('frank.chen+6@keeda.com.tw')
        time.sleep(2)
        self.driver.find_element_by_xpath(" //*[@text='輸入密碼'] ").click()
        self.driver.find_element_by_xpath(" //*[@text='輸入密碼'] ").\
            send_keys(self.passwd)
        self.driver.find_element_by_accessibility_id("登入").click()
        time.sleep(5)

    def navigate_to_chat(self):
        self.driver.find_element_by_accessibility_id("活動").click()
        time.sleep(3)
        self.driver.find_element_by_accessibility_id("聊天").click()
        time.sleep(3)

    def navigate_to_post(self):
        self.driver.find_element_by_accessibility_id("貼文").click()
        time.sleep(3)

    def navigate_to_settings(self):
        self.driver.find_element_by_accessibility_id("設定").click()
        time.sleep(3)

    def navigate_to_personal_settings(self):
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]').click()
        self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View/android.view.View/android.widget.Button[3]').click()
        time.sleep(2)
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)

    def select_photo(self):
        self.driver.tap([(113, 1751), (967, 1877)], 500)
        self.driver.tap([(113, 1751), (967, 1877)], 500)
        time.sleep(2)

    def select_done(self):
        self.driver.tap([(1006, 145)], 50)
        time.sleep(3)

    def change_id(self):
        self.driver.find_element_by_class_name('android.widget.EditText').click()
        self.driver.find_element_by_class_name('android.widget.EditText').clear()
        self.driver.find_element_by_class_name('android.widget.EditText').send_keys(self.random_number())
        self.driver.tap([(151, 418)], 50)
