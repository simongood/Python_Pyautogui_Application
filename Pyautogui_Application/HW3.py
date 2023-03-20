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

# 畫樹
pyautogui.moveTo(1250, 358, 0.1)
pyautogui.dragTo(1070, 500, 2)
pyautogui.dragTo(1242, 498, 2)
pyautogui.dragTo(1005, 625, 2)
pyautogui.dragTo(1189, 655, 2)
pyautogui.dragTo(825, 782, 2)
pyautogui.dragTo(1201, 799, 2)
pyautogui.dragTo(1184, 988, 2)
pyautogui.dragTo(1292, 984, 2)
pyautogui.dragTo(1292, 800, 2)
pyautogui.dragTo(1465, 801, 2)
pyautogui.dragTo(1286, 676, 2)
pyautogui.dragTo(1456, 660, 2)
pyautogui.dragTo(1312, 520, 2)
pyautogui.dragTo(1401, 498, 2)
pyautogui.dragTo(1245, 358, 2)