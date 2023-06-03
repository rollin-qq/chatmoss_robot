import pyautogui
import pyperclip
import random
from pynput import keyboard
from datetime import datetime
import keyboard
import time

from audio_record import record
from audio_play import play
from baidu_ai import audio_to_text, text_to_audio

from PIL import ImageGrab, ImageChops

'''chatmoss_icon.png和chatmoss_enter.png变化了怎么办??？
'''

all_pos = pyautogui.locateAllOnScreen('./wechat_png/chatmoss_icon.png')

time_already_read = datetime.strptime('2022/09/01 00:00:00', '%Y/%m/%d %H:%M:%S')

file = 'test.wav'           # 语音录制，识别文件
synth_file = "synth.mp3"    # 语音合成文
time_list = []
time_area_x_list = []
time_area_y_list = []

enter_pos = pyautogui.locateOnScreen('./wechat_png/chatmoss_enter.png')

# Start the loop
while True:
    if keyboard.is_pressed('esc'):      #按下esc键则退出
        break
    else :
        all_pos = pyautogui.locateAllOnScreen('./wechat_png/chatmoss_icon.png')
        #找到最新的未读过的一条数据
        for pos in all_pos:          
            #获取chatmoss的回复时间
            time_area_x = pos.left
            time_area_y = pos.top
            time_area_width = 90

            time_area_x_list.append(time_area_x)
            time_area_y_list.append(time_area_y)

            pyautogui.moveTo(time_area_x, time_area_y)
            pyautogui.mouseDown()
            pyautogui.moveTo(time_area_x - time_area_width, time_area_y)
            pyautogui.mouseUp()
            pyautogui.hotkey('ctrl', 'c')
            time_str = pyperclip.paste()
            print(time_str[2:])
            time_list.append(datetime.strptime(time_str[2:], '%Y/%m/%d %H:%M:%S'))

        #找出最新的robot回复最新时间，如果大于已读取时间择进行语音合成等后续操作 
                 
        time_latest = max(time_list)
        index_latest = time_list.index(time_latest)

        if time_latest > time_already_read:
            time_already_read = time_latest
            #获取chatmoss的回复内容
            for i, t in enumerate(time_list):
                if t == time_latest:
                    response_area_x = time_area_x_list[index_latest] + 50
                    response_area_y = time_area_y_list[index_latest] + 40

            pyautogui.moveTo(response_area_x, response_area_y) 
            pyautogui.doubleClick()
            #调用API，语音合成，读出文字
            
            robot_response_str=pyperclip.paste()
            print(robot_response_str)
            ret = text_to_audio(synth_file, robot_response_str)    # 语音合成

            if ret != -1:
                play(synth_file)                        # 播放合成结果

            #调用API，语音识别，输入到我的enter栏，点击回车
            record(file)                                # 录制音频 
            res_str = audio_to_text(file  )               # 语音识别
            print(res_str)
            pyperclip.copy(res_str)
            pyautogui.moveTo(enter_pos.left - 50, enter_pos.top - 10)
            pyautogui.click(button='left',clicks=1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

            #====sleep直到屏幕chatmoss无输出后，结束sleep
            # 定义要监测的区域
            WIDTH_CHATMOSS = 600
            HEIGHT_CHATMOSS = 600
            x_chatmoss = enter_pos.left - WIDTH_CHATMOSS
            y_chatmoss = enter_pos.top - HEIGHT_CHATMOSS
            bbox = (x_chatmoss, y_chatmoss, enter_pos.left, enter_pos.top)  #（x1,y1,x2,y2)

            # 截取第一张图像
            im1 = ImageGrab.grab(bbox)

            while True:
                # 等待1秒
                time.sleep(2)
                
                # 截取第二张图像
                im2 = ImageGrab.grab(bbox)
                
                # 计算两张图像的差异
                diff = ImageChops.difference(im1, im2)
                
                # 如果差异为0，则说明两张图像相同
                if diff.getbbox() is None:
                    break

                # 将第二张图像作为下一次比较的基准
                im1 = im2


