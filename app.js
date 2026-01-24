/**
 * Main calculator module
 * Provides backward compatibility while using the new modular structure
 */

// Import from new structure to maintain modularity
import { sum } from './src/js/calculator.js';

// For CommonJS compatibility in older Node environments
export default { sum };
export { sum };
