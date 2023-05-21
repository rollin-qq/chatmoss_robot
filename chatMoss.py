import pyautogui
import pyperclip
import random
from pynput import keyboard
from datetime import datetime, time
import keyboard

from audio_record import record
from audio_play import play
from baidu_ai import audio_to_text, text_to_audio


'''chatmoss_icon.png和chatmoss_enter.png变化了怎么办??？
'''

all_pos = pyautogui.locateAllOnScreen('./wechat_png/chatmoss_icon.png')

time_latest = datetime.strptime('2022/09/01 00:00:00', '%Y/%m/%d %H:%M:%S')

file = 'test.wav'           # 语音录制，识别文件
synth_file = "synth.mp3"    # 语音合成文

# Start the loop
while True:
    if keyboard.is_pressed('esc'):      #按下esc键则退出
        break
    else :
        all_pos = pyautogui.locateAllOnScreen('./wechat_png/chatmoss_icon.png')
        enter_pos = pyautogui.locateOnScreen('./wechat_png/chatmoss_enter.png')
        for pos in all_pos:
            #获取chatmoss的回复时间
            time_area_x = pos.left + 40
            time_area_y = pos.top + 5
            time_area_width = 200

            pyautogui.moveTo(time_area_x, time_area_y)
            pyautogui.mouseDown()
            pyautogui.moveTo(time_area_x + time_area_width, time_area_y)
            pyautogui.mouseUp()
            pyautogui.hotkey('ctrl', 'c')
            time_str = pyperclip.paste()
            #如果一动鼠标滚轮，time_str则会拷贝到错误信息，怎么办？？？？
            time_obj = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
            #如果时间比上次最新的还新，则执行后续动作，否则什么也不做。
            if time_obj > time_latest:
                time_latest = time_obj
                #获取chatmoss的回复内容
                response_area_x = pos.left + 100
                response_area_y = pos.top + 42

                pyautogui.moveTo(response_area_x, response_area_y) 
                pyautogui.doubleClick()
                #调用API，语音合成，读出文字
                robot_response_str=pyperclip.paste()
                ret = text_to_audio(synth_file, robot_response_str)    # 语音合成

                if ret != -1:
                    play(synth_file)                        # 播放合成结果

                #调用API，语音识别，输入到我的enter栏，点击回车（不要等读完，只要有语音输入则执行）
                record(file)                                # 录制音频 
                res_str = audio_to_text(file)               # 语音识别
                pyautogui.moveTo(enter_pos.left + 100, enter_pos.top)
                pyautogui.click(button='left',clicks=1)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('enter')


