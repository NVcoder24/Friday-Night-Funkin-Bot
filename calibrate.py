from pynput import mouse

class MyException(Exception): pass

def on_click(x, y, button, pressed):
    if pressed == True:
        if button == mouse.Button.left:
            print(x - 1920, y)

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()