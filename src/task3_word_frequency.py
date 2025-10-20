"""
Task 3: Word frequency (use regex)

Write top_words(text: str, n: int = 3) -> list[tuple[str,int]] that finds words in text 
(case-insensitive), counts their occurrences, and returns the top n words with counts 
as (word, count) tuples.
"""

import re


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    """
    Find the top n most frequent words in text using regex.
    
    Args:
        text: Input text to analyze
        n: Number of top words to return (default: 3)
        
    Returns:
        List of (word, count) tuples for the top n words
    """
    # Use regex to extract words (letters and digits)
    
    
    # Count word frequencies manually
    
    
    # Convert to list of tuples
    
    
    # Sort by count (descending) and then by word (ascending) for ties
    # Using bubble sort to avoid built-in sort
    
    
    # Return top n words
    return None


if __name__ == "__main__":
    # Test with the example
    test_text = "Hello, hello! This is a test. Test; test?"
    result = top_words(test_text, 2)
    print(f"Input: '{test_text}', n=2")
    print(f"Output: {result}")
    
    # Additional test
    test_text2 = "Python is great. Python is powerful. Python is fun!"
    result2 = top_words(test_text2, 3)
    print(f"Input: '{test_text2}', n=3")
    print(f"Output: {result2}")
