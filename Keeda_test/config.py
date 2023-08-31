
#基礎資訊配置
caps = {}
caps['deviceName'] = 'emulator-5554'
caps['uid'] = 'emulator-5554'
caps['platformName'] = 'Android'
caps['platformVersion'] = '13'
caps['appPackage'] = 'com.example.dev_keeda'
caps['appActivity'] = 'com.example.dev_keeda.MainActivity'
caps['noReset'] = True
caps['autoLaunch'] = False
#caps['unicodeKeyboard'] = True
#caps['resetKeyboard'] = True


caps2 = {}
caps2['deviceName'] = 'emulator-5556'
caps2['uid'] = 'emulator-5556'
caps2['platformName'] = 'Android'
caps2['platformVersion'] = '13'
caps2['appPackage'] = 'com.example.dev_keeda'
caps2['appActivity'] = 'com.example.dev_keeda.MainActivity'
caps2['noReset'] = True
caps2['autoLaunch'] = False
#caps2['unicodeKeyboard'] = True
#caps2['resetKeyboard'] = True


# User Info
pass_wd = 'aPPLEPLOKM123'
test_account_email = 'frank.chen+11@keeda.com.tw'
frank6_email = 'frank.chen+6@keeda.com.tw'




class Number:
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    ten = 10
    email_number = 40

class Text:
    report_text = 'report by frank'
    event_name_test = 'Event Name Test'
    event_location_test = 'Event Location Test'
    event_test = 'Event Test'
    event_description = 'Event Description Test'
    event_location_test2 = 'Event Location Test 2'
    my_name = 'frank'
    hello = 'hello'
    post_test = 'Post Test'
    item_title_test = 'item titel*7((&*#&@(fefewfewwewg'
    item_description_test1 = '1f5e3w1f5ew1f65we1f56we1f56ew1f53we1f35we1f35wf135ewf13w5ef1e3w5f13w51fw53e1f5we1f35we1f53wef135fwe53few1'
    item_description_test2 = '1f5e3w1f5ew1f65we1f56we1f56ew1f53we1f35we1f35wf135ewf13w5ef1e3w5f13w51fw53e1f5we1f35we1f53wef135fwe53few1'
    item_description_test3 = '1f5e3w1f5ew1f65we1f56we1f56ew1f53we1f35we1f35wf135ewf13w5ef1e3w5f13w51fw53e1f5we1f35we1f53wef135fwe53few1'
    share_test = 'share test'



# Coordinates

class Coordinates:
    #進到活動頁面點選第一個活動
    first_event_x = 330
    first_event_y = 600

    #活度詳細頁返回鍵按鈕
    event_return_button_x =  70
    event_return_button_y =  100

    #建立活動選照片的那個按鈕
    create_event_pick_img_x = 700
    create_event_pick_img_y = 680

    #選取照片第一張的位置
    pick_first_img_x = 90
    pick_first_img_y = 1110

    #event name textfield
    event_name_textfield_x = 100
    event_name_textfield_y = 860

    #鍵盤輸入完成
    keyboard_done_x = 700
    keyboard_done_y = 1120

    #選擇年份日期
    select_date_x = 650
    select_date_y = 280

    #活動地點的輸入框
    event_location_textfield_x = 100
    event_location_textfield_y = 640

    #最大人數
    max_people_x = 320
    max_people_y = 280

    #最大寵物數
    max_pet_x = 280
    max_pet_y = 400

    #活動地點
    event_description_x = 200
    event_description_y = 930

    #我的活動返回鍵
    my_event_leading_button_x = 50
    my_event_leading_button_y = 110

    #編輯活動地點
    edit_location_x = 150
    edit_location_y = 630


