"""
A module containing basic mathematical operations.
"""

def sum(a, b):
    """
    Add two numbers together.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The sum of a and b
    
    Raises:
        TypeError: If either parameter is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be numbers")
    return a + b


def subtract(a, b):
    """
    Subtract b from a.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The difference of a and b
    
    Raises:
        TypeError: If either parameter is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be numbers")
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The product of a and b
    
    Raises:
        TypeError: If either parameter is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be numbers")
    return a * b


def divide(a, b):
    """
    Divide a by b.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
    
    Returns:
        int/float: The quotient of a and b
    
    Raises:
        TypeError: If either parameter is not a number
        ZeroDivisionError: If b is zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both parameters must be numbers")
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b
