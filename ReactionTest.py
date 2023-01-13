from time import sleep

import customtkinter as ctk
import keyboard
import pyautogui as gui
import win32api
import win32con


class ReactionTest:
    def __init__(self):
        # Set the default UI theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Create the root element of the UI
        self.root = ctk.CTk()
        self.root.title("ReactionTest")
        self.root.geometry("360x225")

        # Construct the UI widgets
        self.frame = ctk.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=40, fill="both")

        self.title = ctk.CTkLabel(master=self.frame, font=("Roboto", 24, "bold"))
        self.title.pack(pady=24, padx=20)
        self.description = ctk.CTkLabel(master=self.frame)
        self.description.pack(pady=12, padx=10)
        self.button = ctk.CTkButton(master=self.frame, command=lambda: None,
                                    fg_color=("#3A7EBF", "#1F538D"), hover=False)
        self.button.pack(pady=12, padx=10)

        # Index of the current displayed phase
        self.phase = 1

        # Program variables
        self.position = (0, 0)
        self.color = (0, 0, 0)

        self.clicks = 0

    def main(self):
        while True:
            if self.phase == 1:
                self.title.configure(text="ReactionTest")
                self.description.configure(text="Put this window on top\n"
                                                "and place it out of the way")
                self.button.configure(text=f"Done! (1/4)", command=self.next_phase)
            elif self.phase == 2:
                self.position = (gui.position().x, gui.position().y)
                self.color = gui.pixel(self.position[0], self.position[1])

                self.title.configure(text="Calibration")
                self.description.configure(text="Wait for the green and place the cursor\n"
                                                "on a green pixel, then hit the 'c' key")
                self.button.configure(text=f"{self.position}", command=None)

                if keyboard.is_pressed("c"):
                    self.next_phase()
            elif self.phase == 3:
                self.button.configure(text=f"Done! (2/4)", command=self.next_phase, fg_color=("#2CC985", "#2FA572"))
            elif self.phase == 4:
                self.title.configure(text="Preparation")
                self.description.configure(text="Refresh the page and click the\n"
                                                "button below to start the execution")
                self.button.configure(text="Execute (3/4)", command=self.next_phase, fg_color=("#3A7EBF", "#1F538D"))
            elif self.phase == 5:
                self.title.configure(text="Executing")
                if self.clicks == 0:
                    self.description.configure(text="Please start the test")
                else:
                    self.description.configure(text=f"({self.clicks}/5) Clicks")
                self.button.configure(text="Done! (4/4)", command=self.next_phase, state="disabled")

                self.function()
            else:
                exit()

            # Update the UI on every cycle
            self.root.update_idletasks()
            self.root.update()

    def function(self):
        if gui.pixel(self.position[0], self.position[1]) == self.color:
            self.clicks += 1
            for _ in range(0, 2):
                self.click(self.position[0], self.position[1])
                sleep(0.5)

        if self.clicks == 5:
            self.button.configure(state="enabled", require_redraw=True)

    def next_phase(self):
        self.phase += 1

    @staticmethod
    def click(x: int, y: int):
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


if __name__ == "__main__":
    ReactionTest = ReactionTest()
    ReactionTest.main()
