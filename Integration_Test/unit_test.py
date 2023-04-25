from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading
import SMA606Y_Def as Def_file


def random_number():
 return random.randint(1,999999999999999)


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Def_file.caps)
wait = WebDriverWait(driver, 15)


class Test:

    def login(self,driver,wait,frank6_email,passWD):
        Login_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.login_button_xpath)))
        driver.find_element(By.XPATH, Def_file.login_button_xpath).click()

        email_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.email_text_xpath)))
        driver.find_element(By.XPATH, Def_file.email_text_xpath).click()
        driver.find_element(By.XPATH, Def_file.email_text_xpath).send_keys(frank6_email)

        passWD_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.passWD_text_xpath)))
        driver.find_element(By.XPATH, Def_file.passWD_text_xpath).click()
        driver.find_element(By.XPATH, Def_file.passWD_text_xpath).send_keys(passWD)

        click_nothing_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.click_nothing_xpath)))
        driver.find_element(By.XPATH, Def_file.click_nothing_xpath).click()

        second_login_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.second_login_button_xpath)))
        driver.find_element(By.XPATH, Def_file.second_login_button_xpath).click()

    def setting_profile(self,driver,wait):
        setting_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.setting_page_xpath)))
        driver.find_element(By.XPATH, Def_file.setting_page_xpath).click()

        personal_profile_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.personal_profile_xpath)))
        driver.find_element(By.XPATH, Def_file.personal_profile_xpath).click()

        user_ID_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.user_ID_xpath)))
        driver.find_element(By.XPATH, Def_file.user_ID_xpath).click()
        driver.find_element(By.XPATH, Def_file.user_ID_xpath).clear()
        driver.find_element(By.XPATH, Def_file.user_ID_xpath).send_keys(random_number())

        click_gender_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.click_gender_xpath)))
        driver.find_element(By.XPATH, Def_file.click_gender_xpath).click()

        user_photo_stickers_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.user_photo_stickers_xpath)))
        driver.find_element(By.XPATH, Def_file.user_photo_stickers_xpath).click()

        allow_access_photo_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.allow_access_photo_xpath)))
        driver.find_element(By.XPATH, Def_file.allow_access_photo_xpath).click()

        pick_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_picture_xpath).click()

        pick_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_compeleted_xpath).click()

        storage_profile_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.storage_profile_xpath)))
        driver.find_element(By.XPATH, Def_file.storage_profile_xpath).click()

Test().setting_profile(driver,wait)














#Test().login(driver,wait,Def_file.frank6_email,Def_file.passWD)
