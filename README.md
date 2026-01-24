# AI-game-NAA-dragon

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

- Part 2: Setting up GitHub Actions and GitLab CI - first workflow and deployment
- Based on CI/CD fundamentals and best practices
