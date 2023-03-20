import pyautogui
import time

# 開啟網頁(螢幕縮放110%)
pyautogui.PAUSE = 0.5
pyautogui.hotkey('win', 'm')
pyautogui.doubleClick(157, 43)
time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'N')
pyautogui.hotkey('alt', 'space', 'X')
pyautogui.typewrite('https://www.crazygames.com/game/tower-swap', 0)
pyautogui.press('enter')
time.sleep(2)


# 設定function"向左"、"向右移"、判斷教學、判斷代號
def judge(X, Y):  # 判斷教學出現並且點過教學
    pos = X, Y
    count = 0
    while pyautogui.screenshot().getpixel(pos) == (5, 32, 62):
        if count == 2:
            break
        pyautogui.click(X, Y)
        time.sleep(1)
        count = count + 1
        continue


def moveR(X, Y):
    pyautogui.moveTo(X, Y)
    pyautogui.dragTo(X + 63, Y, 0.5)
    judge(1166, 295)


def moveL(X, Y):
    pyautogui.moveTo(X, Y)
    pyautogui.dragTo(X - 63, Y, 0.5)
    judge(1166, 295)


def dist(code, X, Y, R, G, B, x, y):  # 判斷代號
    pos = X, Y
    c = pyautogui.screenshot().getpixel(pos)
    if R - 12 <= c[0] <= R + 12 and G - 12 <= c[1] <= G + 12 and B - 12 <= c[2] <= B + 12:
        list[y][x] = code


def dif(code, y):  # 判斷三個並移動一次
    cnt1 = 0
    xcnt1 = 0
    L = [0, 0, 0, 0, 0, 0]
    global move
    while xcnt1 <= 5:
        if list[y][xcnt1] == code:
            cnt1 = cnt1 + 1
            L[xcnt1] = 1
        xcnt1 = xcnt1 + 1
    if cnt1 == 3:
        move = 1
        if L == [1, 1, 0, 1, 0, 0]:
            moveL(731, 380 + y * 66)
        elif L == [1, 1, 0, 0, 1, 0]:
            moveL(797, 380 + y * 66)
            moveL(731, 380 + y * 66)
        elif L == [1, 1, 0, 0, 0, 1]:
            moveL(863, 380 + y * 66)
            moveL(797, 380 + y * 66)
            moveL(731, 380 + y * 66)
        elif L == [0, 1, 1, 0, 1, 0]:
            moveL(797, 380 + y * 66)
        elif L == [0, 1, 1, 0, 0, 1]:
            moveL(863, 380 + y * 66)
            moveL(797, 380 + y * 66)
        elif L == [1, 0, 1, 1, 0, 0]:
            moveR(533, 380 + y * 66)
        elif L == [0, 0, 1, 1, 0, 1]:
            moveL(863, 380 + y * 66)
        elif L == [1, 0, 0, 1, 1, 0]:
            moveR(533, 380 + y * 66)
            moveR(599, 380 + y * 66)
        elif L == [0, 1, 0, 1, 1, 0]:
            moveR(599, 380 + y * 66)
        elif L == [1, 0, 0, 0, 1, 1]:
            moveR(533, 380 + y * 66)
            moveR(599, 380 + y * 66)
            moveR(665, 380 + y * 66)
        elif L == [0, 1, 0, 0, 1, 1]:
            moveR(599, 380 + y * 66)
            moveR(665, 380 + y * 66)
        elif L == [0, 0, 1, 0, 1, 1]:
            moveR(665, 380 + y * 66)
        else:
            move = 0

# 按 play 玩新手教學
pyautogui.PAUSE = 2
pyautogui.click(1074, 657)
time.sleep(2)
pyautogui.click(704, 760)  # PLAY
time.sleep(3)
moveR(667, 585)  # 石頭
time.sleep(3)
judge(1166, 295)
moveL(730, 582)  # 金礦
pyautogui.click(667, 590)  # 點寶箱
judge(1166, 295)
moveR(600, 580)

# 代號
'''
石頭      = 1  (71, 97, 112)  =>  城堡(灰) = 6      (166, 204, 206)
水晶(藍)  = 2  (221, 231, 219) =>  城牆(藍) = 7     (35, 167, 167)
木材      = 3  (70, 65, 58)   =>  驽       = 8     (74, 52, 33)
礦(黃)    = 4  (113, 101, 46)   =>  寶箱     = 9    (201, 142, 16)
砲彈      = 5  (59, 54, 53)   =>  大砲     = 10     (247, 248, 250) (129, 121, 108)
'''

# 判斷一次完整盤面
list = [[0] * 6 for _ in range(6)]  # 設定盤面list
xcnt = 0
ycnt = 0
xpos = 533
ypos = 380
while ycnt < 6:
    if xcnt < 6:
        dist(1, xpos, ypos, 71, 97, 122, xcnt, ycnt)
        dist(2, xpos, ypos, 221, 231, 219, xcnt, ycnt)
        dist(3, xpos, ypos, 70, 65, 58, xcnt, ycnt)
        dist(4, xpos, ypos, 113, 101, 46, xcnt, ycnt)
        dist(5, xpos, ypos, 59, 54, 53, xcnt, ycnt)
        dist(6, xpos, ypos, 166, 204, 206, xcnt, ycnt)
        dist(7, xpos, ypos, 35, 167, 167, xcnt, ycnt)
        dist(8, xpos, ypos, 74, 52, 33, xcnt, ycnt)
        dist(9, xpos, ypos, 201, 142, 16, xcnt, ycnt)
        dist(10, xpos, ypos, 247, 248, 250, xcnt, ycnt)
        dist(10, xpos, ypos, 129, 121, 108, xcnt, ycnt)
        xcnt = xcnt + 1
        xpos = xpos + 66
    else:
        ycnt = ycnt + 1
        xcnt = 0
        ypos = ypos + 66
        xpos = 533
print(list)

# 判斷哪裡有三個一樣的並連線一次
ycnt = 0
type = 1
move = 0
while ycnt <= 5:
    while type <= 10:
        dif(type, ycnt)
        type = type + 1
    ycnt = ycnt + 1
    type = 1
    if move == 1:
        break

# 玩到死並點廣告
pyautogui.PAUSE = 1
pos = 652, 253
j = 1166, 295
while pyautogui.screenshot().getpixel(pos) == (227, 4, 4):  # 玩到死
    moveR(863, 380)
    if pyautogui.screenshot().getpixel(j) == (15, 40, 83): # 飛龍畫面
        pyautogui.click(j)
        time.sleep(8)
    elif pyautogui.screenshot().getpixel(j) == (4, 25, 49): # 國王畫面
        pyautogui.click(j)

if pyautogui.screenshot().getpixel(j) == (4, 25, 49):   #按廣告
    pyautogui.click(j)
    pyautogui.moveTo(702, 600, 0.2)
    pyautogui.dragTo(702, 600, 0.2)
    time.sleep(10)
    pyautogui.click(709, 839)
    pyautogui.click(691, 696)

time.sleep(2)
while pyautogui.screenshot().getpixel(pos) == (227, 4, 4):  # 在玩一次到到死
    moveR(863, 380)
    if pyautogui.screenshot().getpixel(j) == (15, 40, 38):
        time.sleep(8)
time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.keyUp('alt')
