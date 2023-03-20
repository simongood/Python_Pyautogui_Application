import pyautogui
import time

# 開啟網頁
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'm')
pyautogui.doubleClick(157, 43)
time.sleep(1)
pyautogui.click(1150, 320)
pyautogui.typewrite('https://www.geogebra.org/classic',0)
pyautogui.press('enter')
time.sleep(2)

# 點手寫筆
pyautogui.click(43, 180)
pyautogui.click(60, 458)

# 畫三角
pyautogui.moveTo(1280, 448, 0.1)
pyautogui.dragTo(1042, 628, 1)
pyautogui.dragTo(1556, 660, 2)
pyautogui.dragTo(1280, 448, 0.5)