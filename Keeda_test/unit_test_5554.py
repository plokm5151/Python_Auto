import asyncio

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import config
import pyautogui


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', config.caps)
wait = WebDriverWait(driver, 8)

def swipe_page(self, driver,times):
    for i in range(1, times):


        driver.swipe(330, 970, 330, 420)
        time.sleep(1)
        driver.implicitly_wait(3)

def random_number():
    return random.randint(1,999999999999999999)


def select_time(driver,times):

    time.sleep(2)

    for i in range(1, times):
        driver.swipe(330, 990, 330, 930)
        driver.implicitly_wait(1)

    driver.tap([(370, 570)], 500)

def press_return(self,driver,wait):
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.search_friend_page_return)))
        driver.find_element(By.XPATH, self.xpath.search_friend_page_return).click()
    except Exception as e:
        print(e)
        driver.tap([(50, 110)], 500)
    finally:
        time.sleep(self.number.three)


def press_allow_access_photos(self,driver,wait):
    try:
        time.sleep(self.number.three)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.allow_pick_img_xpath)))
        driver.find_element(By.XPATH, self.xpath.allow_pick_img_xpath).click()
    except Exception as e:
        print(e)
    finally:
        time.sleep(self.number.two)


def add_photo(self,driver,wait):


    print("新增照片的按鈕")
    wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.add_photo_button)))
    driver.find_element(By.XPATH, self.xpath.add_photo_button).click()

    print("如果有的話就點擊允許通知")
    press_allow_access_photos(self=self, driver=driver, wait=wait)

    print("選取第一張照片")
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.pick_first_img_xpath)))
        driver.find_element(By.XPATH, self.xpath.pick_first_img_xpath).click()
    except Exception as e:

        print(e)
        driver.tap([(110, 1120)], 500)

    finally:
        time.sleep(self.number.two)

    print("點擊next step")
    wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.click_next_step)))
    driver.find_element(By.XPATH, self.xpath.click_next_step).click()
    time.sleep(self.number.ten)


def delete_photo(self,driver,wait):

    print("點擊第一張圖片進行刪除")
    driver.tap([(160,630)],2000)

    print("點擊確認刪除")
    try:
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_delete)))
        driver.find_element(By.XPATH,self.xpath.confirm_delete).click()
    except Exception as e:
        print(e)
        driver.tap([(250,750)],500)


def fill_date(self,driver):
    print("利用點擊的方式輸入11/09/2033")

    print("1")
    time.sleep(self.number.one)
    driver.tap([(110,830)],100)
    print("1")
    time.sleep(self.number.one)
    driver.tap([(110,830)],100)
    print("/")
    time.sleep(self.number.one)
    driver.tap([(90,1130)],100)
    print("0")
    time.sleep(self.number.one)
    driver.tap([(300,1110)],100)
    print("9")
    time.sleep(self.number.one)
    driver.tap([(500,1025)],100)
    print("/")
    time.sleep(self.number.one)
    driver.tap([(90,1130)],100)
    print("2")
    time.sleep(self.number.one)
    driver.tap([(300,830)],100)
    print("0")
    time.sleep(self.number.one)
    driver.tap([(300,1110)],100)
    print("3")
    time.sleep(self.number.one)
    driver.tap([(500,840)],100)
    print("3")
    time.sleep(self.number.one)
    driver.tap([(500,840)],100)


def check_country(self,driver,wait,xpath):
    print("點擊洲")
    wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(self.number.three)


    if(xpath == self.xpath.antarctic):
        print("點擊國家")
        time.sleep(self.number.three)
        driver.tap([(42,315)],500)
        driver.tap([(42,315)],500)

    else:
        print("滑動頁面")
        swipe_page(self=self, driver=driver, times=6)
        time.sleep(self.number.two)




    print("回到上一頁")
    wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.back)))
    driver.find_element(By.XPATH,self.xpath.back).click()


