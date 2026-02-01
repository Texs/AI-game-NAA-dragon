/**
 * Calculator module providing backward compatibility with original API
 */
import MathOperations from './math.js';

/**
 * Adds two numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Sum of a and b
 */
function sum(a, b) {
    return MathOperations.add(a, b);
}

/**
 * Subtracts second number from first
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Difference of a and b
 */
function subtract(a, b) {
    return MathOperations.subtract(a, b);
}

/**
 * Multiplies two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} Product of a and b
 */
function multiply(a, b) {
    return MathOperations.multiply(a, b);
}

/**
 * Divides first number by second
 * @param {number} a - First number (dividend)
 * @param {number} b - Second number (divisor)
 * @returns {number} Quotient of a divided by b
 */
function divide(a, b) {
    return MathOperations.divide(a, b);
}

export { sum, subtract, multiply, divide, MathOperations };