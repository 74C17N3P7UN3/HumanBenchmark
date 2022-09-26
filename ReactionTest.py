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
clicks = 0

input("[!] Hit enter to start. ")
print("[$] Executing...")
click(960, 440)

while clicks != 5:
    if pyautogui.pixel(1390, 440)[1] == 219:
        clicks += 1
        for j in range(0, 2):
            click(960, 440)
            time.sleep(0.2)

print("[X] Terminated.")
