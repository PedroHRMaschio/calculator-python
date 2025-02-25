import tkinter as tk
from tkinter import messagebox
from calculator import Calculator


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.calc = Calculator()

        # Text entry on display
        self.display = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("Clear", 5, 0, 4)
        ]

        for (text, row, col, *extra) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=3, font=("Arial", 14),
                               command=lambda text=text: self.on_button_click(text))
            button.grid(row=row, column=col, columnspan=extra[0] if extra else 1)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.display.get())
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        elif text == "Clear":
            self.display.delete(0, tk.END)
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + text)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
