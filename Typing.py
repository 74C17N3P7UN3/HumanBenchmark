import os
import time

import pyautogui
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


os.system("cls")
text = ""

print("[!] Paste the message, then hit enter.")
print("[!] Finally, CTRL+C to start typing.")
print("> ", end="")

try:
    while True:
        try:
            line = input()
        except EOFError:
            break
        text += " " + line
except KeyboardInterrupt:
    text = text[1:]

print("\n[$] Executing...")
click(960, 440)
time.sleep(0.5)
pyautogui.write(text)
print("[X] Terminated.")
