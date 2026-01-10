# Testing Guide

This project includes comprehensive unit tests for both JavaScript and Python implementations of the `sum` function.

## Running JavaScript Tests

To run the JavaScript tests, simply execute:

```bash
node test.js
```

The JavaScript tests use a custom test framework implementation that mimics Jest-style syntax with functions like `test()` and `expect()`. The custom framework includes:
- `toEqual()` for exact equality comparisons
- `toBeCloseTo()` for floating-point comparisons with precision handling
- `toBeTruthy()` and `toBeFalsy()` for boolean evaluations

Note: For production applications, consider installing and using Jest:

```bash
npm install --save-dev jest
npm test
```

## Running Python Tests

To run the Python tests, execute:

```bash
python test.py
```

Alternatively, you can use the unittest module directly:

```bash
python -m unittest test
```

Or for more verbose output:

```bash
python -m unittest -v test
```

## Test Coverage

The tests cover the following scenarios:
- Adding positive numbers
- Adding negative numbers  
- Adding with zero values
- Adding decimal numbers (with proper floating-point precision handling)
- Adding large numbers

## Test Structure

### JavaScript Tests
- Custom test framework implementation with Jest-like syntax
- Multiple test cases with descriptive names
- Proper handling of floating-point precision issues
- Expectation functions for various types of assertions

### Python Tests
- Uses Python's built-in `unittest` framework
- Organized in a `TestSumFunction` class
- Separate test methods for different scenarios
- Proper assertion methods including `assertAlmostEqual` for decimal comparisons
- Comprehensive coverage of edge cases