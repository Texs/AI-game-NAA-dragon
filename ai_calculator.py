import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math
import re
import operator

class AICalculator:
    def __init__(self):
        # Dictionary mapping words to operations
        self.operations_map = {
            'add': '+',
            'plus': '+',
            'sum': '+',
            'subtract': '-',
            'minus': '-',
            'less': '-',
            'multiply': '*',
            'times': '*',
            'product': '*',
            'divide': '/',
            'divided by': '/',
            'over': '/',
            'power': '**',
            'to the power of': '**',
            'raised to': '**',
            'square root': 'sqrt',
            'root': 'sqrt',
            'log': 'log',
            'logarithm': 'log',
            'sin': 'sin',
            'cosine': 'cos',
            'cos': 'cos',
            'tangent': 'tan',
            'tan': 'tan'
        }
        
        # Dictionary mapping operations to functions
        self.func_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '**': operator.pow,
            'sqrt': math.sqrt,
            'log': math.log10,
            'ln': math.log,
            'sin': lambda x: math.sin(math.radians(x)),
            'cos': lambda x: math.cos(math.radians(x)),
            'tan': lambda x: math.tan(math.radians(x))
        }

    def parse_expression(self, text):
        """Parse natural language expression into mathematical expression"""
        text = text.lower().strip()
        
        # Replace word operations with symbols
        for word, symbol in self.operations_map.items():
            text = text.replace(word, symbol)
        
        # Extract numbers and operations
        tokens = []
        i = 0
        while i < len(text):
            if text[i].isdigit() or text[i] == '.':
                # Extract the full number
                num_str = ''
                while i < len(text) and (text[i].isdigit() or text[i] == '.'):
                    num_str += text[i]
                    i += 1
                tokens.append(float(num_str))
            elif text[i] in '+-*/()^':
                tokens.append(text[i])
                i += 1
            elif text[i:i+2] == '**':  # Power operator
                tokens.append('**')
                i += 2
            elif text[i:i+4] == 'sqrt':  # Square root
                tokens.append('sqrt')
                i += 4
            elif text[i:i+3] == 'log':  # Logarithm
                tokens.append('log')
                i += 3
            elif text[i:i+3] == 'sin':  # Sine
                tokens.append('sin')
                i += 3
            elif text[i:i+3] == 'cos':  # Cosine
                tokens.append('cos')
                i += 3
            elif text[i:i+3] == 'tan':  # Tangent
                tokens.append('tan')
                i += 3
            else:
                i += 1
        
        return tokens

    def evaluate_expression(self, tokens):
        """Evaluate a list of tokens as a mathematical expression"""
        # Convert tokens to a string expression first
        expr_str = ""
        for token in tokens:
            if isinstance(token, float):
                expr_str += str(token)
            else:
                expr_str += str(token)
            expr_str += " "
        
        # Evaluate the expression safely
        try:
            # Replace function names with math module equivalents
            expr_str = expr_str.replace('sqrt', 'math.sqrt')
            expr_str = expr_str.replace('log', 'math.log10')
            expr_str = expr_str.replace('ln', 'math.log')
            expr_str = expr_str.replace('sin', 'lambda x: math.sin(math.radians(x))')
            expr_str = expr_str.replace('cos', 'lambda x: math.cos(math.radians(x))')
            expr_str = expr_str.replace('tan', 'lambda x: math.tan(math.radians(x))')
            
            # Evaluate using eval (in a safe way for our controlled input)
            allowed_names = {
                k: v for k, v in math.__dict__.items() if not k.startswith("__")
            }
            allowed_names.update({"abs": abs, "round": round})
            result = eval(expr_str, {"__builtins__": {}}, allowed_names)
            return result
        except Exception as e:
            raise ValueError(f"Could not evaluate expression: {e}")

    def calculate(self, input_text):
        """Main calculation method"""
        try:
            tokens = self.parse_expression(input_text)
            result = self.evaluate_expression(tokens)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

class AICalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("AI Calculator")
        self.root.geometry("600x700")
        
        # Create AI Calculator instance
        self.ai_calc = AICalculator()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="AI Calculator", font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)
        
        # Input label
        input_label = ttk.Label(main_frame, text="Enter your calculation:")
        input_label.grid(row=1, column=0, sticky=tk.W, pady=5)
        
        # Input field
        self.input_var = tk.StringVar()
        input_entry = ttk.Entry(main_frame, textvariable=self.input_var, font=("Arial", 12), width=50)
        input_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        input_entry.bind('<Return>', lambda event: self.calculate_result())
        
        # Calculate button
        calc_button = ttk.Button(main_frame, text="Calculate", command=self.calculate_result)
        calc_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Result label
        result_label = ttk.Label(main_frame, text="Result:")
        result_label.grid(row=4, column=0, sticky=tk.W, pady=5)
        
        # Result display
        self.result_var = tk.StringVar()
        result_display = ttk.Entry(main_frame, textvariable=self.result_var, font=("Arial", 14), 
                                  state="readonly", width=50)
        result_display.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # History label
        history_label = ttk.Label(main_frame, text="Calculation History:")
        history_label.grid(row=6, column=0, sticky=tk.W, pady=(20, 5))
        
        # History text area
        self.history_text = scrolledtext.ScrolledText(main_frame, width=60, height=15, font=("Arial", 10))
        self.history_text.grid(row=7, column=0, columnspan=2, pady=5)
        
        # Clear history button
        clear_button = ttk.Button(main_frame, text="Clear History", command=self.clear_history)
        clear_button.grid(row=8, column=0, columnspan=2, pady=10)
        
        # Examples label
        examples_label = ttk.Label(main_frame, text="Examples:", font=("Arial", 10, "bold"))
        examples_label.grid(row=9, column=0, sticky=tk.W, pady=(10, 5))
        
        # Examples text
        examples_text = """
        Examples of supported expressions:
        • What is 5 plus 3?
        • Calculate 10 times 25
        • What is 100 divided by 4?
        • Find the square root of 64
        • What is 2 to the power of 8?
        • Calculate sin of 30 degrees
        • What is log of 100?
        • 5 * (3 + 2) - 10 / 2
        """
        examples_area = tk.Text(main_frame, height=8, width=60, wrap=tk.WORD, bg="#f0f0f0", relief="flat")
        examples_area.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        examples_area.insert(tk.END, examples_text)
        examples_area.config(state=tk.DISABLED)
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
    def calculate_result(self):
        """Calculate the result of the input expression"""
        input_text = self.input_var.get().strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please enter a calculation.")
            return
            
        try:
            result = self.ai_calc.calculate(input_text)
            self.result_var.set(str(result))
            
            # Add to history
            history_entry = f"Input: {input_text}\nResult: {result}\n{'-'*50}\n"
            self.history_text.insert(tk.END, history_entry)
            self.history_text.see(tk.END)  # Scroll to end
            
            # Clear input
            self.input_var.set("")
        except Exception as e:
            messagebox.showerror("Error", f"Calculation failed: {str(e)}")
    
    def clear_history(self):
        """Clear the history text area"""
        self.history_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = AICalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()