'''百度语音识别SDK调用
'''
#pip install pyttsx3,PyAudio,chardet。pyaudio安装报错，解决办法：https://blog.csdn.net/weixin_38369492/article/details/125992255。
import pyttsx3

#pip install SpeechRecognition
import speech_recognition as sr
# pip install baidu-aip
from aip import AipSpeech                   

# Baidu Speech API, replace with your personal key
APP_ID = '33337135 '
API_KEY = 'dVkH1EFPFrRC8lTtmMKpY4re'            #根据说明文档，在百度智能云后台获取
SECRET_KEY = '4WDkN6sFRubPwBOptETsp0G0mNUGblRm'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# Use SpeechRecognition to record
try:
    def rec(rate=16000):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=rate) as source:
            print("请说话")
            audio = r.listen(source)

        with open("recording.wav", "wb") as f:
            f.write(audio.get_wav_data())
except:
    print("语音录入发生错误")


# 使用百度语音作为STT引擎
def listen():
    with open('recording.wav', 'rb') as f:
        audio_data = f.read()

        result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1536,
    })
        try:
            result_text = result["result"][0]
            print("你说: " + result_text)


            if result_text =="阿龙":
                engine = pyttsx3.init()
                engine.say('真帅')
                engine.runAndWait()
            elif result_text=="其他人":
                engine = pyttsx3.init()
                engine.say('真难看')
                engine.runAndWait()
        except:
            print("没有识别到语音")


while True:
    rec()
    request = listen()