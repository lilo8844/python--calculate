

import tkinter as tk
from tkinter import ttk
import math
import datetime


DARK_BG = "#1e1e1e"
DARK_BTN = "#2d2d2d"
DARK_TEXT = "white"

LIGHT_BG = "#f5f5f5"
LIGHT_BTN = "#ffffff"
LIGHT_TEXT = "black"


class CalculatorApp:

  
    def __init__(self):

        self.root = tk.Tk()
        self.root.title("Mega Calculator")
        self.root.geometry("520x650")
        self.root.resizable(False, False)

        self.dark_mode = True
        self.history_list = []

        self.create_widgets()
        self.bind_keys()
        self.apply_theme()

        self.root.mainloop()




    def create_widgets(self):

  
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(fill="x", pady=5)

     
        self.display = tk.Entry(
            self.top_frame,
            font=("Consolas", 26),
            justify="right"
        )
        self.display.pack(fill="both", padx=8, ipady=12)

        self.history_box = tk.Listbox(self.root, height=6)
        self.history_box.pack(fill="x", padx=8, pady=5)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(expand=True, fill="both")


        self.buttons = [
            ["7","8","9","/","sin"],
            ["4","5","6","*","cos"],
            ["1","2","3","-","tan"],
            ["0",".","C","+","√"],
            ["(",")","^","log","="]
        ]

        self.create_buttons()

  
        self.bottom = tk.Frame(self.root)
        self.bottom.pack(fill="x")

        tk.Button(
            self.bottom,
            text="Toggle Theme",
            command=self.toggle_theme
        ).pack(fill="x")


    def create_buttons(self):

        for r, row in enumerate(self.buttons):

            frame = tk.Frame(self.buttons_frame)
            frame.pack(expand=True, fill="both")

            for label in row:

                btn = tk.Button(
                    frame,
                    text=label,
                    font=("Arial", 16),
                    command=lambda x=label: self.handle_click(x)
                )

                btn.pack(side="left", expand=True, fill="both")




    def handle_click(self, value):

        if value == "C":
            self.clear()

        elif value == "=":
            self.calculate()

        elif value == "√":
            self.add_function("math.sqrt(")

        elif value == "sin":
            self.add_function("math.sin(")

        elif value == "cos":
            self.add_function("math.cos(")

        elif value == "tan":
            self.add_function("math.tan(")

        elif value == "log":
            self.add_function("math.log10(")

        elif value == "^":
            self.insert("**")

        else:
            self.insert(value)




    def insert(self, value):
        self.display.insert(tk.END, value)


    def clear(self):
        self.display.delete(0, tk.END)


    def add_function(self, text):
        self.display.insert(tk.END, text)



    def calculate(self):

        expr = self.display.get()

        try:
            result = eval(expr)

            self.display.delete(0, tk.END)
            self.display.insert(0, result)

            self.add_history(expr, result)

        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")


  
    def add_history(self, expr, result):

        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        text = f"[{timestamp}] {expr} = {result}"

        self.history_list.append(text)
        self.history_box.insert(tk.END, text)

        if len(self.history_list) > 20:
            self.history_box.delete(0)


   
    def bind_keys(self):

        for char in "0123456789.+-*/()":
            self.root.bind(char, lambda e, x=char: self.insert(x))

        self.root.bind("<Return>", lambda e: self.calculate())
        self.root.bind("<BackSpace>", lambda e: self.backspace())


    def backspace(self):
        text = self.display.get()[:-1]
        self.display.delete(0, tk.END)
        self.display.insert(0, text)




    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()


    def apply_theme(self):

        if self.dark_mode:
            bg = DARK_BG
            btn = DARK_BTN
            fg = DARK_TEXT
        else:
            bg = LIGHT_BG
            btn = LIGHT_BTN
            fg = LIGHT_TEXT

        self.root.configure(bg=bg)

        for widget in self.root.winfo_children():
            self.colorize(widget, bg, btn, fg)


    def colorize(self, widget, bg, btn, fg):

        try:
            widget.configure(bg=bg, fg=fg)
        except:
            pass

        for child in widget.winfo_children():
            try:
                child.configure(bg=btn, fg=fg)
            except:
                pass

            self.colorize(child, bg, btn, fg)



if __name__ == "__main__":
    CalculatorApp()

