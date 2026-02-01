# Mathematical Operations Library

This project demonstrates a comprehensive CI/CD setup with automated testing for both JavaScript and Python applications. It provides basic arithmetic functions with input validation and extensive test coverage.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Input validation with appropriate error handling
- Comprehensive test coverage for both JavaScript and Python implementations
- CI/CD integration for automated testing
- **NEW: Modular Architecture**: Clean separation of concerns with refactored codebase

## Project Structure

```
├── app.js          # JavaScript implementation (now uses modular structure)
├── app.py          # Python implementation (now uses modular structure)
├── test.js         # JavaScript test runner
├── test.py         # Python test runner
├── src/            # Source modules
│   ├── js/
│   │   ├── calculator.js  # Calculator wrapper functions
│   │   └── math.js        # Core MathOperations class
│   └── py/
│       └── math_operations.py  # Python MathOperations class
├── tests/          # Dedicated test files
│   ├── js/
│   │   └── calculator.test.js  # JavaScript unit tests
│   └── py/
│       └── test_math_operations.py  # Python unit tests
├── package.json    # Node.js configuration
├── .eslintrc.json  # JavaScript linting configuration
├── CONTRIBUTING.md # Contribution guidelines
└── README.md       # This file
```

## Refactoring Summary

During the refactoring process, several key improvements were made:

1. **Consolidated Code**: Removed duplicate implementations and centralized logic in the `src/` directory
2. **Fixed Package Configuration**: Corrected malformed package.json with proper syntax
3. **Improved Modularity**: Better separation between core logic and API interfaces
4. **Enhanced Documentation**: Added JSDoc/Python docstrings to all functions
5. **Unified API**: Consistent function names and signatures across languages
6. **Better Error Handling**: Consistent error types and messages
7. **Cleaner Test Structure**: Organized tests into dedicated directories with separate test files
8. **Backward Compatibility**: Maintained API compatibility while improving internal structure

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- Python (v3.6 or higher)

### Installation
1. Clone the repository
2. Navigate to the project directory
3. Install dependencies (if any): `npm install`

## Usage

### Running JavaScript Tests
```bash
npm test
```

### Running Python Tests
```bash
python test.py
```

Or using npm script:
```bash
npm run test:py
```

### Using the Library

#### JavaScript
```javascript
import { sum, subtract, multiply, divide } from './app.js';

console.log(sum(2, 3));      // 5
console.log(divide(10, 2));  // 5
```

#### Python
```python
from app import sum, subtract, multiply, divide

print(sum(2, 3))      # 5
print(divide(10, 2))  # 5.0
```

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License.