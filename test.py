from app import sum, subtract, multiply, divide


def test_sum():
    """Test the sum function with various inputs."""
    # Basic positive tests
    assert sum(2, 3) == 5, "2 + 3 should equal 5"
    assert sum(-1, 1) == 0, "-1 + 1 should equal 0"
    assert sum(0, 0) == 0, "0 + 0 should equal 0"
    assert sum(-5, -3) == -8, "-5 + (-3) should equal -8"
    assert sum(2.5, 1.5) == 4.0, "2.5 + 1.5 should equal 4.0"
    print("✓ Sum tests passed")


def test_subtract():
    """Test the subtract function with various inputs."""
    # Basic positive tests
    assert subtract(5, 3) == 2, "5 - 3 should equal 2"
    assert subtract(0, 5) == -5, "0 - 5 should equal -5"
    assert subtract(-1, -1) == 0, "-1 - (-1) should equal 0"
    assert subtract(10, -5) == 15, "10 - (-5) should equal 15"
    assert subtract(2.5, 1.0) == 1.5, "2.5 - 1.0 should equal 1.5"
    print("✓ Subtract tests passed")


def test_multiply():
    """Test the multiply function with various inputs."""
    # Basic positive tests
    assert multiply(3, 4) == 12, "3 * 4 should equal 12"
    assert multiply(-2, 3) == -6, "-2 * 3 should equal -6"
    assert multiply(0, 100) == 0, "0 * 100 should equal 0"
    assert multiply(-3, -4) == 12, "-3 * (-4) should equal 12"
    assert multiply(2.5, 2) == 5.0, "2.5 * 2 should equal 5.0"
    print("✓ Multiply tests passed")


def test_divide():
    """Test the divide function with various inputs."""
    # Basic positive tests
    assert divide(10, 2) == 5, "10 / 2 should equal 5"
    assert divide(-6, 2) == -3, "-6 / 2 should equal -3"
    assert abs(divide(7, 3) - 2.33333) < 0.0001, "7 / 3 should approximately equal 2.33333"
    assert divide(0, 5) == 0, "0 / 5 should equal 0"
    print("✓ Divide tests passed")


def test_error_handling():
    """Test error handling for all functions."""
    # Test division by zero
    try:
        divide(5, 0)
        assert False, "Division by zero should raise ZeroDivisionError"
    except ZeroDivisionError as e:
        assert str(e) == "Division by zero is not allowed", "Wrong error message for division by zero"
    
    # Test type validation for all functions
    functions_to_test = [sum, subtract, multiply, divide]
    for func in functions_to_test:
        try:
            func("not a number", 5)
            assert False, f"{func.__name__} should raise TypeError for non-number inputs"
        except TypeError:
            pass  # Expected behavior
    
    print("✓ Error handling tests passed")


if __name__ == "__main__":
    test_sum()
    test_subtract()
    test_multiply()
    test_divide()
    test_error_handling()
    print("\n🎉 All tests passed!")