class Test:
    #把config檔案的類別實例化
    xpath = config.Xpath()
    text = config.Text()
    coordinates = config.Coordinates()
    number = config.Number()

    #測試活動的檢舉功能
    def test_event_report(self, driver, wait):
        event_report_wait = wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.event_report_xpath)))
        driver.find_element(By.XPATH, self.xpath.event_report_xpath).click()

        # 點擊輸入框
        event_report_textfield_wait = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.xpath.event_report_textfield_xpath)))
        driver.find_element(By.XPATH, self.xpath.event_report_textfield_xpath).click()
        #輸入預設文字
        driver.find_element(By.XPATH, self.xpath.event_report_textfield_xpath).send_keys(self.text.report_text)

        # 送出檢舉文字
        event_report_send_wait = wait.until(
            EC.visibility_of_element_located((By.XPATH, self.xpath.event_report_send_xpath)))
        driver.find_element(By.XPATH, self.xpath.event_report_send_xpath).click()

        driver.implicitly_wait(self.number.one)
        #點擊空白處
        driver.tap([(370,310)],500)



    #預設為一開始就在首頁
    #間隔設為兩秒
    time.sleep(number.two)
    def event_page(self,driver,wait):
        time.sleep(self.number.five)

        #等待活動頁面按鈕出現
        group_wait = wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.event_page_xpath)))
        driver.find_element(By.XPATH,self.xpath.event_page_xpath).click()

        #因為活動名稱所以Xpath無法定位，這邊用坐標定位，不同手機可能要有不同的座標
        time.sleep(self.number.five)
        driver.tap([(self.coordinates.first_event_x,self.coordinates.first_event_y)],500)
        print('點擊完成')


        #進入詳細頁面之後點擊功能按鈕
        #time.sleep(self.number.five)
        #wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.event_function_button_xpath)))
        #driver.find_element(By.XPATH, self.xpath.event_function_button_xpath).click()

        #測試檢舉功能
        #self.test_event_report(driver,wait)


        #等待2秒之後點擊上一頁
        time.sleep(self.number.five)
        driver.implicitly_wait(self.number.two)
        driver.tap([(self.coordinates.event_return_button_x,self.coordinates.event_return_button_y)],500)

        #滑動頁面至底部
        swipe_page(self = self,driver =driver,times=10)

    async def create_event(self,driver,wait):

        print("點擊建立活動按鈕")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_event_xpath)))
        driver.find_element(By.XPATH,self.xpath.create_event_xpath).click()
        time.sleep(self.number.five)

        print("選取照片")
        driver.tap([(self.coordinates.create_event_pick_img_x,self.coordinates.create_event_pick_img_y)],1000)

        print("點擊允許取用照片，如果系統沒有跳出那個通知就丟一個exception然後繼續進行")
        press_allow_access_photos(self = self, driver = driver, wait = wait)


        print("選取第一張照片，如果第一張照片定位不到就用座標點擊")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_first_img_xpath)))
            driver.find_element(By.XPATH,self.xpath.pick_first_img_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.pick_first_img_x,self.coordinates.pick_first_img_y)],1000)

        finally:
            time.sleep(self.number.three)


        print("點擊done")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.pick_img_done_xpath)))
            driver.find_element(By.XPATH, self.xpath.pick_img_done_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(700,115)], 200)

        print("輸入活動名稱")
        try:
            time.sleep(self.number.three)
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_name_textfield_xpath)))
            driver.find_element(By.XPATH,self.xpath.event_name_textfield_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.event_name_textfield_x,self.coordinates.event_name_textfield_y)],200)
        finally:
            print("此處等待鍵盤彈起")
            time.sleep(self.number.five)
            print("輸入活動名稱")
            pyautogui.typewrite(self.text.event_name_test)
            time.sleep(self.number.five)
            print("點擊取消鍵盤")
            driver.tap([(700,1145)],200)
            time.sleep(self.number.three)

        print("滑動至底層")
        swipe_page(self=self,driver=driver,times=4)

        print("點擊開始時間的日期")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.time_date_xpath)))
            driver.find_element(By.XPATH,self.xpath.time_date_xpath).click()
        except Exception as e:
            driver.tap([(430,243)],200)
        finally:
            time.sleep(self.number.three)

        print("直接選當天")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_date_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.select_date_done_xpath).click()
        time.sleep(self.number.three)

        print("點選開始時間的時間")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.time_time_xpath)))
        driver.find_element(By.XPATH,self.xpath.time_time_xpath).click()
        print("等待畫面出現")
        time.sleep(self.number.five)

        print("滑動時間選擇器")
        select_time(driver=driver,times = 5)

        print("選擇結束時間的日期")
        time.sleep(self.number.three)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.time_date_xpath)))
        driver.find_element(By.XPATH,self.xpath.time_date_xpath).click()
        time.sleep(self.number.three)

        print("直接選當天")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_date_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.select_date_done_xpath).click()
        time.sleep(self.number.three)

        print("點選結束時間的時間")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.time_time_xpath)))
        driver.find_element(By.XPATH,self.xpath.time_time_xpath).click()

        print("等待畫面出現")
        time.sleep(self.number.three)

        print("滑動時間選擇器")
        select_time(driver = driver,times = 6)

        print("點選報名截止的日期")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.time_date_xpath)))
        driver.find_element(By.XPATH,self.xpath.time_date_xpath).click()
        time.sleep(self.number.three)

        print("直接選當天")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_date_done_xpath)))
        driver.find_element(By.XPATH, self.xpath.select_date_done_xpath).click()
        time.sleep(self.number.three)

        print("點選報名截止的時間")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.time_time_xpath)))
        driver.find_element(By.XPATH,self.xpath.time_time_xpath).click()

        print("滑動時間選擇器")
        select_time(driver = driver,times = 2)

        print("點擊event location輸入框")
        driver.tap([(self.coordinates.event_location_textfield_x,self.coordinates.event_location_textfield_y)],500)
        print("等待鍵盤彈起")
        time.sleep(self.number.three)

        print("輸入文字然後點擊收下鍵盤")
        pyautogui.typewrite(self.text.event_location_test,0.2)
        time.sleep(self.number.three)
        driver.tap([(80,1225)],300)
        time.sleep(self.number.three)

        print("點擊下一頁")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_nextstep_xpath)))
        driver.find_element(By.XPATH,self.xpath.event_nextstep_xpath).click()
        time.sleep(self.number.three)

        print("選擇最大人數")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.maximum_people_xpath)))
            driver.find_element(By.XPATH,self.xpath.maximum_people_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.max_people_x,self.coordinates.max_people_y)],500)

        time.sleep(self.number.three)
        print("按下done")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_event_done_button_xpath)))
        driver.find_element(By.XPATH,self.xpath.create_event_done_button_xpath).click()

        print("選擇最大寵物數")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.maximum_pet_xpath)))
            driver.find_element(By.XPATH,self.xpath.maximum_pet_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.max_pet_x,self.coordinates.max_pet_y)],500)
        finally:
            time.sleep(self.number.three)

        print("按下done")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_event_done_button_xpath)))
        driver.find_element(By.XPATH,self.xpath.create_event_done_button_xpath).click()
        time.sleep(self.number.three)

        try:
            print("按下活動描述按鈕")
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.event_description_xpath)))
            driver.find_element(By.XPATH, self.xpath.event_description_xpath).click()
            driver.find_element(By.XPATH, self.xpath.event_description_xpath).send_keys(self.text.event_test)
        except Exception as e:
            print(e)
            driver.tap([(200, 935)], 500)

        finally:
            pyautogui.typewrite(self.text.event_description)
            print("點擊空白處收下鍵盤")
            driver.tap([(365,500)],500)
            time.sleep(self.number.three)

        print("點擊建立活動")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_event_button_xpath)))
        driver.find_element(By.XPATH,self.xpath.create_event_button_xpath).click()
        time.sleep(self.number.three)

        print("點擊確認")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_button_xpath)))
        driver.find_element(By.XPATH,self.xpath.confirm_button_xpath).click()

        print("點擊知道了")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.acknowledge_xpath)))
        driver.find_element(By.XPATH,self.xpath.acknowledge_xpath).click()



    def test(self,driver,wait):

        try:
            print("按下活動描述按鈕")
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.event_description_xpath)))
            driver.find_element(By.XPATH, self.xpath.event_description_xpath).click()
            driver.find_element(By.XPATH, self.xpath.event_description_xpath).send_keys(self.text.event_test)
        except Exception as e:
            print(e)
            driver.tap([(200,935)],500)


    def edit_event(self,driver,wait):

        print("按下我的活動")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.my_event_xpath)))
        driver.find_element(By.XPATH,self.xpath.my_event_xpath).click()
        time.sleep(self.number.three)

        print("點擊編輯活動")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.edit_event_xpath)))
        driver.find_element(By.XPATH,self.xpath.edit_event_xpath).click()
        time.sleep(self.number.three)


        print("點擊輸入框")
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'android.widget.EditText')))
        driver.find_element(By.CLASS_NAME,'android.widget.EditText').click()
        driver.find_element(By.CLASS_NAME,'android.widget.EditText').send_keys(self.text.event_location_test2)

        print("點擊左上角收下鍵盤")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.leading)))
            driver.find_element(By.XPATH, self.xpath.leading).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.keyboard_done_x, self.coordinates.keyboard_done_y)], 500)
        finally:
            time.sleep(self.number.two)

        print("滑動頁面")
        swipe_page(self = self,driver = driver, times = 3)


        print("點擊活動地點")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.edit_event_location_xpath)))
            driver.find_element(By.XPATH,self.xpath.edit_event_location_xpath).click()
            driver.find_element(By.XPATH,self.xpath.edit_event_location_xpath).send_keys(self.text.event_location_test2)
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.edit_location_x,self.coordinates.edit_location_y)],500)
            pyautogui.typewrite(self.text.event_location_test2)
        finally:
            time.sleep(self.number.three)

        print("點擊左上角收下鍵盤")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.leading)))
            driver.find_element(By.XPATH,self.xpath.leading).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.keyboard_done_x,self.coordinates.keyboard_done_y)],500)
        finally:
            time.sleep(self.number.two)



        print("點擊下一步")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_nextstep_xpath)))
            driver.find_element(By.XPATH,self.xpath.event_nextstep_xpath).click()
            time.sleep(self.number.three)
        except Exception as e:
            print(e)

        finally:
            time.sleep(self.number.two)


        print("點擊儲存")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_edit_save)))
        driver.find_element(By.XPATH,self.xpath.event_edit_save).click()
        time.sleep(self.number.three)

        print("刪除活動")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.delete_event)))
        driver.find_element(By.XPATH,self.xpath.delete_event).click()

        print("確認刪除")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_delete)))
        driver.find_element(By.XPATH,self.xpath.confirm_delete).click()
        time.sleep(self.number.five)

        print("按下上一頁")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.my_event_leading_button)))
            driver.find_element(By.XPATH,self.xpath.my_event_leading_button).click()
        except Exception as e:
            print(e)
            driver.tap([(self.coordinates.my_event_leading_button_x,self.coordinates.my_event_leading_button_y)])
        finally:
            time.sleep(self.number.five)

    def group_page_and_add_friend(self,driver,wait):

        print("點擊寵群頁面")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.group_page)))
            driver.find_element(By.XPATH,self.xpath.group_page).click()
        except Exception as e:
            print(e)
            driver.tap([(381,1176)],500)
        finally:
            time.sleep(self.number.five)

        print("向下滑動頁面")
        swipe_page(self = self, driver = driver,times=10)

        print("點擊搜尋寵友")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.search_friend_page)))
        driver.find_element(By.XPATH,self.xpath.search_friend_page).click()
        #TODO
        time.sleep(self.number.four)

        print("寵友")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.search_friend)))
        driver.find_element(By.XPATH,self.xpath.search_friend).click()
        driver.find_element(By.XPATH,self.xpath.search_friend).send_keys(self.text.my_name)
        time.sleep(self.number.three)

        print("加好友")
        driver.tap([(630,365)],500)

        print("按下上一頁")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.search_friend_page_return)))
        driver.find_element(By.XPATH,self.xpath.search_friend_page_return).click()
        time.sleep(self.number.two)

    def chat_page_and_friend_list(self,driver,wait):

        print("點擊寵群頁面")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.group_page)))
            driver.find_element(By.XPATH, self.xpath.group_page).click()
        except Exception as e:
            print(e)
            driver.tap([(381, 1176)], 500)
        finally:
            time.sleep(self.number.five)

        print("進到寵友頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.friend_list_page)))
        driver.find_element(By.XPATH,self.xpath.friend_list_page).click()
        time.sleep(self.number.five)

        print("點擊輸入框")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.friend_list_page_textfield)))
        driver.find_element(By.XPATH,self.xpath.friend_list_page_textfield).click()
        time.sleep(self.number.three)

        print("搜尋my_name，如果想要搜尋其他人請把my_name改掉")
        driver.find_element(By.XPATH,self.xpath.friend_list_page_textfield).send_keys(self.text.my_name)
        time.sleep(self.number.two)

        print("進入聊天室")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.into_chatroom_with_first_first_friend)))
        driver.find_element(By.XPATH,self.xpath.into_chatroom_with_first_first_friend).click()
        time.sleep(self.number.five)

        print("發送照片")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.send_photo)))
        driver.find_element(By.XPATH,self.xpath.send_photo).click()
        time.sleep(self.number.two)

        print("點擊通知")
        press_allow_access_photos(self = self,driver = driver, wait = wait)

        print("點擊第一張照片")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.send_first_photo)))
            driver.find_element(By.XPATH,self.xpath.send_first_photo).click()
        except Exception as e:
            print(e)
            driver.tap([(100,980)],500)
        finally:
            time.sleep(self.number.three)

        print("送出按鈕")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.send_button)))
            driver.find_element(By.XPATH,self.xpath.send_button).click()
        except Exception as e:
            print(e)
            driver.tap([(675,800)],500)
        finally:
            time.sleep(self.number.two)

        print("確認送出")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_send)))
        driver.find_element(By.XPATH,self.xpath.confirm_send).click()

        print("等待5秒確認圖片是否送出")
        time.sleep(self.number.five)

        print("點擊輸入框並且寫入訊息")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.chatroom_textfield)))
        driver.find_element(By.XPATH,self.xpath.chatroom_textfield).click()
        driver.find_element(By.XPATH,self.xpath.chatroom_textfield).send_keys(self.text.hello)

        print("發送訊息")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.send_message)))
            driver.find_element(By.XPATH,self.xpath.send_message).click()
        except Exception as e:
            print(e)
            time.sleep(self.number.three)
            driver.tap([(680,590)],200)

        print("按下上一頁 這邊的xpath沿用之前的")
        press_return(self = self,driver = driver, wait = wait)
        print("再按一次回到主頁")
        press_return(self = self,driver = driver, wait = wait)

        time.sleep(self.number.five)


    def post(self,driver,wait):

        print("進入po文頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.into_all_post)))
        driver.find_element(By.XPATH,self.xpath.into_all_post).click()
        time.sleep(self.number.five)

        print("滑動all post頁面")
        swipe_page(self = self, driver = driver, times = 10)

        print("自己PO文")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.post)))
        driver.find_element(By.XPATH,self.xpath.post).click()

        print("點擊通知")
        press_allow_access_photos(self = self ,driver = driver, wait = wait)

        print("選取照片")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_post_photo)))
            driver.find_element(By.XPATH,self.xpath.select_post_photo).click()
        except Exception as e:
            print(e)
            driver.tap([(700,670)],500)
        finally:
            time.sleep(self.number.two)

        print("選取第一張照片")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_first_img_xpath)))
            driver.find_element(By.XPATH,self.xpath.pick_first_img_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(110,1110)],500)
        finally:
            time.sleep(self.number.one)

        print("按下done")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_img_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.pick_img_done_xpath).click()

        print("點擊輸入框")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.post_textfield)))
        driver.find_element(By.XPATH,self.xpath.post_textfield).click()

        print("輸入文字")
        driver.find_element(By.XPATH, self.xpath.post_textfield).send_keys(self.text.post_test)
        time.sleep(self.number.two)

        print("成功PO文")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.post_done)))
        driver.find_element(By.XPATH,self.xpath.post_done).click()

        time.sleep(self.number.ten)

    def comment_my_post(self,driver,wait):

        print("進入自己的貼文")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.my_post)))
            driver.find_element(By.XPATH,self.xpath.my_post).click()
        except Exception as e:
            print(e)
            driver.tap([(410,800)],500)
        finally:
            time.sleep(self.number.three)

        print("進到貼文之後按讚")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.my_post_page_like)))
        driver.find_element(By.XPATH,self.xpath.my_post_page_like).click()

        print("點擊輸入框")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.comment_input_bar)))
        driver.find_element(By.XPATH,self.xpath.comment_input_bar).click()
        driver.find_element(By.XPATH,self.xpath.comment_input_bar).send_keys(self.text.hello)
        time.sleep(self.number.three)

        print("點擊發送")
        driver.tap([(680,640)],500)
        time.sleep(self.number.three)

        print("進入編輯頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.edit_post)))
        driver.find_element(By.XPATH,self.xpath.edit_post).click()
        time.sleep(self.number.three)

        print("編輯留言")
        pyautogui.typewrite(self.text.post_test)
        time.sleep(self.number.three)

        print("返回上一頁")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.edit_post_return)))
            driver.find_element(By.XPATH,self.xpath.edit_post_return).click()
        except Exception as e:
            driver.tap([(57,112)],500)
        finally:
            time.sleep(self.number.three)

        print("按下繼續編輯")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.continue_edit)))
        driver.find_element(By.XPATH,self.xpath.continue_edit).click()
        time.sleep(self.number.five)

        print("收下鍵盤")
        driver.tap([(80,1230)],200)

        print("按下更新貼文")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.update_post)))
        driver.find_element(By.XPATH,self.xpath.update_post).click()

        time.sleep(self.number.two)

        print("進入編輯頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.edit_post)))
        driver.find_element(By.XPATH, self.xpath.edit_post).click()
        time.sleep(self.number.five)

        print("收下鍵盤")
        driver.tap([(80,1230)],200)

        print("刪除貼文")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.delete_post)))
        driver.find_element(By.XPATH,self.xpath.delete_post).click()

        print("確認刪除")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_delete)))
        driver.find_element(By.XPATH,self.xpath.confirm_delete).click()

        time.sleep(self.number.five)




    def add_photos_and_delete(self,driver,wait):
        print("進入all post頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.into_all_post)))
        driver.find_element(By.XPATH, self.xpath.into_all_post).click()

        time.sleep(self.number.five)

        print("進入po照片的頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.add_photo_page)))
        driver.find_element(By.XPATH, self.xpath.add_photo_page).click()

        for i in range(0,1):
            add_photo(self = self, driver = driver, wait = wait)
            delete_photo(self=self,driver = driver,wait = wait)


    def see_other_post(self,driver,wait):

        time.sleep(self.number.three)

        print("進入other_post檢查")
        driver.tap([(375,285)],500)

        time.sleep(self.number.five)

        print("點擊第一個好友")
        driver.tap([(200,236)],500)

        time.sleep(self.number.three)

        print("滑動他的頁面")
        swipe_page(self = self,driver = driver,times = 8)

        print("進入照片區")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.other_post_photh)))
            driver.find_element(By.XPATH,self.xpath.other_post_photo).click()
        except Exception as e:
            for i in range(0,8):
                driver.swipe(330,420,330,970)
            driver.tap([(570,520)],500)
        finally:
            time.sleep(self.number.five)

        print("稍微滑動頁面")
        swipe_page(self = self,driver = driver,times = 3)

        print("回到首頁")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.home_page)))
        driver.find_element(By.XPATH,self.xpath.home_page).click()

        time.sleep(self.number.five)

    def create_exchange_item(self,driver,wait):


        swipe_page(self = self,driver = driver,times = 3)

        print("進入二手物品頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.exchange_page)))
        driver.find_element(By.XPATH,self.xpath.exchange_page).click()

        print("建立二手物品")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_item)))
            driver.find_element(By.XPATH,self.xpath.create_item).click()
        except Exception as e:
            print(e)
            time.sleep(self.number.three)
            driver.tap([(85,223)],200)

        time.sleep(self.number.five)

        print("點擊新增圖片")
        driver.tap([(700,680)],500)

        print("點擊允許存取照片")
        press_allow_access_photos(self = self, driver = driver, wait = wait)

        print("選取第一張照片")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.pick_first_img_xpath)))
            driver.find_element(By.XPATH, self.xpath.pick_first_img_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(110, 1120)], 500)

        finally:
            time.sleep(self.number.two)

        print("點擊done")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_img_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.pick_img_done_xpath).click()

        print("點擊命名輸入框")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.item_title)))
            driver.find_element(By.XPATH,self.xpath.item_title).click()
            print("輸入文字")
            driver.find_element(By.XPATH, self.xpath.item_title).send_keys(self.text.item_title_test)
            time.sleep(self.number.three)
        except Exception as e:
            print(e)
            time.sleep(self.number.five)
            driver.tap([(170,885)],500)
            print("輸入文字")
            pyautogui.typewrite(self.text.item_title_test)

        finally:
            time.sleep(self.number.five)


        print("收下鍵盤")
        driver.tap([(700, 1125)], 200)

        print("選取交易日期")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.exchange_date)))
        driver.find_element(By.XPATH,self.xpath.exchange_date).click()

        print("點擊右上角的輸入日期")
        time.sleep(self.number.three)
        driver.tap([(650,280)],200)

        print("利用點擊的方式輸入11/09/2033")
        fill_date(self = self,driver = driver)


        print("點擊ok")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_date_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.select_date_done_xpath).click()

        print("下一步")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_nextstep_xpath)))
        driver.find_element(By.XPATH,self.xpath.event_nextstep_xpath).click()

        print("確認亞洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.asia)

        print("確認歐洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.europe)

        print("確認非洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.africa)

        print("確認北美洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.north_america)

        print("確認南美洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.south_america)

        print("確認大洋洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.oceania)

        print("確認??洲國家")
        check_country(self = self, driver = driver, wait = wait, xpath=self.xpath.antarctic)



        print("選品種")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.item_category)))
        driver.find_element(By.XPATH,self.xpath.item_category).click()

        print("選其他種類")
        time.sleep(self.number.five)
        driver.tap([(51,987)],200)
        driver.tap([(51,987)],200)
        time.sleep(self.number.three)

        print("back")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.back)))
        driver.find_element(By.XPATH,self.xpath.back).click()

        print('往下滑動頁面')
        driver.swipe(350,1145,350,400)

        print("點擊輸入框")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.item_description)))
            driver.find_element(By.XPATH,self.xpath.item_description).click()
            driver.find_element(By.XPATH,self.xpath.item_description).send_keys(self.text.item_description_test1+self.text.item_description_test2+self.text.item_description_test3)
        except Exception as e:
            print(e)
            time.sleep(self.number.three)
            driver.tap([(200,635)])
            pyautogui.typewrite(self.text.item_description_test1+self.text.item_description_test2+self.text.item_description_test3)

        print("收下鍵盤")
        time.sleep(self.number.five)
        driver.tap([(100,1225)],200)

        print("建立物品")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.create_item)))
        driver.find_element(By.XPATH,self.xpath.create_item).click()
        time.sleep(self.number.three)

        print("確認建立物品")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_button_xpath)))
        driver.find_element(By.XPATH,self.xpath.confirm_button_xpath).click()

        print("知道了")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.acknowledge_xpath)))
        driver.find_element(By.XPATH,self.xpath.acknowledge_xpath).click()

        time.sleep(self.number.three)
    def check_item_detail_page(self,driver,wait):

        print("點擊物品進入詳細頁面")
        time.sleep(self.number.three)
        driver.tap([(200,300)],200)

        print("點擊物品進入詳細頁面")
        time.sleep(self.number.ten)
        driver.tap([(200, 300)], 200)

        time.sleep(self.number.three)
        print("向下滑動")
        swipe_page(self = self,driver = driver,times = 4)

        print("點擊function button")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.item_function_button)))
        driver.find_element(By.XPATH,self.xpath.item_function_button).click()

        print("編輯物品")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.edit_item)))
        driver.find_element(By.XPATH,self.xpath.edit_item).click()
        '''
        print("選取照片")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.select_item_photo)))
        driver.find_element(By.XPATH,self.xpath.select_item_photo).click()

        press_allow_access_photos(self = self, driver = driver, wait = wait)

        print("選照片")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_first_img_xpath)))
            driver.find_element(By.XPATH,self.xpath.pick_first_img_xpath).click()
        except Exception as e:
            print(e)
            driver.tap([(130,1117)],200)
        finally:
            time.sleep(self.number.two)
        
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.pick_img_done_xpath)))
        driver.find_element(By.XPATH,self.xpath.pick_img_done_xpath).click()
        '''
        print("滑動頁面")
        swipe_page(self = self,driver = driver,times = 4)

        print("點擊下一步")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.event_nextstep_xpath)))
        driver.find_element(By.XPATH,self.xpath.event_nextstep_xpath).click()

        print("滑動頁面")
        swipe_page(self = self,driver = driver,times = 4)
        time.sleep(self.number.three)

        print("save")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.save)))
        driver.find_element(By.XPATH,self.xpath.save).click()

        print("點擊function button")
        wait.until(EC.visibility_of_element_located((By.XPATH, self.xpath.item_function_button)))
        driver.find_element(By.XPATH, self.xpath.item_function_button).click()

        print("點擊刪除")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.delete_item)))
        driver.find_element(By.XPATH,self.xpath.delete_item).click()

        print("確認刪除")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.confirm_delete)))
        driver.find_element(By.XPATH,self.xpath.confirm_delete).click()

        print("回到交換主頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.back_to_exchange_page)))
        driver.find_element(By.XPATH,self.xpath.back_to_exchange_page).click()

        print("回到主頁")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.my_event_leading_button)))
        driver.find_element(By.XPATH,self.xpath.my_event_leading_button).click()

        print("往上滑動頁面")
        driver.swipe(350, 400, 350, 1145)

        #print("點擊分享")
        #wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.share)))
        #driver.find_element(By.XPATH,self.xpath.share).click()

        #print("點擊email")
        #try:
        #    wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.email)))
        #    driver.find_element(By.XPATH,self.xpath.email).click()
        #except Exception as e:
        #    time.sleep(self.number.three)
        #    driver.tap([(483,1079)],200)
        #finally:
        #    time.sleep(self.number.two)

        #print("點擊Subject")
        #try:
        #    wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.subject)))
        #    driver.find_element(By.XPATH,self.xpath.subject).click()
        #    driver.find_element(By.XPATH,self.xpath.subject).send_keys(self.text.share_test)
        #except Exception as e:
        #    print(e)
        #    time.sleep(self.number.three)
        #    driver.tap([(200,450)],200)
        #    pyautogui.write(self.text.share_test)
        #finally:
        #    print("點擊收下按鈕")
        #    time.sleep(self.number.two)
        #    driver.tap([(80,1228)],200)

        time.sleep(self.number.three)

    def check_notification_page(self,driver,wait):

        time.sleep(self.number.three)

        print("往上滑動頁面")
        driver.swipe(350, 500, 350, 1100)

        print("進入通知頁面")
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.notification_page)))
            driver.find_element(By.XPATH,self.xpath.notification_page).click()
        except Exception as e:
            print(e)
            driver.tap([(676,113)],200)
        finally:
            time.sleep(self.number.three)

        print("滑動頁面")
        swipe_page(self =self,driver = driver, times = 11)

        print("離開通知頁面")
        wait.until(EC.visibility_of_element_located((By.XPATH,self.xpath.leave_notification_page)))
        driver.find_element(By.XPATH,self.xpath.leave_notification_page).click()

        time.sleep(self.number.three)


test_instance = Test()

test_instance.event_page(driver,wait)
asyncio.run(test_instance.create_event(driver,wait))
test_instance.edit_event(driver,wait)
test_instance.group_page_and_add_friend(driver,wait)
test_instance.chat_page_and_friend_list(driver,wait)
test_instance.post(driver,wait)
test_instance.comment_my_post(driver,wait)
test_instance.add_photos_and_delete(driver,wait)
test_instance.see_other_post(driver,wait)
test_instance.create_exchange_item(driver,wait)
test_instance.check_item_detail_page(driver,wait)
test_instance.check_notification_page(driver,wait)



#text_instance.test(driver,wait)