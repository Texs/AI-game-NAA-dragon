/**
 * Calculator module tests
 */

const calculator = require('../../src/js/calculator');

// Test sum function
console.log('Testing sum function...');

try {
    if (calculator.sum(2, 3) !== 5) {
        console.error('Test failed: 2 + 3 should equal 5');
        process.exit(1);
    }
    console.log('✓ sum(2, 3) === 5');

    if (calculator.sum(-1, 1) !== 0) {
        console.error('Test failed: -1 + 1 should equal 0');
        process.exit(1);
    }
    console.log('✓ sum(-1, 1) === 0');

    if (calculator.sum(0, 0) !== 0) {
        console.error('Test failed: 0 + 0 should equal 0');
        process.exit(1);
    }
    console.log('✓ sum(0, 0) === 0');

    // Test error handling
    try {
        calculator.sum('a', 5);
        console.error('Test failed: sum should throw TypeError for non-number input');
        process.exit(1);
    } catch (error) {
        if (!(error instanceof TypeError)) {
            console.error('Test failed: sum should throw TypeError for non-number input');
            process.exit(1);
        }
        console.log('✓ sum throws TypeError for non-number input');
    }

} catch (error) {
    console.error('Test failed with error:', error.message);
    process.exit(1);
}

// Test subtract function
console.log('\nTesting subtract function...');

try {
    if (calculator.subtract(5, 3) !== 2) {
        console.error('Test failed: 5 - 3 should equal 2');
        process.exit(1);
    }
    console.log('✓ subtract(5, 3) === 2');

    if (calculator.subtract(0, 5) !== -5) {
        console.error('Test failed: 0 - 5 should equal -5');
        process.exit(1);
    }
    console.log('✓ subtract(0, 5) === -5');

} catch (error) {
    console.error('Test failed with error:', error.message);
    process.exit(1);
}

// Test multiply function
console.log('\nTesting multiply function...');

try {
    if (calculator.multiply(3, 4) !== 12) {
        console.error('Test failed: 3 * 4 should equal 12');
        process.exit(1);
    }
    console.log('✓ multiply(3, 4) === 12');

    if (calculator.multiply(-2, 3) !== -6) {
        console.error('Test failed: -2 * 3 should equal -6');
        process.exit(1);
    }
    console.log('✓ multiply(-2, 3) === -6');

} catch (error) {
    console.error('Test failed with error:', error.message);
    process.exit(1);
}

// Test divide function
console.log('\nTesting divide function...');

try {
    if (calculator.divide(10, 2) !== 5) {
        console.error('Test failed: 10 / 2 should equal 5');
        process.exit(1);
    }
    console.log('✓ divide(10, 2) === 5');

    if (calculator.divide(7, 2) !== 3.5) {
        console.error('Test failed: 7 / 2 should equal 3.5');
        process.exit(1);
    }
    console.log('✓ divide(7, 2) === 3.5');

    // Test division by zero
    try {
        calculator.divide(5, 0);
        console.error('Test failed: divide should throw error for division by zero');
        process.exit(1);
    } catch (error) {
        if (error.message !== 'Cannot divide by zero') {
            console.error('Test failed: divide should throw "Cannot divide by zero" error');
            process.exit(1);
        }
        console.log('✓ divide throws error for division by zero');
    }

} catch (error) {
    console.error('Test failed with error:', error.message);
    process.exit(1);
}

console.log('\nAll tests passed! ✓');