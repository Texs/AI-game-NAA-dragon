const { sum } = require('./app');

// Simple test framework implementation
function test(description, fn) {
    try {
        fn();
        console.log(`✓ ${description}`);
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
