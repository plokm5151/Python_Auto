from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading

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
    driver2.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView').click()


#for i in range(1,10):
for i in range(1,100):
 thread1 = threading.Thread(target=Test().emulator5554, args=(driver, wait))
 thread2 = threading.Thread(target=Test().emulator5556, args=(driver2, wait2))

 thread1.start()
 thread2.start()

 thread1.join()
 thread2.join()



 #allow_button = wait.until(EC.visibility_of_element_located((By.ID, 'com.android.permissioncontroller:id/permission_deny_button')))
 #driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_deny_button').click()

 #login_button = wait.until(EC.visibility_of_element_located((By.XPATH,'//android.widget.Button[@content-desc="登入"]')))
 #driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
#定位輸入帳號密碼及按下登入

 #time.sleep(5)
 #driver.tap([(600,1200)],50)
 #email_text = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]')))
 #driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]').click()
 #driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]').send_keys('frank.chen+1@keeda.com.tw')
 #driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]").click()
 #driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]").send_keys(passWD)

 #driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView").click()
 #enter_app = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.Button[@content-desc="登入"]')))
 #driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()
 #driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()

 #chat_page = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.View[@content-desc="聊天"]')))
 #driver.find_element(By.XPATH, '//android.view.View[@content-desc="聊天"]')

 #chat_massage = wait.until(EC.visibility_of_element_located((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[2]')))
 #driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[2]').click()

 #into_group = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.view.View[@content-desc="test"]/android.widget.ImageView[1]')))
 #driver.find_element(By.XPATH, '//android.view.View[@content-desc="test"]/android.widget.ImageView[1]').click()


