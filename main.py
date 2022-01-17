import win32com.client as comclt
import pyautogui
from pygame import mixer
from pynput import keyboard
import time

global play
play = False


def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == '-':
        play = True
        return False


while(1):
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

    wsh = comclt.Dispatch("WScript.Shell")
    wsh.AppActivate('''Meeting in "General"''')

    mixer.init()
    mixer.music.load("yes.mp3")
    print("")
    pyautogui.hotkey('ctrl', 'shift', 'm')

    time.sleep(0.5)
    mixer.music.play()
    time.sleep(1)

    pyautogui.hotkey('ctrl', 'shift', 'm')

    play = False
