# SP - Skills Practice

A Python utility library designed to enhance coding skills through practical examples and clean code practices.

## Overview

This project demonstrates good Python coding practices including:
- Modular code organization
- Comprehensive documentation
- Unit testing with pytest
- Type hints
- Error handling
- Command-line interface

## Project Structure

```
SP/
├── src/                    # Source code
│   ├── __init__.py        # Package initialization
│   ├── string_utils.py    # String manipulation utilities
│   └── math_utils.py      # Mathematical utilities
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_string_utils.py
│   └── test_math_utils.py
├── cli.py                 # Command-line interface
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
```

## Features

### String Utilities
- **reverse_string**: Reverse any string
- **is_palindrome**: Check if a string is a palindrome
- **count_vowels**: Count vowels in a string
- **capitalize_words**: Capitalize first letter of each word

### Math Utilities
- **factorial**: Calculate factorial of a number
- **is_prime**: Check if a number is prime
- **fibonacci**: Generate Fibonacci sequence

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SpFerrari786/SP.git
cd SP
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### As a Library

```python
from src.string_utils import reverse_string, is_palindrome
from src.math_utils import factorial, fibonacci

# String operations
print(reverse_string("hello"))  # Output: olleh
print(is_palindrome("racecar"))  # Output: True

# Math operations
print(factorial(5))  # Output: 120
print(fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### Using the CLI

```bash
# String commands
python cli.py reverse "hello world"
python cli.py palindrome "racecar"
python cli.py vowels "hello world"
python cli.py capitalize "hello world"

# Math commands
python cli.py factorial 5
python cli.py prime 7
python cli.py fibonacci 10

# Get help
python cli.py help
```

## Running Tests

Run all tests:
```bash
pytest tests/
```

Run specific test file:
```bash
pytest tests/test_string_utils.py
pytest tests/test_math_utils.py
```

Run with verbose output:
```bash
pytest tests/ -v
```

## Development

This project is designed for learning and practicing:
- Clean code principles
- Test-driven development (TDD)
- Python best practices
- Documentation standards
- Git workflow

## Future Enhancements

Potential additions to expand this project:
- Data structure implementations (stacks, queues, trees)
- Sorting and searching algorithms
- File I/O utilities
- API integration examples
- Database operations
- Web scraping utilities

## Contributing

This is a personal learning project. Feel free to fork and experiment!

## License

This project is open source and available for educational purposes.
