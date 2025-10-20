"""
Test suite for Task 5: Robust number parser and summation
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task5_number_parser import sum_numbers_from_lines, ParseError


class TestSumNumbersFromLines(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example - should raise ParseError."""
        lines = ["100", " 2,500.5 ", "", "abc", "3.5"]
        with self.assertRaises(ParseError) as context:
            sum_numbers_from_lines(lines)
        
        # Check that failed indices are correct
        self.assertEqual(context.exception.failed_indices, [3])
    
    def test_all_valid_numbers(self):
        """Test with all valid numbers."""
        lines = ["100", " 2,500.5 ", "", "3.5", "  1,000  "]
        result = sum_numbers_from_lines(lines)
        expected = 100 + 2500.5 + 3.5 + 1000
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        """Test with empty list."""
        result = sum_numbers_from_lines([])
        self.assertEqual(result, 0.0)
    
    def test_only_blank_lines(self):
        """Test with only blank lines."""
        lines = ["", "   ", "\t", "\n"]
        result = sum_numbers_from_lines(lines)
        self.assertEqual(result, 0.0)
    
    def test_all_invalid_numbers(self):
        """Test with all invalid numbers."""
        lines = ["abc", "def", "xyz"]
        with self.assertRaises(ParseError) as context:
            sum_numbers_from_lines(lines)
        self.assertEqual(context.exception.failed_indices, [0, 1, 2])
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        lines = ["-100", "-2.5", "50"]
        result = sum_numbers_from_lines(lines)
        expected = -100 + (-2.5) + 50
        self.assertEqual(result, expected)
    
    def test_numbers_with_commas(self):
        """Test numbers with comma formatting."""
        lines = ["1,000", "2,500.75", "10,000,000"]
        result = sum_numbers_from_lines(lines)
        expected = 1000 + 2500.75 + 10000000
        self.assertEqual(result, expected)
    
    def test_numbers_with_spaces(self):
        """Test numbers with spaces."""
        lines = [" 100 ", "  -25.5  ", "1 , 000"]
        result = sum_numbers_from_lines(lines)
        expected = 100 + (-25.5) + 1000
        self.assertEqual(result, expected)
    
    def test_mixed_valid_invalid_with_blanks(self):
        """Test mix of valid, invalid, and blank lines."""
        lines = ["100", "", "invalid", "200.5", "   ", "also_invalid", "50"]
        with self.assertRaises(ParseError) as context:
            sum_numbers_from_lines(lines)
        
        # Should fail on indices 2 and 5
        self.assertEqual(context.exception.failed_indices, [2, 5])
    
    def test_scientific_notation(self):
        """Test with scientific notation."""
        lines = ["1e2", "2.5e-1", "invalid"]
        with self.assertRaises(ParseError) as context:
            sum_numbers_from_lines(lines)
        
        # Should fail on index 2 only
        self.assertEqual(context.exception.failed_indices, [2])
    
    def test_zero_values(self):
        """Test with zero values."""
        lines = ["0", "0.0", "-0", "+0"]
        result = sum_numbers_from_lines(lines)
        self.assertEqual(result, 0.0)
    
    def test_parse_error_message(self):
        """Test ParseError message format."""
        lines = ["valid", "invalid"]
        with self.assertRaises(ParseError) as context:
            sum_numbers_from_lines(lines)
        
        error_message = str(context.exception)
        self.assertIn("Failed to parse lines at indices", error_message)
        self.assertIn("[0, 1]", error_message)


if __name__ == "__main__":
    unittest.main()