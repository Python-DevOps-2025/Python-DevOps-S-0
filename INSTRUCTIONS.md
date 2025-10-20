# Python DevOps S-0 - Setup and Usage Instructions

## Project Overview

This project contains solutions for 6 Python programming tasks demonstrating various concepts including:
- List operations and statistics
- String filtering and transformation
- Regular expressions for text processing
- Email validation with regex
- Exception handling and custom exceptions
- Data structures (stacks) for bracket matching

## Project Structure

```
Python-DevOps-S-0/
├── README.md                 # Original task descriptions
├── INSTRUCTIONS.md           # This file - setup and usage guide
├── requirements.txt          # Python dependencies
├── setup.py                  # Package setup configuration
├── pytest.ini              # Pytest configuration
├── main.py                  # Demonstration script for all solutions
├── run_tests.py             # Test runner script
├── venv/                    # Virtual environment (created during setup)
├── src/                     # Source code directory
│   ├── __init__.py
│   ├── task1_list_stats.py
│   ├── task2_filter_transform.py
│   ├── task3_word_frequency.py
│   ├── task4_email_validator.py
│   ├── task5_number_parser.py
│   └── task6_parentheses_checker.py
└── tests/                   # Test directory
    ├── __init__.py
    ├── test_task1.py
    ├── test_task2.py
    ├── test_task3.py
    ├── test_task4.py
    ├── test_task5.py
    └── test_task6.py
```

## Setup Instructions

### Prerequisites
- Python 3.11 or higher (Python 3.13.3 recommended)
- Git (for cloning the repository)

### Installation Steps

1. **Clone the repository** (if not already done):
   ```powershell
   git clone https://github.com/mehalyna/Python-DevOps-S-0.git
   cd Python-DevOps-S-0
   ```

2. **Create and activate virtual environment**:
   ```powershell
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment (Windows PowerShell)
   .\venv\Scripts\Activate.ps1
   
   # For Command Prompt use:
   # venv\Scripts\activate.bat
   
   # For Git Bash use:
   # source venv/Scripts/activate
   ```

3. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

4. **Verify installation**:
   ```powershell
   python --version
   pip list
   ```

## Running the Solutions

### Quick Demo
Run the main demonstration script to see all solutions in action:
```powershell
python main.py
```

### Individual Task Examples
You can run individual task files to see specific examples:
```powershell
# Task 1: List Statistics
python src/task1_list_stats.py

# Task 2: Filter and Transform
python src/task2_filter_transform.py

# Task 3: Word Frequency
python src/task3_word_frequency.py

# Task 4: Email Validator
python src/task4_email_validator.py

# Task 5: Number Parser
python src/task5_number_parser.py

# Task 6: Parentheses Checker
python src/task6_parentheses_checker.py
```

## Running Tests

### All Tests
Run the complete test suite:
```powershell
# Using pytest
python -m pytest tests/ -v

# Using custom test runner
python run_tests.py

# Individual task tests
python run_tests.py individual
```

### Test Coverage
Generate test coverage report:
```powershell
python -m pytest tests/ --cov=src --cov-report=html
```

### Specific Test Files
Run tests for specific tasks:
```powershell
python -m pytest tests/test_task1.py -v
python -m pytest tests/test_task2.py -v
# ... etc
```

## Development Tools

### Code Formatting
Format code using Black:
```powershell
black src/ tests/
```

### Linting
Check code quality with flake8:
```powershell
flake8 src/ tests/
```

### Type Checking
Run type checking with mypy:
```powershell
mypy src/
```

## Task Descriptions

For detailed task descriptions and requirements, see [README.md](README.md).

### Quick Summary:
1. **Task 1**: Calculate statistics (min, max, sum, avg, unique_count) for a list of integers
2. **Task 2**: Filter words by length, convert to lowercase, and sort alphabetically
3. **Task 3**: Find top N most frequent words in text using regex
4. **Task 4**: Validate email addresses using regex and basic checks
5. **Task 5**: Parse numbers from strings with error handling and custom exceptions
6. **Task 6**: Check if parentheses, brackets, and braces are balanced

## Solution Features

### Task 1 - List Statistics
- Manual implementation of min/max/sum (no built-ins)
- Proper error handling for empty lists
- Accurate average calculation with rounding

### Task 2 - Filter Transform
- Manual sorting implementation (bubble sort)
- Proper string filtering and transformation
- Case-insensitive alphabetical ordering

### Task 3 - Word Frequency
- Regex-based word extraction
- Manual frequency counting
- Tie-breaking by alphabetical order

### Task 4 - Email Validator
- Regex pattern validation
- Multiple validation criteria
- Proper error handling for non-list inputs

### Task 5 - Number Parser
- Custom ParseError exception
- Robust number parsing with comma/space handling
- Continue-on-error processing with index tracking

### Task 6 - Parentheses Checker
- Stack-based algorithm
- Support for multiple bracket types: (), [], {}
- Proper nesting validation

## Testing Strategy

Each task has comprehensive test coverage including:
- Example cases from requirements
- Edge cases (empty inputs, boundary conditions)
- Error conditions
- Various input combinations

Total test count: **57 tests** across all tasks.

## Dependencies

### Production Dependencies
- No external dependencies (uses only Python standard library)

### Development Dependencies
- `pytest>=7.0.0` - Testing framework
- `pytest-cov>=4.0.0` - Coverage reporting
- `black>=23.0.0` - Code formatting
- `flake8>=6.0.0` - Linting
- `mypy>=1.0.0` - Type checking

## Environment Information

- **Python Version**: 3.13.3 (recommended)
- **Virtual Environment**: Located in `venv/` directory
- **Package Management**: pip
- **Testing Framework**: pytest
- **Code Style**: Black formatter

## Troubleshooting

### Common Issues

1. **Virtual environment not activated**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

2. **Import errors when running tests**:
   - Ensure virtual environment is activated
   - Verify all dependencies are installed: `pip install -r requirements.txt`

3. **Python path issues**:
   - Run commands from the project root directory
   - Ensure `src/` and `tests/` directories are present

4. **PowerShell execution policy**:
   If you get execution policy errors:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```

### Getting Help

1. Check that all files are in the correct directory structure
2. Verify Python version compatibility
3. Ensure virtual environment is properly activated
4. Check that all dependencies are installed

## License

This project is for educational purposes as part of the Python DevOps S-0 course.