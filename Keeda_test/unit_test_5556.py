import asyncio
from selenium.webdriver.chrome.service import Service
from selenium import webdriver as s_webdriver
from selenium.webdriver.common.by import By
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
from time import sleep
import threading
import config
import unit_test_5554 as ut
import pyautogui

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config.caps2)
wait = WebDriverWait(driver, 8)

def check_email():
    s_driver = s_webdriver.Chrome()
    s_driver.get('https://mail.google.com/mail/u/0/#inbox')





class Test2:
    # 把config檔案的類別實例化
    xpath = config.Xpath()
    text = config.Text()
    coordinates = config.Coordinates()
    number = config.Number()

    def sign_up(self, driver, wait):

        print("等待後點擊登入按鈕")
        time.sleep(self.number.three)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.login_button_xpath)))
        driver.find_element(By.XPATH, self.xpath.login_button_xpath).click()

        print("再點一次Log in查看錯誤訊息")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.login_button_xpath)))
        driver.find_element(By.XPATH, self.xpath.login_button_xpath).click()

        print("點擊Sign up")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.click_sign_up)))
        driver.find_element(By.XPATH, self.xpath.click_sign_up).click()

        print("點擊email欄位")
        new_account_email = 'frank.chen+' + self.number.email_number + '@keeda.com.tw'
        self.number.email_number += 1
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.register_email)))
            driver.find_element(By.XPATH, self.xpath.register_email).click()
            driver.find_element(By.XPATH, self.xpath.register_email).send_keys(new_account_email)
        except Exception as e:
            print(e)
            driver.tap([(600, 1200)], 200)
            pyautogui.write(new_account_email, 0.2)
        finally:
            time.sleep(self.number.two)

        print("點擊輸入密碼")
        time.sleep(self.number.two)
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.register_pass_wd)))
            driver.find_element(By.XPATH,self.xpath.register_pass_wd).click()
            driver.find_element(By.XPATH, self.xpath.register_pass_wd).send_keys(config.pass_wd)
        except Exception as e:
            print(e)
            driver.tap([(500,1500)],200)
        finally:
            time.sleep(self.number.two)

        print("點擊確認密碼")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.enter_passwd_again)))
            driver.find_element(By.XPATH,self.xpath.enter_passwd_again).click()
            driver.find_element(By.XPATH, self.xpath.enter_passwd_again).send_keys(config.pass_wd)
        except Exception as e:
            print(e)
            driver.tap([(500,1780)],200)
        finally:
            time.sleep(self.number.two)

        print("點擊收下鍵盤")
        time.sleep(self.number.two)
        driver.tap([(1320,2816)],200)

        print("點擊同意按鈕")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.agree)))
            driver.find(By.XPATH,self.xpath.agree).click()
        except Exception as e:
            print(e)
            time.sleep(self.number.three)
            driver.tap([(152,2563)],200)

        print("點擊註冊")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.sign_up_complete)))
        driver.find_element(By.XPATH,self.xpath.sign_up_complete).click()

        print("送出")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_send)))
        driver.find_element(By.XPATH,self.xpath.confirm_send).click()

        print("接下來使用selenium web driver")





        time.sleep(self.number.three)
        print("點擊email欄位輸入")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.email_text_field)))
            driver.find_element(By.XPATH, self.xpath.email_text_field).click()
            driver.find_element(By.XPATH, self.xpath.email_text_field).send_keys('frank.chen+40@keeda.com.tw')

        except Exception as e:
            print(e)







test_instance2 = Test2()
#test_instance2.sign_up(driver, wait)
check_email()
