"""
Module for basic mathematical operations
"""
from typing import Union


class MathOperations:
    """
    A class that provides basic mathematical operations
    """
    
    @staticmethod
    def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
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

    @staticmethod
    def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Subtracts b from a
        
        Args:
            a (int/float): First number
            b (int/float): Number to subtract
            
        Returns:
            int/float: Difference of a and b
            
        Raises:
            TypeError: If either argument is not a number
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a - b

    @staticmethod
    def multiply(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
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

    @staticmethod
    def divide(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """
        Divides a by b
        
        Args:
            a (int/float): First number
            b (int/float): Number to divide by
            
        Returns:
            int/float: Quotient of a and b
            
        Raises:
            TypeError: If either argument is not a number
            ZeroDivisionError: If b is zero
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        
        return a / b


def sum(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Adds two numbers together (for backward compatibility)
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Sum of a and b
        
    Raises:
        TypeError: If either argument is not a number
    """
    return MathOperations.add(a, b)