/**
 * Module for basic mathematical operations
 */
class MathOperations {
    /**
     * Adds two numbers together
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Sum of a and b
     */
    static add(a, b) {
        // Input validation
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Both arguments must be numbers');
        }
        return a + b;
    }

    /**
     * Subtracts b from a
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Difference of a and b
     */
    static subtract(a, b) {
        // Input validation
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Both arguments must be numbers');
        }
        return a - b;
    }

    /**
     * Multiplies two numbers
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Product of a and b
     */
    static multiply(a, b) {
        // Input validation
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Both arguments must be numbers');
        }
        return a * b;
    }

    /**
     * Divides a by b
     * @param {number} a - First number
     * @param {number} b - Second number
     * @returns {number} Quotient of a and b
     */
    static divide(a, b) {
        // Input validation
        if (typeof a !== 'number' || typeof b !== 'number') {
            throw new Error('Both arguments must be numbers');
        }
        
        if (b === 0) {
            throw new Error('Division by zero is not allowed');
        }
        
        return a / b;
    }
}

export default MathOperations;