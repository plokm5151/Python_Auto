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
 #driver.find_element_by_xpath('//android.widget.Button[@content-desc="登入"]').click()
 time.sleep(3)
#定位輸入帳號密碼及按下登入
 driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").click()
 driver.find_element(By.XPATH, " //*[@text='電子郵件'] ").send_keys('frank.chen+6@keeda.com.tw')

 time.sleep(2)

#測試顯示密碼功能
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[2]/android.view.View').click()
# driver.tap([(901,1061),(1028,1187)],100)
 driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").click()
 driver.find_element(By.XPATH, " //*[@text='輸入密碼'] ").send_keys(passWD)

 driver.find_element(By.XPATH, '//android.view.View[@content-desc="或"]').click()
 time.sleep(2)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="登入"]').click()

#登入之後
 time.sleep(5)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="活動"]').click()
 time.sleep(5)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="聊天"]').click()
 time.sleep(5)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="貼文"]').click()
 time.sleep(5)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="設定"]').click()
 time.sleep(5)
 #點擊個人資料設定還有相片
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[1]').click()
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[3]').click()
 time.sleep(2)
 driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
 time.sleep(2)
 #利用座標選取圖片
 driver.tap([(113,1751),(967,1877)],500)
 driver.tap([(113,1751),(967,1877)],500)
 time.sleep(2)
 #利用座標點擊完成
 driver.tap([(1006,145)],50)
 time.sleep(3)
 #點擊修改id
 driver.find_element(By.CLASS_NAME, 'android.widget.EditText').click()
 driver.find_element(By.CLASS_NAME, 'android.widget.EditText').clear()
 driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys(random_number())
 driver.tap([(151,418)],50)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="儲存"]').click()
 time.sleep(2)

 #點進去關於我們查看
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[3]').click()
 time.sleep(2)
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]').click()
 time.sleep(1)
 #點擊貼文頁面
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="貼文"]').click()
 #滑動貼文
 for i in range(1,10):
  driver.swipe(533,1655,533,600,500)
  time.sleep(1)
 time.sleep(2)
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="第 3 個分頁 (共 3 個)"]').click()
 time.sleep(1)
 #+貼文
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="貼文"]').click()
 time.sleep(2)
 #選擇圖片
 driver.tap([(212,1012)],1)
 time.sleep(2)
 #確定選取
  #driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView').click()
  #time.sleep(2)
 #輸入貼文內容
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()
 time.sleep(2)
 driver.find_element(By.CLASS_NAME, 'android.widget.EditText').send_keys('test123')
 driver.tap([(353,1188)],1)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="分享"]').click()
 time.sleep(5)
 #切到貼文的第三個分頁
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="第 3 個分頁 (共 3 個)"]').click()
 time.sleep(1)
 #點選照片
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="照片"]').click()
 #選擇圖片
 driver.tap([(212,1012)],3000)
 time.sleep(1)
 #確定選取
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView').click()
 time.sleep(5)
 #接下來是刪除圖片先滑動
 driver.swipe(590, 690, 533, 590, 1800)
 driver.tap([(220,890)],3000)
 time.sleep(1)
 driver.find_element(By.XPATH, '//android.widget.Button[@content-desc="是"]').click()
 time.sleep(2)
 #切換到聊天頁面
 driver.find_element(By.XPATH, '//android.view.View[@content-desc="聊天"]').click()
 time.sleep(1)
 #搜尋寵友
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[5]').click()
 time.sleep(1)
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').click()
 driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText').send_keys('frank10')
 #按下加寵友
 driver.tap([(918,484)])
 #建立聊天寵群
 driver.find_element(By.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[1]').click()






 #點擊新增寵物
 #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.Button[2]').click()
 #time.sleep(2)



 #點擊設定寵物圖片(這邊要重製成function)
 #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.Button[3]').click()
 #利用座標選取圖片
 #driver.tap([(113,1751),(967,1877)],500)
 #driver.tap([(113,1751),(967,1877)],500)
 #time.sleep(2)
 #利用座標點擊完成
 #driver.tap([(1006,145)],50)
 #time.sleep(3)

 #輸入寵物名字
 #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]').click()
 #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.widget.EditText[1]').send_keys(random_number())
 #點擊空白處
 #driver.tap([(155,446)],50)
 #點擊寵物生日
 #driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View[6]').click()
 #driver.find_element_by_xpath('')
 #driver.swipe(start_x=367 ,start_y=1872 ,end_x=367 ,end_y= 2093,duration=1000)
 #time.sleep(1)
 #driver.find_element_by_xpath('//android.widget.Button[@content-desc="Done"]').click()



#------------------以下為功能測試區-------------------------------
#看起來使用文本定位也是可以，不過本程式通常情況下還是使用xpath
#driver.find_element_by_xpath(" //*[@text='電子郵件'] ").click()
#driver.find_element_by_xpath(" //*[@text='電子郵件'] ").send_keys('frank.chen+10@keeda.comt.tw')
#driver.background_app(5) 將app放入後台

#driver.find_elements(By.ID'登入').click()
#driver.find_element_by_accessibility_id('android.widget.Button')
#selected_icon=(By.XPATH,'//android.widget.Button[@content-desc="註冊"]')
#driver.find(selected_icon)


#driver.close_app()
#driver.quit()



