import pyautogui

#This program for iphone 14 pro max and iphone plus(6.7)
#Do not change simulator position!!!

frankNumberI=18
#移動到註冊頁面

for frankNumber in range(frankNumberI,19):
    
    pyautogui.click(1631,912,clicks=2,interval=0.2,duration=0.2)
    pyautogui.PAUSE=0.3

    #鼠標移動到電子郵件
    pyautogui.moveTo(1554,356)
    pyautogui.PAUSE=0.5
    pyautogui.click(clicks=2,interval=0.2,duration=0.2)
    pyautogui.write('frank.chen+23@keeda.com.tw')
    #密碼
    pyautogui.click(1554,431,clicks=2,interval=0.2,duration=0.2)
    pyautogui.write('aPPLEPLOKM123')

    #確認密碼
    pyautogui.click(1554,536,clicks=2,interval=0.2,duration=0.2)
    pyautogui.write('aPPLEPLOKM123')

    pyautogui.click(1536,756) # 同意隱私及服務條款

    pyautogui.PAUSE=0.3

    pyautogui.click(1678,821,clicks=2,interval=0.2,duration=0.2)#按下註冊

    pyautogui.PAUSE=5#等待註冊頁面->驗證信頁面

    pyautogui.moveTo(1679,650)#按下送出
    pyautogui.click(clicks=2,interval=0.2,duration=0.2)
    pyautogui.PAUSE=3
    pyautogui.click(149,741,clicks=2,interval=0.2,duration=0.2)#點擊gmail空白處
    pyautogui.PAUSE=0.1
    pyautogui.click(81,82,clicks=2,interval=0.1,duration=0.2)#點擊重置頁面

    pyautogui.PAUSE=5 #等待網頁重置
    pyautogui.moveTo(444,723)#點擊驗證碼
    pyautogui.click(clicks=2,interval=0.1,duration=0.2)
    pyautogui.PAUSE=0.1



    #點擊驗證碼並且關閉目前分頁
    pyautogui.keyDown('command')
    pyautogui.press('w')
    pyautogui.keyUp('command')


    pyautogui.click(1545,828,clicks=2,interval=0.1,duration=0.2) #返回登入

    pyautogui.PAUSE=2
    #pyautogui.click(1507,424)#輸入帳號
    pyautogui.moveTo(1562,402)
    pyautogui.click(clicks=2,interval=0.1,duration=0.2)
    pyautogui.PAUSE=0.5
    pyautogui.write('frank.chen+23@keeda.com.tw')
    pyautogui.click(1562,495,clicks=2,interval=0.1,duration=0.2)#輸入密碼
    pyautogui.write('aPPLEPLOKM123')


    pyautogui.click(1685,596,clicks=2,interval=0.1,duration=0.2)#登入
    pyautogui.PAUSE=2

    pyautogui.click(1596,590,clicks=3,interval=0.2,duration=0.2)#我是男森
    pyautogui.PAUSE=1
    pyautogui.click(1722,376,clicks=2,interval=0.1,duration=0.2)#點擊頭像
    pyautogui.click(1688,428,clicks=2,interval=0.1,duration=0.2)#選擇圖片
    pyautogui.click(1810,864)#下一步

    #依序選擇興趣:健行 露營 跑步 瑜伽 攝影
    pyautogui.PAUSE=0.1
    pyautogui.click(1534,425,duration=0.2)
    for i in range(0,4):
        pyautogui.moveRel(60,0)
        pyautogui.click()
    pyautogui.click(1810,864,duration=0.2)#按下一步

    pyautogui.PAUSE=1

    pyautogui.click(1542,322,clicks=2,interval=0.3,duration=0.2)#點擊寵物名字
    pyautogui.write('dog')
    pyautogui.click(1535,405,duration=0.2)#點擊寵物生日
    pyautogui.click(1777,833,duration=0.2)#點擊生日年份
    pyautogui.dragTo(1777,878,button='left')#把生日往前調一年
    pyautogui.click(1852,729,duration=0.2)#done
    pyautogui.click(1553,529,duration=0.2)#點擊寵物種類
    pyautogui.click(1800,859,duration=0.2)#下一步

    pyautogui.click(1556,421,duration=0.2)#選擇米克斯
    pyautogui.PAUSE=5
    pyautogui.click(1812,863,duration=0.2)#下一步
    
    pyautogui.click(1846,904,duration=0.2)#按下設定
    pyautogui.PAUSE=2
    pyautogui.click(1851,366,duration=0.2)#進入個人資料
    pyautogui.click(1725,368,clicks=2,interval=0.2,duration=0.2)#點擊修改暱稱
    pyautogui.PAUSE=0.1
    for i in range(0,15):
        pyautogui.press('backspace')#刪除原本的id
    pyautogui.PAUSE=1
    pyautogui.write('frank23')
    pyautogui.moveTo(1703,824,duration=0.2)#儲存
    pyautogui.click()
