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
#caps['unicodeKeyboard'] = True
#caps['resetKeyboard'] = True


#User Info
passWD = 'aPPLEPLOKM123'
test_account_email = 'frank.chen+11@keeda.com.tw'
frank6_email = 'frank.chen+6@keeda.com.tw'



## 座標
##選定寵物生日的標調整年份
birth_year_x1 = 368
birth_year_y1 = 1967

birth_year_x2 = 368
birth_year_y2 = 2200

pet_other_variety_x = 100
pet_other_variety_y = 562

post_page_pet_first_picture_x = 300
post_page_pet_first_picture_y = 900

private_group_x = 121
private_group_y = 997


# Xpath
#一開始的登入按鈕
login_button_xpath = '//android.widget.Button[@content-desc="登入"]'
#輸入email的欄位
email_text_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]'
#輸入密碼的欄位
passWD_text_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]'
#點擊空白處收下鍵盤
click_nothing_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'
#第二次登入按鍵(打完信箱密碼後)
second_login_button_xpath = '//android.widget.Button[@content-desc="登入"]'
#進入設定頁面
setting_page_xpath = '//android.view.View[@content-desc="設定"]'
#進入個人頁面
personal_profile_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.widget.Button[1]'
#點擊使用者id
user_ID_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
#點擊性別收下按鍵
click_gender_xpath = '//android.view.View[@content-desc="性別"]'
#點擊使用者圖片
user_photo_stickers_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[3]'
#同意取用圖片
allow_access_photo_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'
#挑選第一張圖片
pick_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]'
#挑選完成
pick_compeleted_xpath = '//android.view.View[@content-desc="完成"]'
#儲存資料
storage_profile_xpath = '//android.widget.Button[@content-desc="儲存"]'
#1對1聊天室輸入框
one_to_one_chat_room_input_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'
#1對1聊天室發送message
one_to_one_send_message_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'
#新增寵物資料
add_pet_profile_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.widget.Button[2]'
#新增寵物圖片
add_pet_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[3]'
#寵物名字
pet_name_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText'
#寵物生日
pet_birthday_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]'
#選擇寵物生日
pet_birthday_select_xpath = '//android.widget.SeekBar[@content-desc="2023年"]'
#點擊必填來退鍵盤
click_nothing2_xpath = '//android.view.View[@content-desc="必填"]'
#選取生日完成
birthday_compelete_xpath = '//android.widget.Button[@content-desc="Done"]'
#寵物種類
pet_type_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[4]'
#點選其他種類
pet_other_type_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.RadioButton[3]'
#點選其他textfield
pet_other_type_textfield_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout'
#返回鍵
return_button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'
#知道了
OK_button_xpath = '//android.widget.Button[@content-desc="知道了"]'
#鍵盤彈起後的其他欄位
pet_other_type_textfield_after_keyboard_up_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText'
#寵物品種
pet_variety_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[10]'
#寵物品種裡面的其他選項
pet_variety_other_xpath = '//android.widget.RadioButton[@content-desc="其它"]'
#寵物品種裡面的其他欄位
pet_variety_other_textfield_xpath = '//android.view.View[@content-desc="其它"]/android.widget.EditText'
#寵物品種裡面的返回
pet_variety_return_button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'
#新增寵物
add_pet_compeleted_xpath = '//android.widget.Button[@content-desc="新增"]'
#切換到貼文頁面Navigation bar
post_page_xpath = '//android.view.View[@content-desc="貼文"]'
#新增貼文
add_post_xpath = '//android.widget.Button[@content-desc="貼文"]'
#貼文照片
add_post_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View'
#挑選貼文圖片
pick_post_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]'
#貼文內容
post_content_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText'
#鍵盤彈出後的貼文內容
post_content_after_keyboard_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText'
#分享
post_xpath = '//android.view.View[@content-desc="分享"]'
#第三個分頁
post_third_page_xpath = '//android.view.View[@content-desc="第 3 個分頁 (共 3 個)"]'
#新增照片
add_picture_xpath = '//android.widget.Button[@content-desc="照片"]'
#挑選第一張照片
pick_pet_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]'
#下一步
next_step_xpath = '//android.view.View[@content-desc="下一步"]'
#刪除貼文頁面的寵物照片
delete_post_page_pet_picture_xpath = '//android.widget.Button[@content-desc="是"]'
#切換至聊天頁
chat_page_xpath = '//android.view.View[@content-desc="聊天"]'
#建立聊天寵群
create_group_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[1]'
#寵群照片
group_picture_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[1]'
#私人群組
private_group_xpath = '//android.widget.RadioButton[@content-desc="私密 (僅獲得邀請的寵友加入)"]'
#挑選寵群照片
pick_group_picture_xpath = '//android.widget.LinearLayout[@content-desc="1683254220757.jpg, 2.71 KB, 10:37"]/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.ImageView[2]'