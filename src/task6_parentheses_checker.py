"""
Task 6: Parentheses balance checker (collections + loops)

Write is_balanced(s: str) -> bool that checks whether parentheses (), brackets [], 
and braces {} in the string s are balanced and properly nested.
"""


def is_balanced(s: str) -> bool:
    """
    Check if parentheses, brackets, and braces are balanced and properly nested.
    
    Args:
        s: Input string to check
        
    Returns:
        True if balanced, False otherwise
    """
    # Stack to track opening brackets
    stack = []
    
    # Mapping of closing to opening brackets
    
    

    return None


if __name__ == "__main__":
    # Test with the examples
    test_cases = [
        ("{[()]}()", True),
        ("(unbalanced]", False),
        ("", True),  # Empty string is balanced
        ("((()))", True),
        ("([)]", False),  # Improperly nested
        ("Hello (world) [test]!", True),  # With other characters
        ("((())", False),  # Unmatched opening
        ("())", False),  # Unmatched closing
        ("{[()]}", True),
        ("({[]})", True),
        ("({[}])", False),  # Wrong order
    ]
    
    for test_input, expected in test_cases:
        result = is_balanced(test_input)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{test_input}' -> {result} (expected: {expected})")
