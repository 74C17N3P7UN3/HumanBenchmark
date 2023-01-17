__author__ = "74C17N3P7UN3"
__version__ = "v2.0.1"
__updated__ = "16/01/2023"

from time import sleep

import customtkinter as ctk
import pyautogui as gui
import win32api
import win32con


class Typing:
    def __init__(self):
        # Set the default UI theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create the root element of the UI
        self.root = ctk.CTk()
        self.root.title("Typing")
        self.root.geometry("360x300")

        # Construct the UI widgets
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill="both")

        self.title = ctk.CTkLabel(master=self.frame, font=("Roboto", 24, "bold"))
        self.description = ctk.CTkLabel(master=self.frame)
        self.input = ctk.CTkTextbox(master=self.frame, height=50)
        self.button = ctk.CTkButton(master=self.frame, command=None,
                                    fg_color=("#3A7EBF", "#1F538D"), hover=False)

        # Current phase
        self.phase = [1, False]

        # Program variables
        self.seconds = 5
        self.phrase = ""

    def main(self):
        while True:
            if self.phase[0] == 1:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Typing")
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
                    self.title.configure(text="Input")
                    self.description.configure(text="Input the phrase to\n"
                                                    "type in box below")
                    self.input.pack(pady=12, padx=10)
                    self.button.configure(text=f"Done! (2/3)", command=self.next_phase)
                    self.button.pack_forget()
                    self.button.pack(pady=12, padx=10)

                    self.phase[1] = True
                # Phase loop
                self.phrase = self.input.get("1.0", "end-1c").replace("\n", " ")
            elif self.phase[0] == 3:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Preparation")
                    self.input.pack_forget()
                    self.button.configure(text=f"Done! (3/3)", state="disabled")

                    self.phase[1] = True
                # Phase loop
                self.description.configure(text=f"Focus the input box\n"
                                                f"Starting in {self.seconds}s...")

                self.countdown()
            elif self.phase[0] == 4:
                # Phase initialization
                if not self.phase[1]:
                    self.title.configure(text="Executing")
                    self.description.configure(text="Written!")
                    self.button.configure(state="enabled", require_redraw=True)

                    gui.write(self.phrase)

                    self.phase[1] = True
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
    Program = Typing()
    Program.info()
    Program.main()
