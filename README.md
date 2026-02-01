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

# AI-game-NAA-dragon
CI/CD project
Часть 2: Настройка GitHub Actions и GitLab CI – первый workflow и деплой

CI/CD project demonstrating automated workflows with GitHub Actions and GitLab CI.

## Overview

This project demonstrates how to set up CI/CD pipelines for both GitHub Actions and GitLab CI. It includes automated testing, building, and deployment processes that trigger on code changes.

## Features

- JavaScript and Python application code
- Automated testing for both languages
- Static site deployment
- Code quality enforcement with ESLint
- Security auditing capabilities

## Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)
- Python (v3.6 or higher)

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd ai-game-naa-dragon
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

### Running Tests

To run JavaScript tests:
```bash
npm test
```

To run Python tests:
```bash
python test.py
```

### Additional Scripts

- Start the application: `npm start`
- Lint JavaScript code: `npm run lint`
- Audit security vulnerabilities: `npm run security-audit`

## Project Structure

- `app.js` - Main JavaScript application logic with input validation
- `app.py` - Main Python application logic with input validation
- `test.js` - Comprehensive JavaScript unit tests
- `test.py` - Comprehensive Python unit tests
- `index.html` - Main HTML page for the CI/CD project
- `package.json` - Node.js package configuration
- `.eslintrc.json` - ESLint configuration for code quality
- `README.md` - Project documentation
- `CONTRIBUTING.md` - Contribution guidelines

## CI/CD Pipeline

The project implements a CI/CD pipeline that:
1. Runs tests on code changes
2. Validates code quality
3. Performs security audits
4. Deploys the static site automatically when tests pass

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Это только начало вашего путешествия в мир CI/CD. В следующей статье мы рассмотрим более сложные сценарии: работу с разными ветками, условное выполнение шагов, использование секретов для безопасного хранения чувствительных данных и лучшие практики настройки CI/CD для реальных проектов.

А пока – экспериментируйте с тем, что вы узнали сегодня. Добавьте больше тестов, попробуйте другие actions, настройте деплой для своего проекта. Практика – лучший способ закрепить знания.

До встречи в следующей статье!

Теги:
github actions
gitlab-ci
cic
devops
automation
Хабы:DevOpsGitHubPythonJavaScript
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on how to contribute to this project.

## License

This project is licensed under the MIT License.
- Part 2: Setting up GitHub Actions and GitLab CI - first workflow and deployment
- Based on CI/CD fundamentals and best practices
