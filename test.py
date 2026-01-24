import unittest
from app import sum

class TestSumFunction(unittest.TestCase):
    
    def test_positive_numbers(self):
        """Test adding positive numbers"""
        self.assertEqual(sum(2, 3), 5)
        self.assertEqual(sum(10, 15), 25)
        
    def test_negative_numbers(self):
        """Test adding negative numbers"""
        self.assertEqual(sum(-1, 1), 0)
        self.assertEqual(sum(-5, -3), -8)
        self.assertEqual(sum(-10, 5), -5)
        
    def test_zero_values(self):
        """Test adding with zero"""
        self.assertEqual(sum(0, 0), 0)
        self.assertEqual(sum(0, 5), 5)
        self.assertEqual(sum(7, 0), 7)
        
    def test_decimal_numbers(self):
        """Test adding decimal numbers (may have precision issues)"""
        # Note: Floating point precision might cause issues here
        self.assertAlmostEqual(sum(0.1, 0.2), 0.3, places=7)
        self.assertEqual(sum(1.5, 2.5), 4.0)
        
    def test_large_numbers(self):
        """Test adding large numbers"""
        self.assertEqual(sum(1000000, 2000000), 3000000)

if __name__ == "__main__":
    # Run the tests
    unittest.main()
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
