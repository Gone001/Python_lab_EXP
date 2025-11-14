
import tkinter as tk
from datetime import datetime
import pytz

class TimeZoneApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Welcome App")
        self.window.geometry("460x400")
        self.window.configure(bg="#e8eaf6")  

       
        self.input_frame = tk.Frame(window, bg="#e8eaf6")
        self.input_frame.pack(expand=True)

        self.prompt_label = tk.Label(self.input_frame, text="Please enter your name:", 
                                     font=("Segoe UI", 13), bg="#e8eaf6", fg="#333")
        self.prompt_label.pack(pady=18)

        self.name_input = tk.Entry(self.input_frame, font=("Segoe UI", 13), width=25, relief="solid", bd=2)
        self.name_input.pack(ipady=4, pady=10)

        self.submit_btn = tk.Button(self.input_frame, text="Enter", font=("Segoe UI", 12, "bold"),
                                   bg="#43a047", fg="white", relief="flat", padx=28, pady=6,
                                   activebackground="#357a38", activeforeground="white",
                                   cursor="hand2", command=self.display_welcome)
        self.submit_btn.pack(pady=16)

    def display_welcome(self):
        user_name = self.name_input.get().strip()
        if not user_name:
            self.prompt_label.config(text="Name cannot be empty!", fg="#d32f2f")
            return

        
        self.input_frame.pack_forget()

        
        welcome_section = tk.Frame(self.window, bg="#e8eaf6")
        welcome_section.pack(expand=True, fill="both")

        welcome_text = f"Welcome, {user_name}!"
        welcome_label = tk.Label(welcome_section, text=welcome_text,
                                 font=("Segoe UI", 17, "bold italic"),
                                 fg="#1b5e20", bg="#e8eaf6")
        welcome_label.pack(side="bottom", pady=54)

        
        tz_frame = tk.Frame(welcome_section, bg="#e8eaf6")
        tz_frame.pack(side="bottom")

        separator = tk.Frame(tz_frame, height=2, bd=0, bg="#8c9eff")
        separator.pack(fill="x", pady=(0,10))

        locations = [
            ("Australia", "Australia/Sydney"),
            ("USA", "America/New_York"),
            ("China", "Asia/Shanghai"),
            ("India", "Asia/Kolkata"),
            ("Japan", "Asia/Tokyo"),
            ("Russia", "Europe/Moscow"),
            ("UK", "Europe/London"),
            ("Italy", "Europe/Rome"),
        ]
        now_utc = datetime.now(pytz.utc)

        for place, tz_name in locations:
            tz = pytz.timezone(tz_name)
            local_time = now_utc.astimezone(tz).strftime("%Y-%m-%d %H:%M")
            label = tk.Label(tz_frame, text=f"{place}: {local_time}",
                             font=("Consolas", 11, "bold"), fg="#3f51b5", 
                             bg="#e8eaf6", padx=6, pady=1)
            label.pack(anchor="center")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimeZoneApp(root)
    root.mainloop()
