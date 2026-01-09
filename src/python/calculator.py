"""
Calculator module - provides basic mathematical operations
"""

def sum(a, b):
    """
    Adds two numbers together
    
    Args:
        a (number): The first number
        b (number): The second number
    
    Returns:
        number: The sum of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be numbers')
    return a + b

def subtract(a, b):
    """
    Subtracts the second number from the first
    
    Args:
        a (number): The first number
        b (number): The second number
    
    Returns:
        number: The difference of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be numbers')
    return a - b

def multiply(a, b):
    """
    Multiplies two numbers together
    
    Args:
        a (number): The first number
        b (number): The second number
    
    Returns:
        number: The product of a and b
    
    Raises:
        TypeError: If either argument is not a number
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be numbers')
    return a * b

def divide(a, b):
    """
    Divides the first number by the second
    
    Args:
        a (number): The first number
        b (number): The second number
    
    Returns:
        number: The quotient of a and b
    
    Raises:
        TypeError: If either argument is not a number
        ZeroDivisionError: If attempting to divide by zero
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('Both arguments must be numbers')
    if b == 0:
        raise ZeroDivisionError('Cannot divide by zero')
    return a / b