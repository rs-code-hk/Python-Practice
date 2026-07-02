import pynput

def onPress(key):
    print(key)

with pynput.keyboard.Listener(
    on_press=onPress()
)