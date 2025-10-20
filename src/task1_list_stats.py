"""
Task 1: List statistics

Write a function list_stats(numbers: list[int]) -> dict that receives a list of integers 
and returns a dictionary with keys: min, max, sum, avg (rounded to 2 decimals), and unique_count.
"""


def list_stats(numbers: list[int]) -> dict:
    """
    Calculate statistics for a list of integers.
    
    Args:
        numbers: A list of integers
        
    Returns:
        A dictionary with keys: min, max, sum, avg, unique_count
        
    Raises:
        ValueError: If the list is empty
    """
    
    
    # Iterate through all numbers
    
    
    # Calculate average
    
    
    return None


if __name__ == "__main__":
    # Test with the example
    test_input = [3, 5, 3, 10, -1]
    result = list_stats(test_input)
    print(f"Input: {test_input}")
    print(f"Output: {result}")
    
    # Test with empty list (should raise ValueError)
    try:
        list_stats([])
    except ValueError as e:
        print(f"Empty list test - ValueError raised: {e}")
