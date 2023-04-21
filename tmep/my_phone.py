from appium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from time import sleep

def random_number():
 return random.randint(1,999999999999999)


class Test:
 caps = {}
 caps['deviceName']='RF8N71V1A3N'
 caps['platformName']='Android'
 caps['platformVersion']='12'
 caps['appPackage']='com.example.dev_keeda'
 caps['appActivity']='com.example.dev_keeda.MainActivity'
 passWD='aPPLEPLOKM123'

#連線至手機
 driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)


#定位登入按鍵並點擊
 time.sleep(3)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
 time.sleep(2)
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]').click()
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]').send_keys('frank.chen+6@keeda.com.tw')
 time.sleep(2)
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[2]').click()
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[2]').send_keys(passWD)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="或"]').click()
 time.sleep(2)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
