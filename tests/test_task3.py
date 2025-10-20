"""
Test suite for Task 3: Word frequency (use regex)
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task3_word_frequency import top_words


class TestTopWords(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example."""
        text = "Hello, hello! This is a test. Test; test?"
        result = top_words(text, 2)
        expected = [("test", 3), ("hello", 2)]
        self.assertEqual(result, expected)
    
    def test_default_n_parameter(self):
        """Test default n=3 parameter."""
        text = "one two three four one two one"
        result = top_words(text)  # Should default to n=3
        expected = [("one", 3), ("two", 2), ("four", 1)]  # "four" comes before "three" alphabetically
        self.assertEqual(result, expected)
    
    def test_case_insensitive(self):
        """Test case insensitivity."""
        text = "Hello HELLO hello"
        result = top_words(text, 1)
        expected = [("hello", 3)]
        self.assertEqual(result, expected)
    
    def test_tie_breaking_alphabetical(self):
        """Test tie breaking by alphabetical order."""
        text = "apple banana apple banana cherry"
        result = top_words(text, 3)
        # apple and banana both have count 2, should be ordered alphabetically
        expected = [("apple", 2), ("banana", 2), ("cherry", 1)]
        self.assertEqual(result, expected)
    
    def test_punctuation_handling(self):
        """Test that punctuation is properly handled."""
        text = "word1, word2! word3? word1."
        result = top_words(text, 3)
        expected = [("word1", 2), ("word2", 1), ("word3", 1)]
        self.assertEqual(result, expected)
    
    def test_numbers_in_words(self):
        """Test that numbers in words are included."""
        text = "test123 test123 word456"
        result = top_words(text, 2)
        expected = [("test123", 2), ("word456", 1)]
        self.assertEqual(result, expected)
    
    def test_empty_text(self):
        """Test with empty text."""
        result = top_words("", 3)
        self.assertEqual(result, [])
    
    def test_only_punctuation(self):
        """Test text with only punctuation."""
        result = top_words("!@#$%^&*()", 3)
        self.assertEqual(result, [])
    
    def test_more_n_than_unique_words(self):
        """Test when n is larger than number of unique words."""
        text = "one two"
        result = top_words(text, 5)
        expected = [("one", 1), ("two", 1)]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()