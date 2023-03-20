import pyautogui
import time

# 開啟小畫家
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'm')
pyautogui.click(592, 1063)
time.sleep(1)

# 畫圓圈
pyautogui.click(501, 79)
pyautogui.moveTo(159, 419, 0.1)
pyautogui.keyDown('shift')
pyautogui.dragTo(395, 248, 1)
pyautogui.keyUp('shift')

# 畫方塊
pyautogui.click(522, 75)
pyautogui.moveTo(220, 351, 0.1)
pyautogui.keyDown('shift')
pyautogui.dragTo(265, 307, 1)
pyautogui.keyUp('shift')

# 著色
pyautogui.click(328, 91)
time.sleep(1)
pyautogui.doubleClick(1000, 101)
pyautogui.click(266, 290)

# 選取縮小複製，移到適當位置
pyautogui.click(153, 128)
pyautogui.click(177, 205)
pyautogui.moveTo(146, 231)
pyautogui.dragTo(342, 434)
pyautogui.moveTo(340,231)
pyautogui.dragTo(215, 365, 1)
pyautogui.click(85, 74)

# 迴圈複製
xcnt = 1
ycnt = 1
xp = 179
yp = 295
while ycnt <= 6:
    if xcnt <= 6:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.moveTo(41, 220)
        pyautogui.dragTo(xp, yp, 0.2)
        xp = xp + 116
        xcnt = xcnt + 1
    else:
        yp = yp + 122
        ycnt = ycnt + 1
        xcnt = 1
        xp = 179
        continue