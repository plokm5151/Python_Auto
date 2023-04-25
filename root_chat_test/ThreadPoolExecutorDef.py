from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from time import sleep
import threading
from concurrent.futures import ThreadPoolExecutor

## function define

def random_number():
 return random.randint(1,999999999999999)



## Remote info

driver_Remote = 'http://127.0.0.1:4723/wd/hub'
driver2_Remote = 'http://0.0.0.0:4724/wd/hub'

## basic info
frank2_email = 'frank.chen+2@keeda.com.tw'
frank1_email = 'frank.chen+1@keeda.com.tw'
passWD = 'aPPLEPLOKM123'

## Xpath info

text_field = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
text_field2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'

send_key = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
send_key2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'

enter_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'
enter_button2 = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'






## caps

caps = {
        'deviceName': 'emulator-5554',
        'uid': 'emulator-5554',
        'platformName': 'Android',
        'platformVersion': '13',
        'appPackage': 'com.example.dev_keeda',
        'appActivity': 'com.example.dev_keeda.MainActivity',
        'noRest': True,
        'autoLaunch': False
}

caps2 = {
        'deviceName': 'emulator-5556',
        'uid': 'emulator-5556',
        'platformName': 'Android',
        'platformVersion': '13',
        'appPackage': 'com.example.dev_keeda',
        'appActivity': 'com.example.dev_keeda.MainActivity',
        'noReset': True,
        'autoLaunch': False
}