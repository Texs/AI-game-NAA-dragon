/**
 * Adds two numbers together
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The sum of a and b
 * @throws {TypeError} If either parameter is not a number
 */
function sum(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both parameters must be numbers');
    }
    return a + b;
}

/**
 * Subtracts b from a
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The difference of a and b
 * @throws {TypeError} If either parameter is not a number
 */
function subtract(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both parameters must be numbers');
    }
    return a - b;
}

/**
 * Multiplies two numbers
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The product of a and b
 * @throws {TypeError} If either parameter is not a number
 */
function multiply(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both parameters must be numbers');
    }
    return a * b;
}

/**
 * Divides a by b
 * @param {number} a - First number
 * @param {number} b - Second number
 * @returns {number} The quotient of a and b
 * @throws {TypeError} If either parameter is not a number
 * @throws {Error} If b is zero
 */
function divide(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        throw new TypeError('Both parameters must be numbers');
    }
    if (b === 0) {
        throw new Error('Division by zero is not allowed');
    }
    return a / b;
}

module.exports = { sum, subtract, multiply, divide };
