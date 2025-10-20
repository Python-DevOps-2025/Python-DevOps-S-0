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
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    
    for char in s:
        if char in opening_brackets:
            # Push opening bracket onto stack
            stack.append(char)
        elif char in closing_brackets:
            # Check if we have a matching opening bracket
            if not stack:
                # No opening bracket to match
                return False
            
            # Pop the last opening bracket
            last_opening = stack.pop()
            
            # Check if it matches the current closing bracket
            if last_opening != bracket_pairs[char]:
                return False
        # Ignore all other characters
    
    # If stack is empty, all brackets were matched
    return len(stack) == 0


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