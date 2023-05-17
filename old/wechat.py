import pyautogui
import pyperclip
import random

all_pos = pyautogui.locateAllOnScreen('./wechat_png/dot2.png')

print(list(all_pos))

msg_list = [
    '你好',
    '李二傻',
    '不错',
    '怎了啦'
]

try:
    while True:
        all_pos = pyautogui.locateAllOnScreen('./wechat_png/dot2.png')
        for pos in all_pos:
            pyautogui.moveTo(pos.left,pos.top)
            pyautogui.click(button='left',clicks=1,interval=0.25)

            msg = random.choice(msg_list)
            pyperclip.copy(msg)
            pyautogui.hotkey('ctrl','v')
            pyautogui.press('enter')
except KeyboardInterrupt:
    print('\n')
