/**
 * Calculator module - provides basic mathematical operations
 * @module calculator
 */

/**
 * Adds two numbers together
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The sum of a and b
 * @throws {TypeError} If either argument is not a number
 */
function sum(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a + b;
}

/**
 * Subtracts the second number from the first
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The difference of a and b
 * @throws {TypeError} If either argument is not a number
 */
function subtract(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a - b;
}

/**
 * Multiplies two numbers together
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The product of a and b
 * @throws {TypeError} If either argument is not a number
 */
function multiply(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    return a * b;
}

/**
 * Divides the first number by the second
 * @param {number} a - The first number
 * @param {number} b - The second number
 * @returns {number} The quotient of a and b
 * @throws {TypeError} If either argument is not a number
 * @throws {Error} If attempting to divide by zero
 */
function divide(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both arguments must be numbers');
    }
    if (b === 0) {
        throw new Error('Cannot divide by zero');
    }
    return a / b;
}

module.exports = {
    sum,
    subtract,
    multiply,
    divide
};