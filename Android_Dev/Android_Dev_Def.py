from appium import webdriver
from selenium.webdriver.common.by import By
import time
import random



class Test:
    def __init__(self):
        self.email  = 'frank.chen+6@keeda.com.tw'
        self.passwd = 'aPPLEPLOKM123'
        self.driver = None
        self.caps = {
            'deviceName': 'RF8N71V1A3N',
            'platformName': 'Android',
            'platformVersion': '12',
            'appPackage': 'com.example.dev_keeda',
            'appActivity': 'com.example.dev_keeda.MainActivity',
        }
        #print('123')

    def switch_account(self):
        self.email  = 'frank.chen+11@keeda.com.tw'
        self.passwd = 'aPPLEPLOKM123'
    def connect_to_device(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.caps)

    def random_number(self):
        return random.randint(1, 999999999999999)

    def login(self):
        time.sleep(3)
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").click()
        self.driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").send_keys(self.email)
        time.sleep(2)
        self.driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").click()
        self.driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").send_keys(self.passwd)
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="或"]').click()
        self.driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
        time.sleep(5)

    def navigate_to_event(self):
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="活動"]').click()
        time.sleep(5)

    def navigate_to_chat(self):
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="聊天"]').click()
        time.sleep(5)

    def navigate_to_post(self):
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="貼文"]').click()
        time.sleep(5)

    def navigate_to_settings(self):
        self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="設定"]').click()
        time.sleep(5)

    def navigate_to_personal_settings(self):
        self.driver.find_element(By.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]').click()
        self.driver.find_element(By.XPATH,
            '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/'
            'android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/'
            'android.view.View/android.view.View/android.view.View/android.widget.Button[3]').click()
        time.sleep(2)
        self.driver.find_element(By.ID,'com.android.permissioncontroller:id/permission_allow_button').click()
        time.sleep(2)

    def select_photo(self):
        self.driver.tap([(113, 1751), (967, 1877)], 500)
        self.driver.tap([(113, 1751), (967, 1877)], 500)
        time.sleep(2)

    def select_done(self):
        self.driver.tap([(1006, 145)], 50)
        time.sleep(3)

    def change_id(self):
        self.driver.find_element(By.CLASS_NAME,'android.widget.EditText').click()
        self.driver.find_element(By.CLASS_NAME,'android.widget.EditText').clear()
        self.driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys(self.random_number())
        self.driver.tap([(151, 418)], 50)