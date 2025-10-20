"""
Test suite for Task 2: Filter and transform strings
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task2_filter_transform import filter_transform


class TestFilterTransform(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example."""
        input_words = ["Hello", "to", "WORLD", "py"]
        result = filter_transform(input_words, 2)
        expected = ["hello", "world"]
        self.assertEqual(result, expected)
    
    def test_empty_list(self):
        """Test with empty list."""
        result = filter_transform([], 1)
        self.assertEqual(result, [])
    
    def test_no_words_pass_filter(self):
        """Test when no words pass the length filter."""
        result = filter_transform(["a", "b", "c"], 5)
        self.assertEqual(result, [])
    
    def test_all_words_pass_filter(self):
        """Test when all words pass the filter."""
        result = filter_transform(["hello", "world", "python"], 1)
        expected = ["hello", "python", "world"]  # alphabetically sorted
        self.assertEqual(result, expected)
    
    def test_case_conversion(self):
        """Test proper case conversion."""
        result = filter_transform(["UPPER", "lower", "MiXeD"], 3)
        expected = ["lower", "mixed", "upper"]
        self.assertEqual(result, expected)
    
    def test_alphabetical_sorting(self):
        """Test alphabetical sorting."""
        result = filter_transform(["zebra", "apple", "banana"], 3)
        expected = ["apple", "banana", "zebra"]
        self.assertEqual(result, expected)
    
    def test_exact_length_boundary(self):
        """Test boundary condition with exact length."""
        result = filter_transform(["abc", "ab", "abcd"], 2)
        expected = ["abc", "abcd"]  # "ab" is not > 2, "abc" and "abcd" are
        self.assertEqual(result, expected)
    
    def test_special_characters(self):
        """Test with special characters in words."""
        result = filter_transform(["hello!", "world?", "test"], 3)
        expected = ["hello!", "test", "world?"]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()