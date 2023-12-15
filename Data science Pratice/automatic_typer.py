from pynput import keyboard
from tkinter import Tk

def paste_text():
    text = Tk().clipboard_get()
    for char in text:
        keyboard.Controller().press(char)
        keyboard.Controller().release(char)
    
def on_press(key):
    try:
        if key == keyboard.Key.ctrl_l:
            global ctrl_pressed
            ctrl_pressed = True

        elif key.char == 's':
            paste_text()
            exit(-1)

        elif key.char == '`':
            exit(-1)

    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.ctrl_l:
        global ctrl_pressed
        ctrl_pressed = False

ctrl_pressed = False
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()



