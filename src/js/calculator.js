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

export { sum, MathOperations };