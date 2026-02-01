/**
 * Unit tests for the calculator module
 * Uses a more modern test structure while maintaining the custom framework for now
 */

import { sum, MathOperations } from '../../src/js/calculator.js';

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

function assertThrows(fn, expectedError, message) {
    totalTests++;
    try {
        fn();
        throw new Error(message || `Expected function to throw an error`);
    } catch (error) {
        if (error.constructor.name !== expectedError) {
            throw new Error(message || `Expected error ${expectedError}, got ${error.constructor.name}`);
        }
        passedTests++;
    }
}

// Run tests
console.log('Running calculator tests...\n');

// Test the sum function (backward compatibility)
test('sum should add positive numbers correctly', () => {
    assertEqual(sum(2, 3), 5, '2 + 3 should equal 5');
});

test('sum should handle negative numbers', () => {
    assertEqual(sum(-1, 1), 0, '-1 + 1 should equal 0');
});

test('sum should handle decimal numbers', () => {
    const result = sum(2.5, 3.7);
    // For floating point comparison, we'll check if it's close enough
    if (Math.abs(result - 6.2) > 0.0001) {
        throw new Error(`2.5 + 3.7 should approximately equal 6.2, got ${result}`);
    }
    passedTests++;
    totalTests++;
});

test('sum should handle zero', () => {
    assertEqual(sum(0, 0), 0, '0 + 0 should equal 0');
    assertEqual(sum(5, 0), 5, '5 + 0 should equal 5');
    assertEqual(sum(0, 5), 5, '0 + 5 should equal 5');
});

test('sum should throw error for invalid inputs', () => {
    assertThrows(() => sum('a', 5), 'Error', 'Should throw Error for string input');
    assertThrows(() => sum(5, null), 'Error', 'Should throw Error for null input');
});

// Test the MathOperations class methods
test('MathOperations.add should add positive numbers correctly', () => {
    assertEqual(MathOperations.add(2, 3), 5, '2 + 3 should equal 5');
});

test('MathOperations.subtract should subtract numbers correctly', () => {
    assertEqual(MathOperations.subtract(5, 3), 2, '5 - 3 should equal 2');
});

test('MathOperations.multiply should multiply numbers correctly', () => {
    assertEqual(MathOperations.multiply(3, 4), 12, '3 * 4 should equal 12');
});

test('MathOperations.divide should divide numbers correctly', () => {
    assertEqual(MathOperations.divide(10, 2), 5, '10 / 2 should equal 5');
});

test('MathOperations.divide should throw error when dividing by zero', () => {
    assertThrows(() => MathOperations.divide(10, 0), 'Error', 'Should throw Error when dividing by zero');
});

// Print results
console.log(`\nResults: ${passedTests}/${totalTests} tests passed`);

if (passedTests !== totalTests) {
    process.exit(1);
} else {
    console.log('All tests passed!');
}