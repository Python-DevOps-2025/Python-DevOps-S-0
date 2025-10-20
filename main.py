"""
Main demonstration script for all tasks
This script runs examples for each task to show the solutions work correctly.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from task1_list_stats import list_stats
from task2_filter_transform import filter_transform
from task3_word_frequency import top_words
from task4_email_validator import validate_emails
from task5_number_parser import sum_numbers_from_lines, ParseError
from task6_parentheses_checker import is_balanced


def demonstrate_task1():
    """Demonstrate Task 1: List Statistics"""
    print("TASK 1: List Statistics")
    print("=" * 40)
    
    # Example from requirements
    test_input = [3, 5, 3, 10, -1]
    result = list_stats(test_input)
    print(f"Input: {test_input}")
    print(f"Output: {result}")
    print(f"Expected: {{'min': -1, 'max': 10, 'sum': 20, 'avg': 4.00, 'unique_count': 4}}")
    
    # Test empty list error
    try:
        list_stats([])
    except ValueError as e:
        print(f"Empty list correctly raises ValueError: {e}")
    
    print()


def demonstrate_task2():
    """Demonstrate Task 2: Filter and Transform"""
    print("TASK 2: Filter and Transform Strings")
    print("=" * 40)
    
    # Example from requirements
    test_words = ["Hello", "to", "WORLD", "py"]
    min_length = 2
    result = filter_transform(test_words, min_length)
    print(f"Input: {test_words}, min_len: {min_length}")
    print(f"Output: {result}")
    print(f"Expected: ['hello', 'world']")
    
    print()


def demonstrate_task3():
    """Demonstrate Task 3: Word Frequency"""
    print("TASK 3: Word Frequency (Regex)")
    print("=" * 40)
    
    # Example from requirements
    test_text = "Hello, hello! This is a test. Test; test?"
    result = top_words(test_text, 2)
    print(f"Input: '{test_text}', n=2")
    print(f"Output: {result}")
    print(f"Expected: [('test', 3), ('hello', 2)]")
    
    print()


def demonstrate_task4():
    """Demonstrate Task 4: Email Validator"""
    print("TASK 4: Email Validator (Regex)")
    print("=" * 40)
    
    # Example from requirements
    test_emails = ["user@example.com", "bad@@x", "no-at-sign.com"]
    result = validate_emails(test_emails)
    print(f"Input: {test_emails}")
    print(f"Output: {result}")
    print(f"Expected: {{'valid': ['user@example.com'], 'invalid': ['bad@@x', 'no-at-sign.com']}}")
    
    # Test TypeError
    try:
        validate_emails("not a list")
    except TypeError as e:
        print(f"Non-list input correctly raises TypeError: {e}")
    
    print()


def demonstrate_task5():
    """Demonstrate Task 5: Number Parser"""
    print("TASK 5: Robust Number Parser (Exceptions)")
    print("=" * 40)
    
    # Example from requirements
    test_lines = ["100", " 2,500.5 ", "", "abc", "3.5"]
    print(f"Input: {test_lines}")
    
    try:
        result = sum_numbers_from_lines(test_lines)
        print(f"Sum: {result}")
    except ParseError as e:
        print(f"ParseError correctly raised: {e}")
        print(f"Failed indices: {e.failed_indices}")
        print("Expected: ParseError([3]) - 'abc' at index 3 cannot be parsed")
    
    # Test with all valid numbers
    valid_lines = ["100", " 2,500.5 ", "", "3.5"]
    try:
        result = sum_numbers_from_lines(valid_lines)
        print(f"Valid lines sum: {result}")
        print(f"Expected: {100 + 2500.5 + 3.5}")
    except ParseError as e:
        print(f"Unexpected ParseError: {e}")
    
    print()


def demonstrate_task6():
    """Demonstrate Task 6: Parentheses Checker"""
    print("TASK 6: Parentheses Balance Checker")
    print("=" * 40)
    
    # Examples from requirements
    test_cases = [
        ("{[()]}()", True),
        ("(unbalanced]", False),
        ("", True),
        ("Hello (world) [test]!", True),
        ("([)]", False),
        ("((()))", True),
        ("((())", False)
    ]
    
    for test_input, expected in test_cases:
        result = is_balanced(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{test_input}' -> {result} (expected: {expected})")
    
    print()


def main():
    """Run all demonstrations"""
    print("Python DevOps S-0 - Solution Demonstrations")
    print("=" * 60)
    print()
    
    demonstrate_task1()
    demonstrate_task2()
    demonstrate_task3()
    demonstrate_task4()
    demonstrate_task5()
    demonstrate_task6()
    
    print("All demonstrations completed!")
    print("Run 'python run_tests.py' to execute the full test suite.")


if __name__ == "__main__":
    main()