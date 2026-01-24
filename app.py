"""
Main calculator module
Provides backward compatibility while using the new modular structure
"""

from src.py.math_operations import sum

# Make sure sum is available at the module level for backward compatibility
__all__ = ['sum']
