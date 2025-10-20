"""
Test suite for Task 1: List statistics
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task1_list_stats import list_stats


class TestListStats(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example."""
        input_list = [3, 5, 3, 10, -1]
        expected = {"min": -1, "max": 10, "sum": 20, "avg": 4.00, "unique_count": 4}
        result = list_stats(input_list)
        self.assertEqual(result, expected)
    
    def test_empty_list_raises_error(self):
        """Test that empty list raises ValueError."""
        with self.assertRaises(ValueError) as context:
            list_stats([])
        self.assertIn("empty list", str(context.exception).lower())
    
    def test_single_element(self):
        """Test with single element."""
        result = list_stats([42])
        expected = {"min": 42, "max": 42, "sum": 42, "avg": 42.00, "unique_count": 1}
        self.assertEqual(result, expected)
    
    def test_all_same_elements(self):
        """Test with all identical elements."""
        result = list_stats([5, 5, 5, 5])
        expected = {"min": 5, "max": 5, "sum": 20, "avg": 5.00, "unique_count": 1}
        self.assertEqual(result, expected)
    
    def test_negative_numbers(self):
        """Test with negative numbers."""
        result = list_stats([-5, -2, -10, -1])
        expected = {"min": -10, "max": -1, "sum": -18, "avg": -4.50, "unique_count": 4}
        self.assertEqual(result, expected)
    
    def test_mixed_positive_negative(self):
        """Test with mix of positive and negative numbers."""
        result = list_stats([-3, 0, 3, -3, 6])
        expected = {"min": -3, "max": 6, "sum": 3, "avg": 0.60, "unique_count": 4}
        self.assertEqual(result, expected)
    
    def test_large_numbers(self):
        """Test with large numbers."""
        result = list_stats([1000000, 2000000, 1000000])
        expected = {"min": 1000000, "max": 2000000, "sum": 4000000, "avg": 1333333.33, "unique_count": 2}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()