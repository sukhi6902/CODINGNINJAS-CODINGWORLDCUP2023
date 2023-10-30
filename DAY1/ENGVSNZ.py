from typing import List

def minDifference(a: List[int]) -> int:
    # Sort the jersey numbers in ascending order
    a.sort()
    
    min_diff = float('inf')  # Initialize the minimum difference to positive infinity
    
    # Iterate through the sorted jersey numbers and find the minimum difference
    for i in range(1, len(a)):
        diff = a[i] - a[i - 1]
        if diff < min_diff:
            min_diff = diff
    
    return min_diff
