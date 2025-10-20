"""
Task 4: Simple email validator (regex + branching)

Write validate_emails(emails: list[str]) -> dict that separates the input into 
{"valid": [...], "invalid": [...]} using a simple regex for email format.
"""

import re


def validate_emails(emails: list[str]) -> dict:
    """
    Validate a list of email addresses using regex.
    
    Args:
        emails: List of email strings to validate
        
    Returns:
        Dictionary with "valid" and "invalid" lists
        
    Raises:
        TypeError: If input is not a list
    """
    
    
    # Simple email pattern: local@domain with at least one dot in domain
    
   
    
    return None


if __name__ == "__main__":
    # Test with the example
    test_emails = ["user@example.com", "bad@@x", "no-at-sign.com"]
    result = validate_emails(test_emails)
    print(f"Input: {test_emails}")
    print(f"Output: {result}")
    
    # Test with non-list input (should raise TypeError)
    try:
        validate_emails("not a list")
    except TypeError as e:
        print(f"TypeError test - Exception raised: {e}")
    
    # Additional tests
    test_emails2 = [
        "valid@domain.com",
        "also.valid@sub.domain.org",
        "invalid@",
        "@invalid.com",
        "has spaces@domain.com",
        "nodomain@",
        "multiple@@at.com"
    ]
    result2 = validate_emails(test_emails2)
    print(f"Additional test input: {test_emails2}")
    print(f"Additional test output: {result2}")
