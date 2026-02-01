"""
Main calculator module
Provides backward compatibility while using the new modular structure
"""

from src.py.math_operations import sum, subtract, multiply, divide

# Make sure all functions are available at the module level for backward compatibility
__all__ = ['sum', 'subtract', 'multiply', 'divide']
