"""
Task 2: Filter and transform strings

Write filter_transform(words: list[str], min_len: int) -> list[str] that returns a new list 
with words longer than min_len, converted to lowercase and sorted alphabetically.
"""


def filter_transform(words: list[str], min_len: int) -> list[str]:
    """
    Filter words by minimum length, convert to lowercase, and sort alphabetically.
    
    Args:
        words: A list of strings
        min_len: Minimum length threshold
        
    Returns:
        A list of filtered, lowercased, and sorted words
    """
    
    
    # Filter words longer than min_len and convert to lowercase
    
    
    # Sort alphabetically using a simple sorting algorithm (bubble sort)
    # Note: We're not using built-in sort() as requested to use explicit loops
    
    
    return None


if __name__ == "__main__":
    # Test with the example
    test_words = ["Hello", "to", "WORLD", "py"]
    min_length = 2
    result = filter_transform(test_words, min_length)
    print(f"Input: {test_words}, min_len: {min_length}")
    print(f"Output: {result}")
    
    # Additional test
    test_words2 = ["Python", "is", "Great", "a"]
    result2 = filter_transform(test_words2, 1)
    print(f"Input: {test_words2}, min_len: 1")
    print(f"Output: {result2}")
