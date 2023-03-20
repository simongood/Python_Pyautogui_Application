import pyautogui
import time

# 開啟powerpo
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'm')
pyautogui.click(592, 1063)
time.sleep(1)

# 畫旗桿與藍色部分
pyautogui.click(451, 77)
pyautogui.moveTo(919,78)
pyautogui.click(919, 78)
pyautogui.moveTo(430, 813)
pyautogui.dragTo(430, 292)

pyautogui.click(528, 76)
pyautogui.click(666, 105)
pyautogui.click(694, 166)
pyautogui.click(1085, 76)
pyautogui.click(848, 106)
pyautogui.moveTo(1085, 76)
pyautogui.click(1085, 76)
pyautogui.moveTo(434, 292, 0.5)
pyautogui.dragTo(779, 519)

# 畫紅色部分
pyautogui.click(1166, 607)
pyautogui.moveTo(971, 80)
pyautogui.click(971, 80)
pyautogui.click(800, 90)
pyautogui.moveTo(971, 80)
pyautogui.click(971, 80)

r = 0
yr = 292
while r < 4:
    pyautogui.moveTo(784, yr)
    pyautogui.dragTo(1158, yr+32)
    yr = yr + 64
    r = r + 1
while r < 7:
    pyautogui.moveTo(434, yr)
    pyautogui.dragTo(1158, yr+32)
    yr = yr + 64
    r = r + 1

# 畫星星
pyautogui.click(497, 125)
pyautogui.moveTo(889, 106)
pyautogui.click(889, 106)
pyautogui.click(851, 102)
pyautogui.moveTo(889, 106)
pyautogui.click(889, 106)

xs = 453
ys = 324
xcnt = 0
ycnt = 0
while ycnt < 5:
    if xcnt < 6:
        pyautogui.moveTo(xs, ys)
        pyautogui.dragTo(xs+25, ys-21)
        xcnt = xcnt + 1
        xs = xs + 57
    else:
        ys = ys + 46
        xs = 453
        ycnt = ycnt + 1
        xcnt = 0
else:
    xs = 481
    ys = 342

while ycnt < 9:
    if xcnt < 5:
        pyautogui.moveTo(xs, ys)
        pyautogui.dragTo(xs+25, ys-21)
        xcnt = xcnt + 1
        xs = xs + 57
    else:
        ys = ys + 46
        xs = 481
        ycnt = ycnt + 1
        xcnt = 0
