import pyautogui

pyautogui.PAUSE=2.0
pyautogui.write('')

for i in range(1,1000):
    pyautogui.write('y')
    pyautogui.PAUSE=0.5
    pyautogui.press('enter')