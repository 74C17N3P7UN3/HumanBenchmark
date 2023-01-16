__author__ = "74C17N3P7UN3"
__version__ = "v2.1.3"
__updated__ = "16/01/2023"

from time import sleep

import customtkinter as ctk
import keyboard
import pyautogui as gui
import win32api
import win32con


class ReactionTime:
    def __init__(self):
        # Set the default UI theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create the root element of the UI
        self.root = ctk.CTk()
        self.root.title("ReactionTime")
        self.root.geometry("360x225")

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
        self.position = (0, 0)
        self.color = (0, 0, 0)

        self.clicks = 0

    def main(self):
        while True:
            if self.phase[0] == 1:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="ReactionTime")
                    self.title.pack(pady=24, padx=20)
                    self.description.configure(text="Put this window on top\n"
                                                    "and place it out of the way")
                    self.description.pack(pady=12, padx=10)
                    self.button.configure(text=f"Done! (1/4)", command=self.next_phase)
                    self.button.pack(pady=12, padx=10)

                    self.phase[1] = True
            elif self.phase[0] == 2:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Calibration")
                    self.description.configure(text="Wait for the green and place the cursor\n"
                                                    "on a green pixel, then hit the 'n' key")
                    self.button.configure(command=None)

                    self.phase[1] = True
                # Phase loop
                self.position = (gui.position().x, gui.position().y)
                self.color = gui.pixel(self.position[0], self.position[1])
                self.button.configure(text=f"{self.position}")

                if keyboard.is_pressed("n"):
                    self.next_phase()
            elif self.phase[0] == 3:
                # Phase initialization
                if not self.phase[1]:
                    self.button.configure(text=f"Done! (2/4)", command=self.next_phase,
                                          fg_color=("#2CC985", "#2FA572"))

                    self.phase[1] = True
            elif self.phase[0] == 4:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Preparation")
                    self.description.configure(text="Refresh the page, click the button\n"
                                                    "below and manually start the test")
                    self.button.configure(text="Execute (3/4)", command=self.next_phase,
                                          fg_color=("#3A7EBF", "#1F538D"))

                    self.phase[1] = True
            elif self.phase[0] == 5:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Executing")
                    self.button.configure(text="Done! (4/4)", command=self.next_phase, state="disabled")

                    self.phase[1] = True
                # Phase loop
                self.description.configure(text=f"({self.clicks}/5) Clicks")
                self.function()
            else:
                exit()

            # Update the UI on every cycle
            self.root.update_idletasks()
            self.root.update()

    def function(self):
        if gui.pixel(self.position[0], self.position[1]) == self.color and self.clicks < 5:
            self.clicks += 1
            for _ in range(0, 2):
                self.click(self.position[0], self.position[1])
                sleep(0.5)

        if self.clicks == 5:
            self.button.configure(state="enabled")

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
    Program = ReactionTime()
    Program.info()
    Program.main()
