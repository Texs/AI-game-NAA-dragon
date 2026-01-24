const { sum } = require('./app');

// Simple test framework implementation
function test(description, fn) {
    try {
        fn();
        console.log(`✓ ${description}`);
    } catch (error) {
        console.log(`✗ ${description}: ${error.message}`);
    }
}

function expect(actual) {
    return {
        toEqual: (expected) => {
            if (actual !== expected) {
                throw new Error(`${actual} does not equal ${expected}`);
            }
        },
        toBeTruthy: () => {
            if (!actual) {
                throw new Error(`${actual} is not truthy`);
            }
        },
        toBeFalsy: () => {
            if (actual) {
                throw new Error(`${actual} is not falsy`);
            }
        },
        toBeCloseTo: (expected, precision = 2) => {
            const multiplier = Math.pow(10, precision);
            const actualRounded = Math.round(actual * multiplier);
            const expectedRounded = Math.round(expected * multiplier);
            
            if (actualRounded !== expectedRounded) {
                throw new Error(`${actual} is not close to ${expected} within precision ${precision}`);
            }
        }
    };
}

// Tests for sum function
test('adds 2 + 3 to equal 5', () => {
    expect(sum(2, 3)).toEqual(5);
});

test('adds -1 + 1 to equal 0', () => {
    expect(sum(-1, 1)).toEqual(0);
});

test('adds 0 + 0 to equal 0', () => {
    expect(sum(0, 0)).toEqual(0);
});

test('adds negative numbers correctly', () => {
    expect(sum(-5, -3)).toEqual(-8);
});

test('handles decimal numbers', () => {
    expect(sum(0.1, 0.2)).toBeCloseTo(0.3, 10); // Using precision to handle floating point arithmetic
});

test('handles decimal numbers with simpler case', () => {
    expect(sum(1.5, 2.5)).toEqual(4.0);
});
        return true;
    } catch (error) {
        console.error(`✗ ${description}: ${error.message}`);
        return false;
    }
}

// Test results tracker
let passedTests = 0;
let totalTests = 0;

function assertEqual(actual, expected, message) {
    totalTests++;
    if (actual !== expected) {
        throw new Error(message || `Expected ${expected}, got ${actual}`);
    }
    passedTests++;
}

// Run tests
console.log('Running tests...\n');

test('should add positive numbers correctly', () => {
    assertEqual(sum(2, 3), 5, '2 + 3 should equal 5');
});

test('should handle negative numbers', () => {
    assertEqual(sum(-1, 1), 0, '-1 + 1 should equal 0');
});

test('should handle decimal numbers', () => {
    assertEqual(sum(2.5, 3.7), 6.2, '2.5 + 3.7 should equal 6.2 (approximately)');
});

test('should handle zero', () => {
    assertEqual(sum(0, 0), 0, '0 + 0 should equal 0');
    assertEqual(sum(5, 0), 5, '5 + 0 should equal 5');
    assertEqual(sum(0, 5), 5, '0 + 5 should equal 5');
});

test('should throw error for invalid inputs', () => {
    try {
        sum('a', 5);
        throw new Error('Should have thrown an error for string input');
    } catch (error) {
        if (error.message !== 'Both arguments must be numbers') {
            throw new Error('Should throw "Both arguments must be numbers" error');
        }
    }
    
    try {
        sum(5, null);
        throw new Error('Should have thrown an error for null input');
    } catch (error) {
        if (error.message !== 'Both arguments must be numbers') {
            throw new Error('Should throw "Both arguments must be numbers" error');
        }
    }
});

// Print results
console.log(`\nResults: ${passedTests}/${totalTests} tests passed`);

if (passedTests !== totalTests) {
    process.exit(1);
} else {
    console.log('All tests passed!');
}
