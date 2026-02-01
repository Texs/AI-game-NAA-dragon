# AI Calculator with GUI

This project includes two calculator applications with graphical user interfaces built using Python's tkinter library, plus recommendations for building an AI calculator:

1. **Basic Calculator (gui_app.py)** - A traditional calculator with buttons for standard operations
2. **AI Calculator (ai_calculator.py)** - A natural language calculator that can interpret mathematical expressions written in English

## How to Run

To run either calculator, use Python 3:

```bash
# For the basic calculator
python gui_app.py

# For the AI calculator
python ai_calculator.py
```

## Features

### Basic Calculator
- Standard arithmetic operations (+, -, *, /)
- Square root (√)
- Sign change (±)
- Clear (C) functionality
- Clean and intuitive interface

### AI Calculator
- Natural language processing for mathematical expressions
- Supports both symbolic and verbal operations
- Calculation history tracking
- Examples of supported expressions
- Safe evaluation of expressions
## Recommendations for Building an AI Calculator

Here are key recommendations for developing an effective AI calculator:

### 1. Natural Language Processing
- Implement keyword recognition for mathematical operations
- Handle variations in phrasing ("plus", "add", "sum" all mean addition)
- Support for both symbolic and verbal input methods

### 2. Expression Parsing
- Develop a robust parser that converts natural language to mathematical expressions
- Handle operator precedence correctly
- Support for parentheses and complex expressions

### 3. Safety Considerations
- Implement safe evaluation methods to prevent code injection
- Validate inputs before processing
- Provide error handling for invalid expressions

### 4. User Experience
- Provide clear examples of supported expressions
- Maintain a calculation history
- Offer both keyboard and mouse input options
- Responsive design that works well on different screen sizes

### 5. Mathematical Functions
- Support for basic arithmetic operations
- Scientific functions (trigonometry, logarithms, exponents)
- Constants (π, e) for advanced calculations

### 6. Extensibility
- Modular design to easily add new functions
- Plugin architecture for custom operations
- Configurable settings for different user preferences

## Supported Operations in the AI Calculator

The AI calculator recognizes these operations:
- Addition: "add", "plus", "sum"
- Subtraction: "subtract", "minus", "less"
- Multiplication: "multiply", "times", "product"
- Division: "divide", "divided by", "over"
- Exponents: "power", "to the power of", "raised to"
- Square root: "square root", "root"
- Logarithms: "log", "logarithm"
- Trigonometric functions: "sin", "cos", "tan"

Example inputs:
- "What is 5 plus 3?"
- "Calculate 10 times 25"
- "Find the square root of 64"
- "What is 2 to the power of 8?"

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- math module (included with Python)

No external dependencies are required for this implementation.