# Xpath
class Xpath:
    #存放各Widget的Xpath

    #第一頁的Login按鈕
    login_button_xpath = '//android.widget.Button[@content-desc="Login"]'
    #進入活動頁面
    event_page_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]'

    #點擊詳細頁面的function button
    event_function_button_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button'

    #function_button的檢舉功能
    event_report_xpath = '//android.widget.ImageView[@content-desc="Report"]'

    #檢舉功能裡面的輸入框
    event_report_textfield_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ScrollView/android.widget.EditText'

    #送出檢舉文字
    event_report_send_xpath = '//android.view.View[@content-desc="Send"]'

    #建立活動按鈕
    create_event_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[1]'

    #允許存取照片
    allow_pick_img_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]'

    #選取照片第一張
    pick_first_img_xpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.widget.ImageView[1]'

    #選完照片點擊done
    pick_img_done_xpath = '//android.view.View[@content-desc="Done"]'

    #活動名稱輸入框(before keyborad jump)
    event_name_textfield_xpath = '//android.view.View[@content-desc="10 times left to create events this month Start Time End Time Deadline"]/android.widget.EditText'

    #時間date
    time_date_xpath = '(//android.view.View[@content-desc="Date"])[1]'

    #時間time
    time_time_xpath = '(//android.view.View[@content-desc="Time"])[1]'

    #選擇日期完成
    select_date_done_xpath = '//android.widget.Button[@content-desc="OK"]'

    #建立活動點擊下一頁
    event_nextstep_xpath = '//android.widget.Button[@content-desc="Next Step"]'

    #最大人數
    maximum_people_xpath = '//android.view.View[@content-desc="Type of Event (Cannot be changed) Public (Open to all pet owners) Private (Only invited pet pals)"]/android.view.View[1]'

    #最大寵物數
    maximum_pet_xpath = '//android.view.View[@content-desc="Type of Event (Cannot be changed) Public (Open to all pet owners) Private (Only invited pet pals)"]/android.view.View[2]'

    #選擇人數以及寵物數的done
    create_event_done_button_xpath = '//android.widget.Button[@content-desc="Done"]'

    #活動描述
    event_description_xpath = '//android.view.View[@content-desc="Type of Event (Cannot be changed) Public (Open to all pet owners) Private (Only invited pet pals)"]/android.widget.EditText'

    #建立活動
    create_event_button_xpath = '//android.widget.Button[@content-desc="Create"]'

    #確認建立活動
    confirm_button_xpath = '//android.widget.Button[@content-desc="Confirm"]'

    #知道了
    acknowledge_xpath = '//android.widget.Button[@content-desc="Acknowledge"]'

    #我的活動
    my_event_xpath = '//android.widget.Button[@content-desc="My events"]'

    #編輯活動
    edit_event_xpath = '//android.view.View[@content-desc="Edit"]'

    #編輯活動地點
    edit_event_location_xpath = '//android.view.View[@content-desc="Start Time End Time Deadline"]/android.widget.EditText[2]'

    #點擊左上角收下鍵盤
    leading = '//android.view.View[@content-desc="Edit"]/android.widget.Button[1]'

    #點擊儲存
    event_edit_save = '//android.widget.Button[@content-desc="Save"]'

    #刪除活動
    delete_event = '//android.view.View[@content-desc="Delete"]'

    #確認刪除
    confirm_delete = '//android.widget.Button[@content-desc="Delete"]'

    #按下上一頁
    my_event_leading_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'

    #前往寵群頁面
    group_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[4]'

    #點擊搜尋寵友頁面
    search_friend_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[4]'

    #點擊搜尋寵友
    search_friend = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText'

    #搜尋寵友頁面按下上一頁
    search_friend_page_return = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'

    #進入寵友頁面
    friend_list_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ImageView[3]'

    #點擊輸入框
    friend_list_page_textfield = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'

    #進入到第一個寵友的聊天室
    into_chatroom_with_first_first_friend = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.ImageView[2]'

    #點擊發送圖片
    send_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]'

    #點擊第一張圖片
    send_first_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]/android.view.View/android.widget.ImageView[1]'

    #送出按鈕
    send_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'

    #確認送出
    confirm_send = '//android.widget.Button[@content-desc="Send"]'

    #聊天室輸入框
    chatroom_textfield = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.EditText'

    #聊天室送出訊息
    send_message = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'

    #進入allPost頁面
    into_all_post = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[5]'

    #自己PO文
    post = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button'

    #選取PO文照片
    select_post_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View'

    #點擊輸入框
    post_textfield = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText'

    #po文
    post_done = '//android.view.View[@content-desc="Share"]'

    #進入自己的貼文
    my_post = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ScrollView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView[2]'

    #自己貼文頁面的讚
    my_post_page_like = '//android.view.View[@content-desc="0/150"]/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[1]'

    #點擊留言輸入框
    comment_input_bar = '//android.view.View[@content-desc="0/150"]/android.widget.EditText'

    #進入編輯貼文
    edit_post = '//android.view.View[@content-desc="Edit"]'

    #編輯貼文回到上一頁
    edit_post_return = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]'

    #繼續編輯
    continue_edit = '//android.widget.Button[@content-desc="Continue editing"]'

    #更新貼文
    update_post = '//android.widget.Button[@content-desc="Update Post"]'

    #刪除貼文
    delete_post = '//android.widget.Button[@content-desc="Delete Post"]'

    #進入po照片的頁面
    add_photo_page = '//android.view.View[@content-desc="Tab 3 of 3"]'

    #新增照片的按鈕
    add_photo_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.Button'

    #點擊下一步
    click_next_step = '//android.view.View[@content-desc="Next Step"]'

    #刪除第一張照片
    delete_first_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.widget.ScrollView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView'

    #進入other_post的照片區
    other_post_photo = '//android.view.View[@content-desc="Tab 2 of 2"]'

    #回到首頁
    home_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]'

    #點擊二手物品交易的詳細頁
    exchange_page = '//android.view.View[@content-desc="more"]'

    #建立二手物品
    create_item = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[1]/android.widget.ImageView'

    #二手物品命名
    item_title = '//android.view.View[@content-desc="15 times left to create supplies Shelf Date (No more changes allowed)"]/android.widget.EditText'

    #選取交易日期
    exchange_date = '//android.view.View[@content-desc="Date"]'

    #點選亞洲
    asia = '//android.view.View[@content-desc="Asia"]'

    #點選歐洲
    europe = '//android.view.View[@content-desc="Europe"]'

    #點選非洲
    africa = '//android.view.View[@content-desc="Africa"]'

    #點選北美
    north_america = '//android.view.View[@content-desc="North America"]'

    #點選南美
    south_america = '//android.view.View[@content-desc="South America"]'

    #點選大洋洲
    oceania = '//android.view.View[@content-desc="Oceania"]'

    #點Antarctic
    antarctic = '//android.view.View[@content-desc="Antarctic"]'

    #建立物品->選國家->回上一頁
    back = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.Button[1]'

    #物品種類
    item_category = '//android.view.View[@content-desc="select a category"]'

    #其他種類
    other_category = '//android.widget.RadioButton[@content-desc="other"]'

    #物品說明
    item_description = '//android.view.View[@content-desc="Create Supplies"]/android.view.View/android.view.View/android.widget.EditText'

    #建立物品
    create_item = '//android.widget.Button[@content-desc="Create"]'

    #物品詳細頁的功能按鈕
    item_function_button = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View'

    #編輯物品
    edit_item = '//android.widget.ImageView[@content-desc="Edit"]'

    #選取照片
    select_item_photo = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ScrollView/android.view.View'

    #儲存
    save = '//android.widget.Button[@content-desc="Save"]'

    #點擊分享
    share = '//android.widget.ImageView[@content-desc="Share"]'

    #點擊email
    email = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.TabHost/android.widget.LinearLayout/android.widget.FrameLayout/com.android.internal.widget.ViewPager/android.widget.RelativeLayout/com.android.internal.widget.RecyclerView/android.widget.LinearLayout[3]/android.widget.LinearLayout[3]'

    #點擊subject
    subject = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.EditText'

    #刪除
    delete_item = '//android.widget.ImageView[@content-desc="Delete"]'

    #從我的物品回到上一頁
    back_to_exchange_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.Button'

    #通知頁面
    notification_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.widget.ScrollView/android.widget.ImageView'

    #離開通知頁面
    leave_notification_page = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]'

    #輸入email的欄位
    email_text_field = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.view.View/android.widget.EditText[1]'

    #點擊Sign up
    click_sign_up = '//android.widget.Button[@content-desc="To Sign Up"]'

    #點擊註冊時候的email欄位
    register_email = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[1]'

    #點擊註冊的密碼
    register_pass_wd = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[2]'

    #點擊確認密碼
    enter_passwd_again = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.EditText[3]'

    #我同意
    agree = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.widget.ImageView/android.widget.ScrollView/android.widget.CheckBox'

    #註冊完成
    sign_up_complete = '//android.widget.Button[@content-desc="Sign Up"]'