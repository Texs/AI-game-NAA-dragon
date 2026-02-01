/**
 * Mathematical operations library
 * Provides basic arithmetic functions with input validation
 */

/**
 * Adds two numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Sum of a and b
 * @throws {TypeError} If either argument is not a number
 */
function sum(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a + b;
}

/**
 * Subtracts second number from first
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Difference of a and b
 * @throws {TypeError} If either argument is not a number
 */
function subtract(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a - b;
}

/**
 * Multiplies two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Product of a and b
 * @throws {TypeError} If either argument is not a number
 */
function multiply(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a * b;
}

/**
 * Divides first number by second
 * @param {number} a - First number (dividend)
 * @param {number} b - Second number (divisor)
 * @returns {number} Quotient of a divided by b
 * @throws {TypeError} If either argument is not a number
 * @throws {Error} If divisor is zero
 */
function divide(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    if (b === 0) {
        throw new Error('Division by zero is not allowed');
    }
    return a / b;
}

module.exports = {
    sum,
    subtract,
    multiply,
    divide
};
 * Main calculator module
 * Provides backward compatibility while using the new modular structure
 */

// Import from new structure to maintain modularity
import { sum } from './src/js/calculator.js';

// For CommonJS compatibility in older Node environments
export default { sum };
export { sum };
