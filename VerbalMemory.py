__author__ = "74C17N3P7UN3"
__version__ = "v2.0.0"
__updated__ = "16/01/2023"

import os
from time import sleep

import customtkinter as ctk
import keyboard
import pyautogui as gui
import pytesseract
import win32api
import win32con


class VerbalMemory:
    def __init__(self):
        # Set the default UI theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create the root element of the UI
        self.root = ctk.CTk()
        self.root.title("VerbalMemory")
        self.root.geometry("330x240")

        # Construct the UI widgets
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill="both")

        self.title = ctk.CTkLabel(master=self.frame, font=("Roboto", 24, "bold"))
        self.description = ctk.CTkLabel(master=self.frame)
        self.button = ctk.CTkButton(master=self.frame, command=None,
                                    fg_color=("#3A7EBF", "#1F538D"), hover=False)

        # Current phase
        self.phase = [1, False]

        # Program variables
        self.words = []

        self.corner1 = (0, 0)
        self.corner2 = (0, 0)
        self.seen = (0, 0)
        self.new = (0, 0)

        # Files paths
        self.seen_paths = [
            'assets/verbal_memory/seen.png',
            'assets/seen.png',
            'seen.png'
        ]
        self.new_paths = [
            'assets/verbal_memory/new.png',
            'assets/new.png',
            'new.png'
        ]

    def main(self):
        while True:
            if self.phase[0] == 1:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="VerbalMemory")
                    self.title.pack(pady=24, padx=20)
                    self.description.configure(text="Put this window on top\n"
                                                    "and place it out of the way")
                    self.description.pack(pady=12, padx=10)
                    self.button.configure(text=f"Done! (1/6)", command=self.next_phase)
                    self.button.pack(pady=12, padx=10)

                    self.phase[1] = True
            elif self.phase[0] == 2:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Calibration")
                    self.description.configure(text="Put the cursor on the top-left corner\n"
                                                    "(taking into account the bigger words).\n"
                                                    "After positioning it, hit the 'n' key")
                    self.button.configure(command=None)

                    self.phase[1] = True
                # Phase loop
                self.corner1 = (gui.position().x, gui.position().y)
                self.button.configure(text=f"{self.corner1}")

                if keyboard.is_pressed("n"):
                    self.next_phase()
            elif self.phase[0] == 3:
                # Phase initialization
                if not self.phase[1]:
                    self.button.configure(text=f"Done! (2/6)", command=self.next_phase,
                                          fg_color=("#2CC985", "#2FA572"))

                    self.phase[1] = True
            elif self.phase[0] == 4:
                # Phase initialization
                if not self.phase[1]:
                    self.description.configure(text="Put the cursor on the bottom-right corner\n"
                                                    "(taking into account the bigger words).\n"
                                                    "After positioning it, hit the 'n' key")
                    self.button.configure(command=None, fg_color=("#3A7EBF", "#1F538D"))

                    self.phase[1] = True
                # Phase loop
                self.corner2 = (gui.position().x, gui.position().y)
                self.button.configure(text=f"{self.corner2}")

                if keyboard.is_pressed("n"):
                    self.next_phase()
            elif self.phase[0] == 5:
                # Phase initialization
                if not self.phase[1]:
                    self.button.configure(text=f"Done! (3/6)", command=self.next_phase,
                                          fg_color=("#2CC985", "#2FA572"))

                    self.phase[1] = True
            elif self.phase[0] == 6:
                # Phase initialization
                if not self.phase[1]:
                    # Try importing the 'seen' button
                    for path in self.seen_paths:
                        if os.path.exists(path):
                            btn = gui.locateCenterOnScreen(path, confidence=0.9)
                            if btn is not None:
                                self.description.configure(text="Successfully located the 'seen'\n"
                                                                "button on the screen, go ahead")
                                self.seen = (btn[0], btn[1])
                                self.next_phase()
                    if self.phase[0] != 6:
                        continue

                    # Otherwise, ask for the coordinates
                    self.description.configure(text="Put the cursor on the 'seen'\n"
                                                    "button, then hit the 'n' key")
                    self.button.configure(command=None, fg_color=("#3A7EBF", "#1F538D"))

                    self.phase[1] = True
                # Phase loop
                self.seen = (gui.position().x, gui.position().y)
                self.button.configure(text=f"{self.seen}")

                if keyboard.is_pressed("n"):
                    self.next_phase()
            elif self.phase[0] == 7:
                # Phase initialization
                if not self.phase[1]:
                    self.button.configure(text=f"Done! (4/6)", command=self.next_phase,
                                          fg_color=("#2CC985", "#2FA572"))

                    self.phase[1] = True
            elif self.phase[0] == 8:
                # Phase initialization
                if not self.phase[1]:
                    # Try importing the 'new' button
                    for path in self.new_paths:
                        if os.path.exists(path):
                            btn = gui.locateCenterOnScreen(path, confidence=0.9)
                            if btn is not None:
                                self.description.configure(text="Successfully located the 'new'\n"
                                                                "button on the screen, go ahead")
                                self.new = (btn[0], btn[1])
                                self.next_phase()
                    if self.phase[0] != 8:
                        continue

                    # Otherwise, ask for the coordinates
                    self.description.configure(text="Put the cursor on the 'new'\n"
                                                    "button, then hit the 'n' key")
                    self.button.configure(command=None, fg_color=("#3A7EBF", "#1F538D"))

                    self.phase[1] = True
                # Phase loop
                self.new = (gui.position().x, gui.position().y)
                self.button.configure(text=f"{self.new}")

                if keyboard.is_pressed("n"):
                    self.next_phase()
            elif self.phase[0] == 9:
                # Phase initialization
                if not self.phase[1]:
                    self.button.configure(text=f"Done! (5/6)", command=self.next_phase,
                                          fg_color=("#2CC985", "#2FA572"))

                    self.phase[1] = True
            elif self.phase[0] == 10:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Preparation")
                    self.description.configure(text="Now you can click the button\n"
                                                    "below to start the execution")
                    self.button.configure(text="Execute (6/6)", command=self.next_phase,
                                          fg_color=("#3A7EBF", "#1F538D"))

                    self.phase[1] = True
            elif self.phase[0] == 11:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Executing")
                    self.button.configure(text="Hold 'q' to quit", command=None, state="disabled",
                                          fg_color=("#E74C3C", "#C0392B"))

                    self.phase[1] = True
                # Phase loop
                self.description.configure(text=f"({len(self.words)}) Different words")
                self.function()

                if keyboard.is_pressed("q"):
                    self.next_phase()
            else:
                exit()

            # Update the UI on every cycle
            self.root.update_idletasks()
            self.root.update()

    def function(self):
        image = gui.screenshot(region=(
            self.corner1[0], self.corner1[1],
            self.corner2[0] - self.corner1[0], self.corner2[1] - self.corner1[1]
        ))
        word = pytesseract.image_to_string(image)

        if word in self.words:
            self.click(self.seen[0], self.seen[1])
        else:
            self.words.append(word)
            self.click(self.new[0], self.new[1])

        sleep(0.2)

    def next_phase(self):
        self.phase = [self.phase[0] + 1, False]

    @staticmethod
    def click(x: int, y: int):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

    @staticmethod
    def info():
        print(f"Author: {__author__}")
        print(f"Version: {__version__}")
        print(f"Updated: {__updated__}")


if __name__ == "__main__":
    Program = VerbalMemory()
    Program.info()
    Program.main()
