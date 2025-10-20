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
    if not numbers:
        raise ValueError("Cannot calculate statistics for an empty list")
    
    # Initialize values with first element
    min_val = numbers[0]
    max_val = numbers[0]
    total_sum = 0
    unique_values = set()
    
    # Iterate through all numbers
    for num in numbers:
        # Update min and max
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
        
        # Add to sum
        total_sum += num
        
        # Add to unique set
        unique_values.add(num)
    
    # Calculate average
    avg = total_sum / len(numbers)
    
    return {
        "min": min_val,
        "max": max_val,
        "sum": total_sum,
        "avg": round(avg, 2),
        "unique_count": len(unique_values)
    }


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