from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
from time import sleep
import threading
import SMA606Y_Def as Def_file
import datetime



driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Def_file.caps)
wait = WebDriverWait(driver, 15)


def swipe_page(self, driver,times):
    for i in range(1, times):

        driver.implicitly_wait(10)

        driver.swipe(560, 1600, 560, 880)
        time.sleep(1)
        driver.implicitly_wait(10)

def random_number():
    return random.randint(1,999999999999999999)



def delete_all_picture(self,driver,wait):

    driver.implicitly_wait(10)

    driver.tap([(Def_file.post_page_pet_first_picture_x,Def_file.post_page_pet_first_picture_y)],2000)

    #post_third_page_first_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.post_third_page_first_picture_xpath)))
    #driver.find_element(By.XPATH, Def_file.post_third_page_first_picture_xpath).click()

    try:
        delete_post_page_pet_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.delete_post_page_pet_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.delete_post_page_pet_picture_xpath).click()
    except NoSuchElementException:
        print("Element not found, ccontinuing with the rest of the code.")




def add_ten_picture(self,driver,wait):

    driver.implicitly_wait(10)

    add_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.add_picture_xpath)))
    driver.find_element(By.XPATH, Def_file.add_picture_xpath).click()

    driver.implicitly_wait(10)

    pick_pet_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_pet_picture_xpath)))
    driver.find_element(By.XPATH, Def_file.pick_pet_picture_xpath).click()

    next_step_xpath = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.next_step_xpath)))
    driver.find_element(By.XPATH, Def_file.next_step_xpath).click()
    time.sleep(2)

