import tkinter as tk
from tkinter import ttk, messagebox
import math

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Calculator")
        self.root.geometry("400x600")
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Display area
        self.display_var = tk.StringVar()
        display = ttk.Entry(main_frame, textvariable=self.display_var, font=("Arial", 16), 
                           justify="right", state="readonly")
        display.grid(row=0, column=0, columnspan=4, sticky=(tk.W, tk.E), pady=5)
        
        # Button layout
        buttons = [
            ('C', 1, 0), ('±', 1, 1), ('√', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 2), ('=', 5, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            if text == '0':
                btn = ttk.Button(main_frame, text=text, command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, columnspan=2, sticky=(tk.W, tk.E), padx=2, pady=2)
            else:
                btn = ttk.Button(main_frame, text=text, command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, sticky=(tk.W, tk.E), padx=2, pady=2)
        
        # Initialize calculator state
        self.current_input = ""
        self.result = 0
        self.last_operation = ""
        
    def button_click(self, value):
        if value.isdigit() or value == '.':
            self.current_input += value
            self.display_var.set(self.current_input)
        elif value == 'C':
            self.current_input = ""
            self.result = 0
            self.last_operation = ""
            self.display_var.set("")
        elif value == '=':
            try:
                if self.last_operation:
                    expression = str(self.result) + self.last_operation + self.current_input
                    self.result = eval(expression)
                else:
                    self.result = float(self.current_input)
                
                self.display_var.set(str(self.result))
                self.current_input = str(self.result)
                self.last_operation = ""
            except Exception as e:
                messagebox.showerror("Error", "Invalid operation")
                self.clear_all()
        elif value in ['+', '-', '*', '/']:
            if self.current_input:
                if not self.last_operation and self.result == 0:
                    self.result = float(self.current_input)
                else:
                    # Calculate intermediate result if there's a pending operation
                    expression = str(self.result) + self.last_operation + self.current_input
                    try:
                        self.result = eval(expression)
                    except:
                        messagebox.showerror("Error", "Invalid operation")
                        self.clear_all()
                        return
                
                self.last_operation = value
                self.current_input = ""
        elif value == '√':
            try:
                num = float(self.current_input) if self.current_input else self.result
                result = math.sqrt(num)
                self.display_var.set(str(result))
                self.current_input = str(result)
                self.result = result
            except:
                messagebox.showerror("Error", "Invalid operation")
        elif value == '±':
            if self.current_input:
                if self.current_input.startswith('-'):
                    self.current_input = self.current_input[1:]
                else:
                    self.current_input = '-' + self.current_input
                self.display_var.set(self.current_input)
    
    def clear_all(self):
        self.current_input = ""
        self.result = 0
        self.last_operation = ""
        self.display_var.set("")

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()