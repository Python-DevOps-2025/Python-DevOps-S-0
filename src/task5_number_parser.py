"""
Task 5: Robust number parser and summation (exceptions)

Write sum_numbers_from_lines(lines: list[str]) -> float which accepts lines each containing 
a single number possibly with commas or spaces. Parse each line to float, ignore blank lines, 
and return the total sum.
"""

import re


class ParseError(Exception):
    """Custom exception for parse failures."""
    
    def __init__(self, failed_indices: list[int]):
        self.failed_indices = failed_indices
        super().__init__(f"Failed to parse lines at indices: {failed_indices}")


def sum_numbers_from_lines(lines: list[str]) -> float:
    """
    Parse numbers from lines and return their sum.
    
    Args:
        lines: List of strings, each containing a number
        
    Returns:
        Sum of all successfully parsed numbers
        
    Raises:
        ParseError: If any lines failed to parse (contains failed indices)
    """
    total_sum = 0.0
    failed_indices = []
    
    for i, line in enumerate(lines):
        # Skip blank lines (empty or whitespace only)
        if not line.strip():
            continue
            
        try:
            # Clean the line: remove spaces and commas
            cleaned_line = line.strip().replace(',', '').replace(' ', '')
            
            # Try to parse as float
            number = float(cleaned_line)
            total_sum += number
            
        except ValueError:
            # Record the index of failed parse
            failed_indices.append(i)
    
    # If there were parse failures, raise ParseError
    if failed_indices:
        raise ParseError(failed_indices)
    
    return total_sum


if __name__ == "__main__":
    # Test with the example
    test_lines = ["100", " 2,500.5 ", "", "abc", "3.5"]
    
    try:
        result = sum_numbers_from_lines(test_lines)
        print(f"Sum: {result}")
    except ParseError as e:
        print(f"ParseError raised: {e}")
        print(f"Failed indices: {e.failed_indices}")
    
    # Test with all valid numbers
    valid_lines = ["100", " 2,500.5 ", "", "3.5", "  1,000  "]
    try:
        result = sum_numbers_from_lines(valid_lines)
        print(f"All valid test - Sum: {result}")
    except ParseError as e:
        print(f"Unexpected ParseError: {e}")
    
    # Test with all invalid numbers
    invalid_lines = ["abc", "def", "", "xyz"]
    try:
        result = sum_numbers_from_lines(invalid_lines)
        print(f"All invalid test - Sum: {result}")
    except ParseError as e:
        print(f"All invalid test - ParseError: {e}")
        print(f"Failed indices: {e.failed_indices}")