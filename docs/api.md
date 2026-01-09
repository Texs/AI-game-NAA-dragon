# API Documentation

## JavaScript Calculator API

### Functions

#### `sum(a, b)`
Adds two numbers together.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The sum of a and b
- **Throws**: `TypeError` if either argument is not a number

#### `subtract(a, b)`
Subtracts the second number from the first.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The difference of a and b
- **Throws**: `TypeError` if either argument is not a number

#### `multiply(a, b)`
Multiplies two numbers together.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The product of a and b
- **Throws**: `TypeError` if either argument is not a number

#### `divide(a, b)`
Divides the first number by the second.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The quotient of a and b
- **Throws**: 
  - `TypeError` if either argument is not a number
  - `Error` if attempting to divide by zero

## Python Calculator API

### Functions

#### `sum(a, b)`
Adds two numbers together.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The sum of a and b
- **Raises**: `TypeError` if either argument is not a number

#### `subtract(a, b)`
Subtracts the second number from the first.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The difference of a and b
- **Raises**: `TypeError` if either argument is not a number

#### `multiply(a, b)`
Multiplies two numbers together.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The product of a and b
- **Raises**: `TypeError` if either argument is not a number

#### `divide(a, b)`
Divides the first number by the second.

- **Parameters**:
  - `a` (number): The first number
  - `b` (number): The second number
- **Returns**: `number` - The quotient of a and b
- **Raises**: 
  - `TypeError` if either argument is not a number
  - `ZeroDivisionError` if attempting to divide by zero