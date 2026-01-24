const { sum, subtract, multiply, divide } = require('./app');

// Counter for tracking total tests
let testsPassed = 0;
let totalTests = 0;

// Function to run a test case
function runTest(description, testFunction) {
    totalTests++;
    try {
        testFunction();
        console.log(`✓ ${description}`);
        testsPassed++;
    } catch (error) {
        console.error(`✗ ${description}: ${error.message}`);
    }
}

// Test sum function
runTest('sum(2, 3) should return 5', () => {
    const result = sum(2, 3);
    if (result !== 5) {
        throw new Error(`Expected 5, got ${result}`);
    }
});

runTest('sum(-1, 1) should return 0', () => {
    const result = sum(-1, 1);
    if (result !== 0) {
        throw new Error(`Expected 0, got ${result}`);
    }
});

runTest('sum(0, 0) should return 0', () => {
    const result = sum(0, 0);
    if (result !== 0) {
        throw new Error(`Expected 0, got ${result}`);
    }
});

runTest('sum with decimals: sum(0.1, 0.2) should approximately equal 0.3', () => {
    const result = sum(0.1, 0.2);
    if (Math.abs(result - 0.3) > 0.0001) {
        throw new Error(`Expected ~0.3, got ${result}`);
    }
});

// Test subtract function
runTest('subtract(5, 3) should return 2', () => {
    const result = subtract(5, 3);
    if (result !== 2) {
        throw new Error(`Expected 2, got ${result}`);
    }
});

runTest('subtract(0, 5) should return -5', () => {
    const result = subtract(0, 5);
    if (result !== -5) {
        throw new Error(`Expected -5, got ${result}`);
    }
});

// Test multiply function
runTest('multiply(3, 4) should return 12', () => {
    const result = multiply(3, 4);
    if (result !== 12) {
        throw new Error(`Expected 12, got ${result}`);
    }
});

runTest('multiply with negative: multiply(-2, 3) should return -6', () => {
    const result = multiply(-2, 3);
    if (result !== -6) {
        throw new Error(`Expected -6, got ${result}`);
    }
});

runTest('multiply by zero: multiply(5, 0) should return 0', () => {
    const result = multiply(5, 0);
    if (result !== 0) {
        throw new Error(`Expected 0, got ${result}`);
    }
});

// Test divide function
runTest('divide(10, 2) should return 5', () => {
    const result = divide(10, 2);
    if (result !== 5) {
        throw new Error(`Expected 5, got ${result}`);
    }
});

runTest('divide with decimals: divide(1, 3) should approximately equal 0.3333', () => {
    const result = divide(1, 3);
    if (Math.abs(result - 0.3333) > 0.0001) {
        throw new Error(`Expected ~0.3333, got ${result}`);
    }
});

// Test error handling
runTest('sum should throw TypeError for non-number inputs', () => {
    try {
        sum('a', 5);
        throw new Error('Should have thrown an error');
    } catch (error) {
        if (!(error instanceof TypeError)) {
            throw new Error(`Expected TypeError, got ${error.constructor.name}`);
        }
    }
});

runTest('divide should throw error for division by zero', () => {
    try {
        divide(5, 0);
        throw new Error('Should have thrown an error');
    } catch (error) {
        if (!error.message.includes('Division by zero')) {
            throw new Error(`Expected division by zero error, got: ${error.message}`);
        }
    }
});

// Print test results
console.log(`\nTest Results: ${testsPassed}/${totalTests} tests passed`);
if (testsPassed === totalTests) {
    console.log('🎉 All tests passed!');
    process.exit(0);
} else {
    console.log('❌ Some tests failed');
    process.exit(1);
}
