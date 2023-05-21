import os

def play(file_name):
    """audio play"""
    os.system(f"ffplay -autoexit {file_name}")		#播放完毕自动退出



# import Play_mp3

# def play(file_name):
#     """audio play"""
#     Play_mp3.play(file_name)


'''
# 如果您尚未安装 `pydub` 库，请在命令行中使用以下命令进行安装：

# ```
# pip install pydub
# ```

# 请注意，`pydub` 库需要 FFmpeg 多媒体框架支持才能正常工作，因此还需要安装 FFmpeg。可以在 FFmpeg 官网（https://ffmpeg.org/）
# 下载适用于您所使用操作系统的安装包并进行安装。安装完成后，请将 FFmpeg 的 bin 目录添加到系统的环境变量中，以确保 `pydub` 库可以找到并使用 FFmpeg。
# '''
# from pydub import AudioSegment
# from pydub.playback import play as pb_play

# def play(file_name):
#     """audio play"""
#     sound = AudioSegment.from_file(file_name)
#     pb_play(sound)



# import pygame

# def play(file_name):
#     """audio play"""
#     pygame.init()
#     pygame.mixer.music.load(file_name)
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)
#     pygame.quit()

# from playsound import playsound

# def play(file_name):
#     """audio play"""
#     playsound(file_name)
