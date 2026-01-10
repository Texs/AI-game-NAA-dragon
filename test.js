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
