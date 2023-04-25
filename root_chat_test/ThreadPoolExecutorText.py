from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor
import ThreadPoolExecutorDef as Def_file



driver = webdriver.Remote(Def_file.driver_Remote, Def_file.caps)
wait = WebDriverWait(driver, 15)

driver2 = webdriver.Remote(Def_file.driver2_Remote, Def_file.caps2)
wait2 = WebDriverWait(driver2, 15)

Text_field = wait.until(EC.visibility_of_element_located((By.XPATH,Def_file.text_field)))
driver.find_element(By.XPATH,Def_file.text_field).click()

Text_field2 = wait2.until(EC.visibility_of_element_located((By.XPATH,Def_file.text_field2)))
driver2.find_element(By.XPATH,Def_file.text_field2).click()

executor = ThreadPoolExecutor()  # 設定一個執行 Thread 的啟動器
class Test:

 def emulator5554(self,driver,wait):

    Send_key = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.send_key)))
    driver.find_element(By.XPATH, Def_file.send_key).send_keys(Def_file.random_number())
    out = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.enter_button)))
    driver.find_element(By.XPATH, Def_file.enter_button).click()


 def emulator5556(self,driver2,wait2):

    send_key2 = wait2.until(EC.visibility_of_element_located((By.XPATH, Def_file.send_key2)))
    driver2.find_element(By.XPATH, Def_file.send_key2).send_keys(Def_file.random_number())
    out2 = wait2.until(EC.visibility_of_element_located((By.XPATH, Def_file.enter_button2)))
    driver2.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView').click()
    driver2.tap([(1288, 1790)], 0.5)


#for i in range(1,10):
for i in range(1,100):
 a = executor.submit(Test().emulator5554(driver,wait),driver,wait)
 b = executor.submit(Test().emulator5556(driver2,wait2),driver2,wait2)
