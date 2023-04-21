from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor



def random_number():
 return random.randint(1,999999999999999)


caps = {}
caps['deviceName'] = 'emulator-5554'
caps['uid'] = 'emulator-5554'
caps['platformName'] = 'Android'
caps['platformVersion'] = '13'
caps['appPackage'] = 'com.example.dev_keeda'
caps['appActivity'] = 'com.example.dev_keeda.MainActivity'
caps['noReset'] = True
caps['autoLaunch'] = False
passWD = 'aPPLEPLOKM123'

caps2 = {}
caps2['deviceName'] = 'emulator-5556'
caps2['platformName'] = 'Android'
caps2['platformVersion'] = '13'
caps2['appPackage'] = 'com.example.dev_keeda'
caps2['appActivity'] = 'com.example.dev_keeda.MainActivity'
caps2['noReset'] = True
caps2['autoLaunch'] = False

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
wait = WebDriverWait(driver, 15)

driver2 = webdriver.Remote('http://0.0.0.0:4724/wd/hub', caps2)
wait2 = WebDriverWait(driver2, 15)

text_field = wait.until(EC.visibility_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')))
driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()

text_field2 = wait2.until(EC.visibility_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')))
driver2.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').click()

executor = ThreadPoolExecutor()  # 設定一個執行 Thread 的啟動器
class Test:

 def emulator5554(self,driver,wait):

    send_key = wait.until(EC.visibility_of_element_located((By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')))
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys(random_number())
    out = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView')))
    driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView').click()


 def emulator5556(self,driver2,wait2):

    send_key2 = wait2.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText')))
    driver2.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText').send_keys(random_number())
    out2 = wait2.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView')))
    #print('1')
    driver2.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView').click()
    driver2.tap([(1288, 1790)], 0.5)


#for i in range(1,10):
for i in range(1,100):
 a = executor.submit(Test().emulator5554(driver,wait),driver,wait)
 b = executor.submit(Test().emulator5556(driver2,wait2),driver2,wait2)
