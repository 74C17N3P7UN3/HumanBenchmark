import os
import time

import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


os.system("cls")
words = []

print("[!] Enter the word and the bot will")
print("[!] automatically click 'Seen' or 'New'")
print("[!] Enter 'EXIT 0' to quit.")

while True:
    word = input("> ")
    if word in words:
        click(885, 510)
    elif word == "EXIT 0":
        break
    else:
        click(1020, 510)
        words.append(word)
    click(1390, 440)
