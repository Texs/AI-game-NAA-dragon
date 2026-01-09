/**
 * Demo file to demonstrate the calculator functionality
 */

const calculator = require('./calculator');

console.log('=== Calculator Demo ===');

// Demonstrate all operations
console.log('Sum: 5 + 3 =', calculator.sum(5, 3));
console.log('Subtract: 10 - 4 =', calculator.subtract(10, 4));
console.log('Multiply: 6 * 7 =', calculator.multiply(6, 7));
console.log('Divide: 15 / 3 =', calculator.divide(15, 3));

// Demonstrate error handling
console.log('\n=== Error Handling Demo ===');

try {
    calculator.divide(10, 0);
} catch (error) {
    console.log('Error caught:', error.message);
}

try {
    calculator.sum('hello', 5);
} catch (error) {
    console.log('Error caught:', error.message);
}

console.log('\nDemo completed successfully!');