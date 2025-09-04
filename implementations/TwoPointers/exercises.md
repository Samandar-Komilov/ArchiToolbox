# Two Pointers Practice Problems

## General Template

```python
def two_pointers_template(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Calculate current sum or condition
        current = arr[left] + arr[right]  # or other operation
        
        if current == target:
            # Found solution
            return [left, right] or True
        elif current < target:
            left += 1  # Need larger value
        else:
            right -= 1  # Need smaller value
    
    return False or [-1, -1]  # No solution found
```

## Practice Problems

### Easy Problems (Array Manipulation)

1. **Pair with Target Sum**: Given a sorted array, find if there exists a pair with sum = target
2. **Remove Duplicates**: Remove duplicates from sorted array in-place, return new length
3. **Square Sorted Array**: Given sorted array (may contain negatives), return sorted squares
4. **Triplet with Target Sum**: Find if triplet exists with sum = target in sorted array
5. **Dutch National Flag**: Sort array of 0s, 1s, and 2s in one pass

### String Problems

6. **Valid Palindrome**: Check if string is palindrome (ignore non-alphanumeric)
7. **Reverse String**: Reverse string in-place using two pointers
8. **Reverse Vowels**: Reverse only vowels in a string
9. **Valid Palindrome II**: Check if string can be palindrome by removing at most one char
10. **Backspace String Compare**: Compare two strings with '#' as backspace

### Window Problems

11. **Minimum Window Sort**: Find shortest subarray that needs sorting to make entire array sorted
12. **Container with Most Water**: Find two lines that form container with most water
13. **Trapping Rain Water**: Calculate how much water can be trapped between bars
14. **Longest Substring Without Repeating**: Find longest substring with all unique chars
15. **Minimum Size Subarray Sum**: Find minimal length subarray with sum ≥ target

### Advanced Problems

16. **3Sum**: Find all unique triplets that sum to zero
17. **3Sum Closest**: Find triplet with sum closest to target
18. **4Sum**: Find all unique quadruplets that sum to target
19. **Subarray Product Less Than K**: Count subarrays where product < k
20. **Sort Colors**: Given array of colors (0,1,2), sort in-place