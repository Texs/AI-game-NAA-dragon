"""
Unit tests for the math operations module
"""
import sys
from src.py.math_operations import MathOperations, sum


def test_sum_positive_numbers():
    """Test addition of positive numbers"""
    assert sum(2, 3) == 5, "2 + 3 should equal 5"


def test_sum_negative_numbers():
    """Test addition with negative numbers"""
    assert sum(-1, 1) == 0, "-1 + 1 should equal 0"
    assert sum(-5, -3) == -8, "-5 + (-3) should equal -8"


def test_sum_with_zero():
    """Test addition involving zero"""
    assert sum(0, 0) == 0, "0 + 0 should equal 0"
    assert sum(5, 0) == 5, "5 + 0 should equal 5"
    assert sum(0, 5) == 5, "0 + 5 should equal 5"


def test_sum_decimal_numbers():
    """Test addition of decimal numbers"""
    # Using approximate equality for floating point numbers
    result = sum(2.5, 3.7)
    expected = 6.2
    assert abs(result - expected) < 0.0001, f"2.5 + 3.7 should approximately equal {expected}, got {result}"


def test_sum_invalid_inputs():
    """Test that invalid inputs raise TypeError"""
    try:
        sum("a", 5)
        assert False, "Should have raised TypeError for string input"
    except TypeError:
        pass  # Expected behavior

    try:
        sum(5, None)
        assert False, "Should have raised TypeError for None input"
    except TypeError:
        pass  # Expected behavior

    try:
        sum([1, 2], 3)
        assert False, "Should have raised TypeError for list input"
    except TypeError:
        pass  # Expected behavior


def test_math_operations_add():
    """Test MathOperations.add method"""
    assert MathOperations.add(2, 3) == 5, "MathOperations.add(2, 3) should equal 5"
    assert MathOperations.add(-1, 1) == 0, "MathOperations.add(-1, 1) should equal 0"


def test_math_operations_subtract():
    """Test MathOperations.subtract method"""
    assert MathOperations.subtract(5, 3) == 2, "MathOperations.subtract(5, 3) should equal 2"
    assert MathOperations.subtract(3, 5) == -2, "MathOperations.subtract(3, 5) should equal -2"


def test_math_operations_multiply():
    """Test MathOperations.multiply method"""
    assert MathOperations.multiply(3, 4) == 12, "MathOperations.multiply(3, 4) should equal 12"
    assert MathOperations.multiply(-2, 3) == -6, "MathOperations.multiply(-2, 3) should equal -6"


def test_math_operations_divide():
    """Test MathOperations.divide method"""
    assert MathOperations.divide(10, 2) == 5, "MathOperations.divide(10, 2) should equal 5"
    assert MathOperations.divide(7, 2) == 3.5, "MathOperations.divide(7, 2) should equal 3.5"


def test_math_operations_divide_by_zero():
    """Test that division by zero raises ZeroDivisionError"""
    try:
        MathOperations.divide(10, 0)
        assert False, "Should have raised ZeroDivisionError for division by zero"
    except ZeroDivisionError:
        pass  # Expected behavior
    except Exception as e:
        assert False, f"Should have raised ZeroDivisionError, but raised {type(e).__name__}"


def test_all_operations_with_invalid_inputs():
    """Test that all operations raise TypeError for invalid inputs"""
    operations = [
        MathOperations.add,
        MathOperations.subtract,
        MathOperations.multiply,
        MathOperations.divide
    ]
    
    for op in operations:
        try:
            op("invalid", 5)
            assert False, f"{op.__name__} should have raised TypeError for string input"
        except TypeError:
            pass  # Expected behavior
        
        try:
            op(5, "invalid")
            assert False, f"{op.__name__} should have raised TypeError for string input"
        except TypeError:
            pass  # Expected behavior


def run_test(test_func):
    """Helper function to run individual tests"""
    try:
        test_func()
        print(f"✓ {test_func.__name__}")
        return True
    except Exception as e:
        print(f"✗ {test_func.__name__}: {str(e)}")
        return False


def main():
    """Run all tests and report results"""
    print("Running math operations tests...\n")

    tests = [
        test_sum_positive_numbers,
        test_sum_negative_numbers,
        test_sum_with_zero,
        test_sum_decimal_numbers,
        test_sum_invalid_inputs,
        test_math_operations_add,
        test_math_operations_subtract,
        test_math_operations_multiply,
        test_math_operations_divide,
        test_math_operations_divide_by_zero,
        test_all_operations_with_invalid_inputs
    ]

    passed_tests = 0
    total_tests = len(tests)

    for test in tests:
        if run_test(test):
            passed_tests += 1

    print(f"\nResults: {passed_tests}/{total_tests} tests passed")

    if passed_tests != total_tests:
        sys.exit(1)
    else:
        print("All tests passed!")


if __name__ == "__main__":
    main()