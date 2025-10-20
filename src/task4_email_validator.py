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
    if not isinstance(emails, list):
        raise TypeError("Input must be a list")
    
    valid_emails = []
    invalid_emails = []
    
    # Simple email pattern: local@domain with at least one dot in domain
    # No spaces allowed, exactly one @ symbol
    email_pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    
    for email in emails:
        # Check if it's a string first
        if not isinstance(email, str):
            invalid_emails.append(email)
            continue
            
        # Check for basic requirements
        if ' ' in email:  # No spaces
            invalid_emails.append(email)
            continue
            
        at_count = email.count('@')
        if at_count != 1:  # Exactly one @
            invalid_emails.append(email)
            continue
            
        # Use regex for final validation
        if re.match(email_pattern, email):
            # Additional check: domain must contain at least one dot
            domain = email.split('@')[1]
            if '.' in domain:
                valid_emails.append(email)
            else:
                invalid_emails.append(email)
        else:
            invalid_emails.append(email)
    
    return {
        "valid": valid_emails,
        "invalid": invalid_emails
    }


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