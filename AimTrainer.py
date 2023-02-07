__author__ = "74C17N3P7UN3"
__version__ = "v1.0.0"
__updated__ = "17/01/2023"

import os
from time import sleep

import customtkinter as ctk
import pyautogui as gui
import win32api
import win32con


class AimTrainer:
    def __init__(self):
        # Set the default UI theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create the root element of the UI
        self.root = ctk.CTk()
        self.root.title("AimTrainer")
        self.root.geometry("330x240")

        # Construct the UI widgets
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill="both")

        self.title = ctk.CTkLabel(master=self.frame, font=("Roboto", 24, "bold"))
        self.description = ctk.CTkLabel(master=self.frame)
        self.button = ctk.CTkButton(master=self.frame, command=None,
                                    fg_color=("#3498DB", "#2980B9"), hover=False)

        # Current phase
        self.phase = [1, False]

        # Program variables
        self.clicks = 0
        self.seconds = 5

        # Files paths
        self.path = ""
        self.target_paths = [
            'assets/aim_trainer/target.png',
            'assets/target.png',
            'target.png'
        ]

    def main(self):
        while True:
            if self.phase[0] == 1:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="AimTrainer")
                    self.title.pack(pady=24, padx=20)
                    self.description.configure(text="Put this window on top\n"
                                                    "and place it out of the way")
                    self.description.pack(pady=12, padx=10)
                    self.button.configure(text=f"Done! (1/3)", command=self.next_phase)
                    self.button.pack(pady=12, padx=10)

                    self.phase[1] = True
            elif self.phase[0] == 2:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Configuration")

                    # Try importing the target
                    for path in self.target_paths:
                        if os.path.exists(path):
                            self.path = path
                            target = gui.locateCenterOnScreen(path, confidence=0.9)
                            if target is not None:
                                self.description.configure(text="Successfully loaded and located\n"
                                                                "the target on the screen, go ahead")
                                self.button.configure(text=f"Done! (2/3)", command=self.next_phase,
                                                      fg_color=("#2ECC71", "#27AE60"))
                            else:
                                self.description.configure(text="Successfully loaded the target, but\n"
                                                                "failed to locate it on the screen. Make\n"
                                                                "sure that you are in the starting page")
                                self.button.configure(text=f"Continue! (2/3)", command=self.next_phase,
                                                      fg_color=("#F39C12", "#E67E22"))

                    # Otherwise, exit the program
                    if self.path == "":
                        self.description.configure(text="Failed to load the target.\n"
                                                        "Make sure that the file exists")
                        self.button.configure(text="Quit (2/2)", command=self.exit,
                                              fg_color=("#E74C3C", "#C0392B"))

                    self.phase[1] = True
            elif self.phase[0] == 3:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Preparation")
                    self.button.configure(text=f"Done! (3/3)", state="disabled")

                    self.phase[1] = True
                # Phase loop
                self.description.configure(text=f"Starting in {self.seconds}s...")
                self.countdown()
            elif self.phase[0] == 4:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Executing")
                    target = gui.locateCenterOnScreen(self.path, confidence=0.9)
                    self.click(target[0], target[1])

                    self.phase[1] = True
                # Phase loop
                self.description.configure(text=f"({self.clicks}/30) Clicks")
                self.function()
            else:
                exit()

            # Update the UI on every cycle
            self.root.update_idletasks()
            self.root.update()

    def countdown(self):
        if self.seconds > 0:
            sleep(1)
            self.seconds -= 1
        else:
            self.next_phase()

    def exit(self):
        self.phase = [5, False]

    def next_phase(self):
        self.phase = [self.phase[0] + 1, False]

    def function(self):
        if self.clicks < 30:
            while True:
                target = gui.locateCenterOnScreen(self.path, confidence=0.9)
                if target is not None:
                    self.click(target[0], target[1])
                    break

            self.clicks += 1

        if self.clicks == 30:
            self.button.configure(state="enabled")

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
    Program = AimTrainer()
    Program.info()
    Program.main()
