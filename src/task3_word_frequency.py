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
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    
    # Count word frequencies manually
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Convert to list of tuples
    word_list = []
    for word, count in word_counts.items():
        word_list.append((word, count))
    
    # Sort by count (descending) and then by word (ascending) for ties
    # Using bubble sort to avoid built-in sort
    for i in range(len(word_list)):
        for j in range(0, len(word_list) - i - 1):
            # Sort by count descending, then by word ascending
            if (word_list[j][1] < word_list[j + 1][1] or 
                (word_list[j][1] == word_list[j + 1][1] and word_list[j][0] > word_list[j + 1][0])):
                word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]
    
    # Return top n words
    return word_list[:n]


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