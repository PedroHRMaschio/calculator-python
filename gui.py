import tkinter as tk
from tkinter import messagebox
from calculator import Calculator


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.calc = Calculator()

        # Text input
        self.display = tk.Entry(root, width=30, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
        self.display.grid(row=0, column=0, columnspan=4, pady=10)

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("Clear", 5, 0, 2), ("History", 5, 2, 2)
        ]

        for (text, row, col, *extra) in buttons:
            button = tk.Button(self.root, text=text, width=10, height=2, font=("Arial", 14),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, columnspan=extra[0] if extra else 1, pady=5)

    def on_button_click(self, text):
        if text == "=":
            self.calculate()
        elif text == "Clear":
            self.display.delete(0, tk.END)
        elif text == "History":
            self.show_history()
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + text)

    def calculate(self):
        """Evaluates the expression and uses the Calculator class to calculate."""
        try:
            expression = self.display.get()
            if "+" in expression:
                num1, num2 = map(float, expression.split("+"))
                result = self.calc.add(num1, num2)
            elif "-" in expression:
                num1, num2 = map(float, expression.split("-"))
                result = self.calc.subtract(num1, num2)
            elif "*" in expression:
                num1, num2 = map(float, expression.split("*"))
                result = self.calc.multiply(num1, num2)
            elif "/" in expression:
                num1, num2 = map(float, expression.split("/"))
                result = self.calc.divide(num1, num2)
            else:
                raise ValueError("Operação inválida")
            print(result)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid Expression: {str(e)}")

    def show_history(self):
        """Shows operation history."""
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")

        history_text = "\n".join(self.calc.get_history()) or "No history yet."
        tk.Label(history_window, text=history_text, justify="left").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