class Test:

    def login(self,driver,wait,user_email,user_passWD):
        Login_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.login_button_xpath)))
        driver.find_element(By.XPATH, Def_file.login_button_xpath).click()

        email_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.email_text_xpath)))
        driver.find_element(By.XPATH, Def_file.email_text_xpath).click()

        email_text_after_keyboard_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.email_text_after_keyboard_xpath)))
        driver.find_element(By.XPATH, Def_file.email_text_after_keyboard_xpath).send_keys(user_email)

        passWD_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.passWD_text_xpath)))
        driver.find_element(By.XPATH, Def_file.passWD_text_xpath).click()
        time.sleep(1)
        driver.find_element(By.XPATH, Def_file.passWD_text_xpath).send_keys(user_passWD)

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

        add_pet_profile_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.add_pet_profile_xpath)))
        driver.find_element(By.XPATH, Def_file.add_pet_profile_xpath).click()

        add_pet_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.add_pet_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.add_pet_picture_xpath).click()

        #allow_access_photo_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.allow_access_photo_xpath)))
        #driver.find_element(By.XPATH, Def_file.allow_access_photo_xpath).click()

        pick_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_picture_xpath).click()

        pick_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_compeleted_xpath).click()

        pet_name_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_name_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_name_xpath).click()
        driver.find_element(By.XPATH, Def_file.pet_name_xpath).send_keys('123456789ABCEDFG')
        driver.find_element(By.XPATH, Def_file.pet_name_xpath).clear()
        driver.find_element(By.XPATH, Def_file.pet_name_xpath).send_keys('&*#@! #我feef4121')
        #driver.find_elemnet(By.XPATH, Def_file.pet_name_xpath).click().clear()
        #driver.find_element(By.XPATH, Def_file.pet_name_xpath).send_keys('確定不能打特殊字元')
        click_nothing2_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.click_nothing2_xpath)))
        driver.find_element(By.XPATH, Def_file.click_nothing2_xpath).click()

        pet_birthday_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_birthday_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_birthday_xpath).click()

        pet_birthday_select_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_birthday_select_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_birthday_select_xpath).click()

        driver.swipe(Def_file.birth_year_x1, Def_file.birth_year_y1, Def_file.birth_year_x2, Def_file.birth_year_y2,500)
        birthday_compelete_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.birthday_compelete_xpath)))
        driver.find_element(By.XPATH, Def_file.birthday_compelete_xpath).click()

        pet_type_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_type_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_type_xpath).click()

        pet_other_type_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_other_type_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_other_type_xpath).click()

        return_button_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.return_button_xpath)))
        driver.find_element(By.XPATH, Def_file.return_button_xpath).click()

        OK_button_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.OK_button_xpath)))
        driver.find_element(By.XPATH, Def_file.OK_button_xpath).click()

        pet_other_type_textfield_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_other_type_textfield_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_other_type_textfield_xpath).click()
        time.sleep(2)
        driver.find_element(By.XPATH, Def_file.pet_other_type_textfield_after_keyboard_up_xpath).send_keys('!@#$我是$fwe153')

        return_button_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.return_button_xpath)))
        driver.find_element(By.XPATH, Def_file.return_button_xpath).click()

        pet_variety_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_variety_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_variety_xpath).click()

        #pet_variety_other_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_variety_other_xpath)))
        #driver.find_element(By.XPATH, Def_file.pet_variety_other_xpath).click()
        driver.tap([(Def_file.pet_other_variety_x,Def_file.pet_other_variety_y)])
        time.sleep(1)

        pet_variety_other_textfield_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pet_variety_other_textfield_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_variety_other_textfield_xpath).click()
        driver.find_element(By.XPATH, Def_file.pet_variety_other_textfield_xpath).send_keys('!@#!@#我是15&*()')

        pet_variety_return_button_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.return_button_xpath)))
        driver.find_element(By.XPATH, Def_file.pet_variety_return_button_xpath).click()

        add_pet_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.add_pet_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.add_pet_compeleted_xpath).click()



    def post(self,driver,wait):

        post_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.post_page_xpath)))
        driver.find_element(By.XPATH, Def_file.post_page_xpath).click()

        time.sleep(2)

        driver.swipe(560,880,560,1600,500)

        swipe_page(self,driver,10)

        add_post_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.add_post_xpath)))
        driver.find_element(By.XPATH, Def_file.add_post_xpath).click()

        add_post_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH,Def_file.add_post_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.add_post_picture_xpath).click()


        pick_post_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_post_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_post_picture_xpath).click()

        pick_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_compeleted_xpath).click()

        post_content_xpath = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.post_content_xpath)))
        driver.find_element(By.XPATH, Def_file.post_content_xpath).click()

        post_content_after_keyboard_wait = wait.until(EC.visibility_of_element_located((By.XPATH,Def_file.post_content_after_keyboard_xpath)))
        driver.find_element(By.XPATH, Def_file.post_content_after_keyboard_xpath).send_keys('!@#!@$@%#$%#@^%日常自動化測試fewfwsfefewfewfwe541534534534354')
        #driver.find_element(By.XPATH, Def_file.post_content_after_keyboard_xpath).send_keys(datetime.datetime.today())
        #driver.find_element(By.XPATH, Def_file.post_content_after_keyboard_xpath).send_keys(datetime.datetime.now())


        post_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.post_xpath)))
        driver.find_element(By.XPATH, Def_file.post_xpath).click()

        driver.implicitly_wait(15)

        swipe_page(self,driver,10)

        post_third_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.post_third_page_xpath)))
        driver.find_element(By.XPATH, Def_file.post_third_page_xpath).click()

        add_ten_picture(self,driver,wait)

        delete_all_picture(self,driver,wait)

        driver.implicitly_wait(10)


    def chat_page(self,driver,wait):

        chat_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.chat_page_xpath)))
        driver.find_element(By.XPATH, Def_file.chat_page_xpath).click()

        create_group_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.create_group_xpath)))
        driver.find_element(By.XPATH, Def_file.create_group_xpath).click()

        group_picture_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.group_picture_xpath)))
        driver.find_element(By.XPATH, Def_file.group_picture_xpath).click()

        #driver.find_element(By.XPATH, Def_file.pick_group_picture_xpath).click()
        #點擊圖片
        driver.tap([(Def_file.pick_group_picture_x,Def_file.pick_group_picture_y)],500)

        pick_group_picture_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.pick_group_picture_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.pick_group_picture_compeleted_xpath).click()
        #點擊私密群組
        driver.implicitly_wait(10)
        driver.tap([(Def_file.private_group_x,Def_file.private_group_y)])
        #點擊其他動物
        driver.implicitly_wait(10)
        driver.tap([(Def_file.others_pet_x,Def_file.others_pet_y)])
        #將頁面滑動至底部

        swipe_page(self,driver,3)

        group_name_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.group_name_xpath)))
        driver.find_element(By.XPATH, Def_file.group_name_xpath).click()

        group_name_after_keyboard_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.group_name_after_keyborad_xpath)))
        driver.find_element(By.XPATH, Def_file.group_name_after_keyborad_xpath).send_keys('@1!#2!3@4#5%6&*7@8#9)A(B_C_D(E)FG')

        #click_group_name_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.click_group_name_xpath)))
        #driver.find_element(By.XPATH, Def_file.click_group_name_xpath).click()

        driver.swipe(Def_file.create_group_page_start_y,Def_file.create_group_page_start_y,Def_file.create_group_page_end_x,Def_file.create_group_page_end_y)

        create_group_compeleted_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.create_group_compeleted_xpath)))
        driver.find_element(By.XPATH, Def_file.create_group_compeleted_xpath).click()

        driver.implicitly_wait(10)

        confirming_creation_pet_group_return_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.confirming_creation_pet_group_return_xpath)))
        driver.find_element(By.XPATH, Def_file.confirming_creation_pet_group_return_xpath).click()


    def search_friends(self,driver,wait):

        enter_search_friends_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.enter_search_friends_xpath)))
        driver.find_element(By.XPATH, Def_file.enter_search_friends_xpath).click()

        #滑動整個寵友頁面
        swipe_page(self,driver,10)

        enter_friends_name_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.enter_friends_name_xpath)))
        driver.find_element(By.XPATH, Def_file.enter_friends_name_xpath).click()

        enter_friends_name_after_keyboard_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.enter_friends_name_after_keyboard_xpath)))
        driver.find_element(By.XPATH, Def_file.enter_friends_name_after_keyboard_xpath).send_keys("自動化測試帳號")

        driver.implicitly_wait(10)

        driver.tap([(Def_file.send_friend_request_to_another_user_x,Def_file.send_friend_request_to_another_user_y)])

        after_friend_request_and_return_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.after_send_friend_request_and_return_xpath)))
        driver.find_element(By.XPATH, Def_file.after_send_friend_request_and_return_xpath).click()


    def log_out(self,driver,wait):

        setting_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.setting_page_xpath)))
        driver.find_element(By.XPATH, Def_file.setting_page_xpath).click()

        personal_profile_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.personal_profile_xpath)))
        driver.find_element(By.XPATH, Def_file.personal_profile_xpath).click()

        log_out_wait =  wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.log_out_xpath)))
        driver.find_element(By.XPATH, Def_file.log_out_xpath).click()

        log_out_wait2 = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.log_out_xpath)))
        driver.find_element(By.XPATH, Def_file.log_out_xpath).click()



    def inspect_page_and_agree_friend_request(self,driver,wait):

        chat_page_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.chat_page_xpath)))
        driver.find_element(By.XPATH, Def_file.chat_page_xpath).click()






    def unicode_test(self,driver):
        one_to_one_chat_room_input_xpath_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.one_to_one_chat_room_input_xpath)))
        driver.find_element(By.XPATH, Def_file.one_to_one_chat_room_input_xpath).click()

        time.sleep(1)

        driver.find_element(By.XPATH, Def_file.one_to_one_chat_room_input_xpath).send_keys(r"\u{1F600!@#$%^&*()-=+_)(*&}")
        one_to_one_send_message_wait = wait.until(EC.visibility_of_element_located((By.XPATH, Def_file.one_to_one_send_message_xpath)))
        driver.find_element(By.XPATH, Def_file.one_to_one_send_message_xpath).click()





Test().login(driver,wait,Def_file.frank6_email,Def_file.passWD)
Test().setting_profile(driver,wait)
Test().post(driver,wait)
Test().chat_page(driver,wait)
Test().search_friends(driver,wait)
Test().log_out(driver,wait)
Test().login(driver,wait,Def_file.test_account_email,Def_file.passWD)
#Test().unicode_test(driver)














