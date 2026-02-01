import sys
from app import sum, subtract, multiply, divide

def test_sum():
    """Test cases for the sum function"""
    # Basic addition
from app import sum

def test_sum_positive_numbers():
    """Test addition of positive numbers"""
    assert sum(2, 3) == 5, "2 + 3 should equal 5"

def test_sum_negative_numbers():
    """Test addition with negative numbers"""
    assert sum(-1, 1) == 0, "-1 + 1 should equal 0"
    assert sum(0, 0) == 0, "0 + 0 should equal 0"
    
    # Decimal addition
    assert abs(sum(0.1, 0.2) - 0.3) < 0.0001, "0.1 + 0.2 should approximately equal 0.3"
    
    # Negative numbers
    assert sum(-5, -3) == -8, "-5 + (-3) should equal -8"
    assert sum(-10, 5) == -5, "-10 + 5 should equal -5"
    
    print("✓ Sum tests passed")

def test_subtract():
    """Test cases for the subtract function"""
    # Basic subtraction
    assert subtract(5, 3) == 2, "5 - 3 should equal 2"
    assert subtract(0, 5) == -5, "0 - 5 should equal -5"
    assert subtract(-1, -1) == 0, "-1 - (-1) should equal 0"
    
    # Decimal subtraction
    assert abs(subtract(0.3, 0.1) - 0.2) < 0.0001, "0.3 - 0.1 should approximately equal 0.2"
    
    print("✓ Subtract tests passed")

def test_multiply():
    """Test cases for the multiply function"""
    # Basic multiplication
    assert multiply(3, 4) == 12, "3 * 4 should equal 12"
    assert multiply(-2, 3) == -6, "-2 * 3 should equal -6"
    assert multiply(5, 0) == 0, "5 * 0 should equal 0"
    
    # Decimal multiplication
    assert abs(multiply(0.1, 0.2) - 0.02) < 0.0001, "0.1 * 0.2 should approximately equal 0.02"
    
    # Negative multiplication
    assert multiply(-3, -4) == 12, "-3 * (-4) should equal 12"
    assert multiply(-5, 2) == -10, "-5 * 2 should equal -10"
    
    print("✓ Multiply tests passed")

def test_divide():
    """Test cases for the divide function"""
    # Basic division
    assert divide(10, 2) == 5, "10 / 2 should equal 5"
    assert divide(-6, 2) == -3, "-6 / 2 should equal -3"
    
    # Decimal division
    assert abs(divide(1, 3) - 0.3333) < 0.0001, "1 / 3 should approximately equal 0.3333"
    
    # Division by negative
    assert divide(8, -2) == -4, "8 / (-2) should equal -4"
    
    print("✓ Divide tests passed")

def test_error_handling():
    """Test cases for error handling"""
    # Test TypeError for non-number inputs
    try:
        sum('a', 5)
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
    # Test string input
    raised = False
    try:
        sum("a", 5)
    except TypeError:
        raised = True
    assert raised, "Should have raised TypeError for string input"
    
    # Test None input
    raised = False
    try:
        subtract(5, 'b')
        assert False, "Should have raised TypeError for string input"
        sum(5, None)
    except TypeError:
        raised = True
    assert raised, "Should have raised TypeError for None input"
    
    # Test list input
    raised = False
    try:
        multiply([1, 2], 3)
        assert False, "Should have raised TypeError for list input"
    except TypeError:
        pass  # Expected behavior
    
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Should have raised ZeroDivisionError for division by zero"
    except ZeroDivisionError:
        pass  # Expected behavior
    
    print("✓ Error handling tests passed")

def run_all_tests():
    """Run all test suites"""
    total_tests = 4  # Number of test functions
    passed_tests = 0
    
    try:
        test_sum()
        passed_tests += 1
    except Exception as e:
        print(f"✗ Sum tests failed: {e}")
    
    try:
        test_subtract()
        passed_tests += 1
    except Exception as e:
        print(f"✗ Subtract tests failed: {e}")
    
    try:
        test_multiply()
        passed_tests += 1
    except Exception as e:
        print(f"✗ Multiply tests failed: {e}")
    
    try:
        test_divide()
        passed_tests += 1
    except Exception as e:
        print(f"✗ Divide tests failed: {e}")
    
    try:
        test_error_handling()
        passed_tests += 1
    except Exception as e:
        print(f"✗ Error handling tests failed: {e}")
    
    print(f"\nTest Results: {passed_tests}/{total_tests + 1} test suites passed")
    
    if passed_tests == total_tests + 1:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
        sum([1, 2], 3)
    except TypeError:
        raised = True
    assert raised, "Should have raised TypeError for list input"

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
    print("Running tests...\n")
    
    tests = [
        test_sum_positive_numbers,
        test_sum_negative_numbers,
        test_sum_with_zero,
        test_sum_decimal_numbers,
        test_sum_invalid_inputs
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
