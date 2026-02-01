import sys
from app import sum

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
        sum(5, None)
    except TypeError:
        raised = True
    assert raised, "Should have raised TypeError for None input"
    
    # Test list input
    raised = False
    try:
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
