# AI-game-NAA-dragon
CI/CD project - Mathematical Operations Library

This project demonstrates a comprehensive CI/CD setup with automated testing for both JavaScript and Python applications. It provides basic arithmetic functions with input validation and extensive test coverage.

## Features

- Basic arithmetic operations (addition, subtraction, multiplication, division)
- Input validation with appropriate error handling
- Comprehensive test coverage for both JavaScript and Python implementations
- CI/CD integration for automated testing

## Project Structure

```
├── app.js          # JavaScript implementation
├── app.py          # Python implementation  
├── test.js         # JavaScript tests
├── test.py         # Python tests
├── package.json    # Node.js configuration
├── .eslintrc.json  # JavaScript linting configuration
├── CONTRIBUTING.md # Contribution guidelines
└── README.md       # This file
```

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
const { sum, subtract, multiply, divide } = require('./app');

console.log(sum(2, 3));      // 5
console.log(divide(10, 2));  // 5
```

#### Python
```python
from app import sum, subtract, multiply, divide

print(sum(2, 3))      # 5
print(divide(10, 2))  # 5.0
```

## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License.
