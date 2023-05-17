#####
#    点击鼠标左键，确定鼠标坐标；按鼠标右键，退出
#####

from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        print(f"鼠标当前坐标：({x}, {y})")
    #点击右键退出
    if pressed and button == mouse.Button.right:
        return False

# 监听鼠标点击事件
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
