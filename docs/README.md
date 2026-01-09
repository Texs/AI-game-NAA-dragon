# AI-game-NAA-dragon - Refactored

## Overview
This is a refactored version of the CI/CD demonstration project. The original simple implementation has been enhanced with better structure, comprehensive functionality, and improved testing.

## Project Structure
```
/workspace/
├── src/
│   ├── js/
│   │   └── calculator.js          # JavaScript implementation
│   └── python/
│       └── calculator.py          # Python implementation
├── tests/
│   ├── js/
│   │   └── calculator.test.js     # JavaScript tests
│   └── python/
│       └── calculator.test.py     # Python tests
├── docs/                         # Documentation
├── index.html                    # Main HTML page
├── package.json                  # Node.js configuration
└── README.md                     # This file
```

## Features Added
- Enhanced calculator with four operations: sum, subtract, multiply, divide
- Input validation and error handling
- Comprehensive test suites for both JS and Python
- Better documentation and code organization
- Proper error handling for edge cases like division by zero

## Running Tests
### JavaScript
```bash
npm test
# or
npm run test:js
```

### Python
```bash
python tests/python/calculator.test.py
```

## License
MIT