"""
Main test runner for Python code
This file now imports and runs the new modular tests
"""

# Import and run the new test suite
if __name__ == "__main__":
    import subprocess
    import sys
    result = subprocess.run([sys.executable, "tests/py/test_math_operations.py"], capture_output=True, text=True)
    print(result.stdout)
    if result.stderr:
        print("STDERR:", result.stderr, file=sys.stderr)
    sys.exit(result.returncode)
