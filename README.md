# AI-game-NAA-dragon

## Refactored Mathematical Operations Library

This project demonstrates a refactored mathematical operations library with enhanced functionality and improved error handling in both JavaScript and Python.

### Features

- **Basic Math Operations**: Addition, subtraction, multiplication, and division
- **Type Validation**: Ensures both parameters are numbers
- **Error Handling**: Proper error messages for invalid inputs
- **Comprehensive Tests**: Full test coverage for all operations
- **Documentation**: Clear JSDoc/Python docstrings for all functions

### JavaScript Implementation

The JavaScript implementation includes:

- `sum(a, b)`: Adds two numbers
- `subtract(a, b)`: Subtracts b from a
- `multiply(a, b)`: Multiplies two numbers
- `divide(a, b)`: Divides a by b

### Python Implementation

The Python implementation includes:

- `sum(a, b)`: Adds two numbers
- `subtract(a, b)`: Subtracts b from a
- `multiply(a, b)`: Multiplies two numbers
- `divide(a, b)`: Divides a by b

### Testing

To run the tests:

```bash
npm test          # Run both JavaScript and Python tests
npm run test-js   # Run only JavaScript tests
python3 test.py   # Run only Python tests
```

### Original Project Context

This project was originally part of a CI/CD tutorial series:

Part 2: Setting up GitHub Actions and GitLab CI - first workflow and deployment

In the first article, we covered the basics of CI/CD: what it is, why it's needed, and what tools exist. Now it's time to move from theory to practice - let's create our first CI/CD pipelines on GitHub Actions and GitLab CI.

Here's a navigation map between parts:

Part 1: CI/CD Basics - What it is and why it's needed; GitHub Actions and GitLab CI

Part 2: Setting up GitHub Actions and GitLab CI - first workflow and deployment

^ You are here ^

Part 3: CI/CD - branches, conditions, secrets, and environments

Terminology
In the world of CI/CD, many specific terms are used. Here's a brief dictionary to help you better understand documentation and discussions:

Workflow – an automation scenario described in a YAML file on GitHub Actions.

Job – a separate task in a workflow or pipeline that runs on one runner.

Runner – a virtual machine or container on which tasks are executed.

Step – a separate step inside a job, for example, a command or action.

YAML – the file format used to describe workflows and pipelines. Indents in it are critically important!

Script – a section with commands in a GitLab CI file.

Action – a ready-made action on GitHub that you can use in your workflows, for example, actions/checkout.

Stage – a pipeline stage in GitLab, for example, build, test, deploy.

Artifact – a file or set of files created during job execution and saved for use in other jobs or for downloading.

Environment – the environment to which deployment is performed, for example, staging or production.

Don't worry if you don't immediately remember all the terms – they will become clearer with practice.

Results
In this article we:

Created repositories on GitHub and GitLab.
Set up first workflows and pipelines.
Automated deployment of a static website.
Added automatic tests.
Built a complete CI/CD pipeline that checks and publishes code on every change.

Now with every push to the main branch, tests are automatically run, and if they pass successfully, the site updates. The team no longer needs to manually run checks – now errors are visible immediately, and deployment happens automatically.

This is just the beginning of your journey into the world of CI/CD. In the next article, we'll look at more complex scenarios: working with different branches, conditional execution of steps, using secrets for secure storage of sensitive data, and best practices for setting up CI/CD for real projects.

Until next time!

Tags:
github actions
gitlab-ci
cic
devops
automation
