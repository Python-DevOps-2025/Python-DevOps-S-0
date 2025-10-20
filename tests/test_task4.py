"""
Test suite for Task 4: Simple email validator
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(__file__)), 'src'))

from task4_email_validator import validate_emails


class TestValidateEmails(unittest.TestCase):
    
    def test_example_case(self):
        """Test the provided example."""
        emails = ["user@example.com", "bad@@x", "no-at-sign.com"]
        result = validate_emails(emails)
        expected = {"valid": ["user@example.com"], "invalid": ["bad@@x", "no-at-sign.com"]}
        self.assertEqual(result, expected)
    
    def test_non_list_input_raises_error(self):
        """Test that non-list input raises TypeError."""
        with self.assertRaises(TypeError):
            validate_emails("not a list")
        
        with self.assertRaises(TypeError):
            validate_emails(123)
    
    def test_empty_list(self):
        """Test with empty list."""
        result = validate_emails([])
        expected = {"valid": [], "invalid": []}
        self.assertEqual(result, expected)
    
    def test_valid_emails(self):
        """Test various valid email formats."""
        valid_emails = [
            "user@domain.com",
            "test.email@example.org",
            "user123@test-domain.net",
            "a@b.co",
            "long.email.address@very-long-domain-name.com"
        ]
        result = validate_emails(valid_emails)
        self.assertEqual(result["valid"], valid_emails)
        self.assertEqual(result["invalid"], [])
    
    def test_invalid_emails_no_at(self):
        """Test emails without @ symbol."""
        invalid_emails = ["nodomain.com", "just-a-string", ""]
        result = validate_emails(invalid_emails)
        self.assertEqual(result["valid"], [])
        self.assertEqual(result["invalid"], invalid_emails)
    
    def test_invalid_emails_multiple_at(self):
        """Test emails with multiple @ symbols."""
        invalid_emails = ["user@@domain.com", "test@domain@com", "a@b@c.com"]
        result = validate_emails(invalid_emails)
        self.assertEqual(result["valid"], [])
        self.assertEqual(result["invalid"], invalid_emails)
    
    def test_invalid_emails_no_dot_in_domain(self):
        """Test emails without dot in domain."""
        invalid_emails = ["user@domain", "test@localhost"]
        result = validate_emails(invalid_emails)
        self.assertEqual(result["valid"], [])
        self.assertEqual(result["invalid"], invalid_emails)
    
    def test_invalid_emails_with_spaces(self):
        """Test emails with spaces."""
        invalid_emails = ["user @domain.com", "user@ domain.com", "user@domain .com", " user@domain.com"]
        result = validate_emails(invalid_emails)
        self.assertEqual(result["valid"], [])
        self.assertEqual(result["invalid"], invalid_emails)
    
    def test_invalid_emails_empty_parts(self):
        """Test emails with empty local or domain parts."""
        invalid_emails = ["@domain.com", "user@", "@", "user@.com"]
        result = validate_emails(invalid_emails)
        self.assertEqual(result["valid"], [])
        self.assertEqual(result["invalid"], invalid_emails)
    
    def test_mixed_valid_invalid(self):
        """Test mix of valid and invalid emails."""
        emails = [
            "valid@example.com",
            "invalid@@domain.com",
            "also.valid@test.org",
            "no-at-sign.com",
            "spaces @domain.com"
        ]
        result = validate_emails(emails)
        expected_valid = ["valid@example.com", "also.valid@test.org"]
        expected_invalid = ["invalid@@domain.com", "no-at-sign.com", "spaces @domain.com"]
        self.assertEqual(result["valid"], expected_valid)
        self.assertEqual(result["invalid"], expected_invalid)


if __name__ == "__main__":
    unittest.main()