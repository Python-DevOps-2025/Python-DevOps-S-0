"""
Test suite for Task 6: Parentheses balance checker
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task6_parentheses_checker import is_balanced


class TestIsBalanced(unittest.TestCase):
    
    def test_example_cases(self):
        """Test the provided examples."""
        self.assertTrue(is_balanced("{[()]}()"))
        self.assertFalse(is_balanced("(unbalanced]"))
    
    def test_empty_string(self):
        """Test empty string is balanced."""
        self.assertTrue(is_balanced(""))
    
    def test_simple_parentheses(self):
        """Test simple parentheses cases."""
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("((()))"))
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced(")"))
        self.assertFalse(is_balanced("())"))
        self.assertFalse(is_balanced("(()"))
    
    def test_simple_brackets(self):
        """Test simple square brackets cases."""
        self.assertTrue(is_balanced("[]"))
        self.assertTrue(is_balanced("[[[]]]"))
        self.assertFalse(is_balanced("["))
        self.assertFalse(is_balanced("]"))
        self.assertFalse(is_balanced("[]]"))
        self.assertFalse(is_balanced("[["))
    
    def test_simple_braces(self):
        """Test simple curly braces cases."""
        self.assertTrue(is_balanced("{}"))
        self.assertTrue(is_balanced("{{{}}}"))
        self.assertFalse(is_balanced("{"))
        self.assertFalse(is_balanced("}"))
        self.assertFalse(is_balanced("{}}}"))
        self.assertFalse(is_balanced("{{{"))
    
    def test_mixed_brackets_valid(self):
        """Test valid mixed bracket combinations."""
        self.assertTrue(is_balanced("()[]{}"))
        self.assertTrue(is_balanced("([{}])"))
        self.assertTrue(is_balanced("{[()]}"))
        self.assertTrue(is_balanced("([]){}"))
        self.assertTrue(is_balanced("((([[[{}]]])))"))  # Properly balanced: 3 of each type
    
    def test_mixed_brackets_invalid(self):
        """Test invalid mixed bracket combinations."""
        self.assertFalse(is_balanced("([)]"))  # Crossed
        self.assertFalse(is_balanced("({[}])"))  # Wrong order
        self.assertFalse(is_balanced("[(])"))  # Crossed
        self.assertFalse(is_balanced("{[}]"))  # Wrong closing
        self.assertFalse(is_balanced("((([[[{{{}}}}]]])))"))  # Missing closing
    
    def test_with_other_characters(self):
        """Test brackets mixed with other characters."""
        self.assertTrue(is_balanced("Hello (world) [test]!"))
        self.assertTrue(is_balanced("if (condition) { do_something(); }"))
        self.assertTrue(is_balanced("array[index] = function(param)"))
        self.assertFalse(is_balanced("if (condition { missing_paren"))
        self.assertFalse(is_balanced("array[index) = wrong_bracket"))
    
    def test_only_text_no_brackets(self):
        """Test strings with no brackets."""
        self.assertTrue(is_balanced("hello world"))
        self.assertTrue(is_balanced("12345"))
        self.assertTrue(is_balanced("!@#$%^&*"))
    
    def test_nested_structures(self):
        """Test deeply nested structures."""
        self.assertTrue(is_balanced("((((((()))))))"))
        self.assertTrue(is_balanced("[[[[[[[]]]]]]]"))
        self.assertTrue(is_balanced("{{{{{{{}}}}}}}"))
        self.assertTrue(is_balanced("{[({[({[]})]})]}" ))
    
    def test_edge_cases(self):
        """Test edge cases."""
        self.assertFalse(is_balanced(")("))  # Wrong order
        self.assertFalse(is_balanced("}{"))  # Wrong order
        self.assertFalse(is_balanced("]["))  # Wrong order
        self.assertTrue(is_balanced("abc"))  # No brackets
        self.assertFalse(is_balanced("(abc]"))  # Mismatched types


if __name__ == "__main__":
    unittest.main()