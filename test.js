const { sum, subtract, multiply, divide } = require('./app');

// Test sum function
try {
    if (sum(2, 3) !== 5) {
        console.error('Test failed: 2 + 3 should equal 5');
        process.exit(1);
    }
    
    if (sum(-1, 1) !== 0) {
        console.error('Test failed: -1 + 1 should equal 0');
        process.exit(1);
    }
    
    if (sum(0, 0) !== 0) {
        console.error('Test failed: 0 + 0 should equal 0');
        process.exit(1);
    }
    
    console.log('✓ Sum tests passed');
} catch (error) {
    console.error('Sum test error:', error.message);
    process.exit(1);
}

// Test subtract function
try {
    if (subtract(5, 3) !== 2) {
        console.error('Test failed: 5 - 3 should equal 2');
        process.exit(1);
    }
    
    if (subtract(0, 5) !== -5) {
        console.error('Test failed: 0 - 5 should equal -5');
        process.exit(1);
    }
    
    if (subtract(-1, -1) !== 0) {
        console.error('Test failed: -1 - (-1) should equal 0');
        process.exit(1);
    }
    
    console.log('✓ Subtract tests passed');
} catch (error) {
    console.error('Subtract test error:', error.message);
    process.exit(1);
}

// Test multiply function
try {
    if (multiply(3, 4) !== 12) {
        console.error('Test failed: 3 * 4 should equal 12');
        process.exit(1);
    }
    
    if (multiply(-2, 3) !== -6) {
        console.error('Test failed: -2 * 3 should equal -6');
        process.exit(1);
    }
    
    if (multiply(0, 100) !== 0) {
        console.error('Test failed: 0 * 100 should equal 0');
        process.exit(1);
    }
    
    console.log('✓ Multiply tests passed');
} catch (error) {
    console.error('Multiply test error:', error.message);
    process.exit(1);
}

// Test divide function
try {
    if (divide(10, 2) !== 5) {
        console.error('Test failed: 10 / 2 should equal 5');
        process.exit(1);
    }
    
    if (divide(-6, 2) !== -3) {
        console.error('Test failed: -6 / 2 should equal -3');
        process.exit(1);
    }
    
    if (Math.abs(divide(7, 3) - 2.33333) < 0.0001) {
        console.log('✓ Divide tests passed');
    } else {
        console.error('Test failed: 7 / 3 should approximately equal 2.33333');
        process.exit(1);
    }
} catch (error) {
    console.error('Divide test error:', error.message);
    process.exit(1);
}

// Test error cases
try {
    // Test division by zero
    try {
        divide(5, 0);
        console.error('Test failed: Division by zero should throw an error');
        process.exit(1);
    } catch (err) {
        if (!(err instanceof Error && err.message === 'Division by zero is not allowed')) {
            console.error('Test failed: Wrong error message for division by zero');
            process.exit(1);
        }
    }
    
    // Test type validation
    try {
        sum("not a number", 5);
        console.error('Test failed: Non-number inputs should throw an error');
        process.exit(1);
    } catch (err) {
        if (!(err instanceof TypeError)) {
            console.error('Test failed: Wrong error type for non-number inputs');
            process.exit(1);
        }
    }
    
    console.log('✓ Error handling tests passed');
} catch (error) {
    console.error('Error handling test error:', error.message);
    process.exit(1);
}

console.log('\n🎉 All tests passed successfully!');
