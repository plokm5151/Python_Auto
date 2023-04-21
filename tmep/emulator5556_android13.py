from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep

def random_number():
 return random.randint(1,999999999999999)


class Test():
    def __init__(self, driver):
        self.frank6_email= 'frank.chen+6@keeda.com.tw'
        self.passWD='aPPLEPLOKM123'
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
        return self.driver.find_element(By.XPATH,xpath)

    def find_element_ID(self, ID):
        return self.driver.find_element(By.ID,ID)
    #def login(self):
   #     wait = webdriverwait


#定位登入按鍵並點擊
# time.sleep(10)
# driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_deny_button').click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
 #driver.find_element_by_xpath('//android.widget.Button[@content-desc="登入"]').click()
# time.sleep(3)
#定位輸入帳號密碼及按下登入
# driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]").click()
# time.sleep(2)
# driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]").send_keys('frank.chen+6@keeda.com.tw')
# time.sleep(2)
# driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]").click()
# driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]").send_keys(passWD)
# time.sleep(2)
# driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView").click()
# time.sleep(2)
# driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()

# driver.find_element(By.XPATH, '').click()


