"""
Mathematical operations library
Provides basic arithmetic functions with input validation
"""

def sum(a, b):
    """
    Adds two numbers together
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a + b

def subtract(a, b):
    """
    Subtracts second number from first
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Difference of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Product of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b

def divide(a, b):
    """
    Divides first number by second
    
    Args:
        a (int/float): First number (dividend)
        b (int/float): Second number (divisor)
        
    Returns:
        int/float: Quotient of a divided by b
        
    Raises:
        TypeError: If either argument is not a number
        ZeroDivisionError: If divisor is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
