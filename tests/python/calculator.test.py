"""
Calculator module tests
"""

import sys
import os

# Add the src directory to the path so we can import the calculator module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../../src/python'))

from calculator import sum, subtract, multiply, divide

def test_sum():
    """Test the sum function"""
    print("Testing sum function...")
    
    # Basic tests
    assert sum(2, 3) == 5, "2 + 3 should equal 5"
    print("✓ sum(2, 3) == 5")
    
    assert sum(-1, 1) == 0, "-1 + 1 should equal 0"
    print("✓ sum(-1, 1) == 0")
    
    assert sum(0, 0) == 0, "0 + 0 should equal 0"
    print("✓ sum(0, 0) == 0")
    
    # Test error handling
    try:
        sum('a', 5)
        assert False, "sum should raise TypeError for non-number input"
    except TypeError:
        print("✓ sum raises TypeError for non-number input")

def test_subtract():
    """Test the subtract function"""
    print("\nTesting subtract function...")
    
    assert subtract(5, 3) == 2, "5 - 3 should equal 2"
    print("✓ subtract(5, 3) == 2")
    
    assert subtract(0, 5) == -5, "0 - 5 should equal -5"
    print("✓ subtract(0, 5) == -5")

def test_multiply():
    """Test the multiply function"""
    print("\nTesting multiply function...")
    
    assert multiply(3, 4) == 12, "3 * 4 should equal 12"
    print("✓ multiply(3, 4) == 12")
    
    assert multiply(-2, 3) == -6, "-2 * 3 should equal -6"
    print("✓ multiply(-2, 3) == -6")

def test_divide():
    """Test the divide function"""
    print("\nTesting divide function...")
    
    assert divide(10, 2) == 5, "10 / 2 should equal 5"
    print("✓ divide(10, 2) == 5")
    
    assert divide(7, 2) == 3.5, "7 / 2 should equal 3.5"
    print("✓ divide(7, 2) == 3.5")
    
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "divide should raise ZeroDivisionError for division by zero"
    except ZeroDivisionError:
        print("✓ divide raises ZeroDivisionError for division by zero")

if __name__ == "__main__":
    try:
        test_sum()
        test_subtract()
        test_multiply()
        test_divide()
        print("\nAll tests passed! ✓")
    except Exception as e:
        print(f"Test failed with error: {e}")
        sys.exit(1)