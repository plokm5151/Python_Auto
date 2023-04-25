from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading

caps = {}
caps['deviceName'] = 'R58MC1Y2WYF'
caps['uid'] = 'R58MC1Y2WYF'
caps['platformName'] = 'Android'
caps['platformVersion'] = '11'
caps['appPackage'] = 'com.example.dev_keeda'
caps['appActivity'] = 'com.example.dev_keeda.MainActivity'
caps['noReset'] = True
caps['autoLaunch'] = False


#User Info
passWD = 'aPPLEPLOKM123'
test_account_email = 'frank.chen+11@keeda.com.tw'
frank6_email = 'frank.chen+6@keeda.com.tw'

# Xpath

login_button_xpath = '//android.widget.Button[@content-desc="登入"]'

email_text_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]'

passWD_text_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]'

click_nothing_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'

second_login_button_xpath = '//android.widget.Button[@content-desc="登入"]'

setting_page_xpath = '//android.view.View[@content-desc="設定"]'

personal_profile_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.widget.Button[1]'

user_ID_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'

click_gender_xpath = '//android.view.View[@content-desc="性別"]'

user_photo_stickers_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[3]'

allow_access_photo_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'

pick_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]'

pick_compeleted_xpath = '//android.view.View[@content-desc="完成"]'

storage_profile_xpath = '//android.widget.Button[@content-desc="儲存"]'

