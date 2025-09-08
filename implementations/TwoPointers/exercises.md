# Two Pointers Practice Problems

## 1. Opposite Ends (Converging Pointers)

These start from both ends of the array/string and move towards each other.

1. **Check if Array is Palindrome**
   * Input: `[1, 2, 3, 2, 1]` → Output: `True`
   * Input: `[1, 2, 2, 3]` → Output: `False`
   * Edge: empty array → treat as `True`.

2. **Check if String is Palindrome (ignore case + spaces)**
   * Input: `"A man a plan a canal Panama"` → Output: `True`.

3. **Pair Sum Exists**
   * Input: `[1, 2, 4, 7, 11, 15], target=15` → Output: `True` (because 4+11).
   * Input: `[1, 2, 3], target=6` → Output: `False`.
   * Array sorted.

4. **Find All Pairs with Target Sum**
   * Input: `[1, 2, 2, 3, 4], target=4` → Output: `(1,3), (2,2)`.

5. **Container with Most Water (easy version)**
   * Input: `[1,8,6,2,5,4,8,3,7]` → Output: `49`.
   * Each index is a wall, find max water area between two walls.

---

## 2. Same Direction Pointers

Both pointers move in one direction.

6. **Remove Duplicates from Sorted Array (in-place)**
   * Input: `[1,1,2,2,3]` → Output array: `[1,2,3]` length=3.
   * Edge: empty array.

7. **Merge Two Sorted Arrays (like merge step in merge sort)**
   * Input: `[1,3,5]`, `[2,4,6]` → Output: `[1,2,3,4,5,6]`.

8. **Intersection of Two Sorted Arrays**
   * Input: `[1,2,2,3]`, `[2,2,4]` → Output: `[2,2]`.

9. **Union of Two Sorted Arrays (unique elements)**
   * Input: `[1,2,4]`, `[2,3,5]` → Output: `[1,2,3,4,5]`.

10. **Difference of Two Sorted Arrays**
* Input: `[1,2,3,4]`, `[2,4]` → Output: `[1,3]`.

---

## 3. Sliding Window (classic subdomain)

Two pointers maintain a "window".

11. **Smallest Subarray with Sum ≥ Target**
* Input: `[2,3,1,2,4,3], target=7` → Output: `2` (subarray `[4,3]`).

12. **Longest Subarray with Sum ≤ Target**
* Input: `[1,2,3,4,5], target=11` → Output: `3` (subarray `[3,4,5]`).

13. **Max Sum Subarray of Size K**
* Input: `[1,2,3,4,5,6], k=3` → Output: `15`.

14. **Longest Substring without Repeating Characters**
* Input: `"abcabcbb"` → Output: `3`.

15. **Longest Substring with At Most K Distinct Characters**
* Input: `"eceba", k=2` → Output: `3` (`"ece"`).

---

## 4. Partitioning / Rearrangement

Using two pointers to rearrange.

16. **Move All Zeroes to End**
* Input: `[0,1,0,3,12]` → Output: `[1,3,12,0,0]`.

17. **Segregate Even and Odd Numbers**
* Input: `[1,2,3,4]` → Output: `[2,4,1,3]`.

18. **Sort 0s, 1s, 2s (Dutch National Flag)**
* Input: `[2,0,2,1,1,0]` → Output: `[0,0,1,1,2,2]`.

19. **Reverse Words in String In-Place**
* Input: `"the sky is blue"` → Output: `"blue is sky the"`.

20. **Remove Spaces from String (in-place)**
* Input: `"a b  c "` → Output: `"abc"`.

---

## 5. Searching / Ranges

Two pointers to search or compress ranges.

21. **Find First and Last Position of Target in Sorted Array**
* Input: `[5,7,7,8,8,10], target=8` → Output: `[3,4]`.

22. **Count Pairs with Difference = K**
* Input: `[1,5,3,4,2], k=2` → Output: `3` (`(1,3),(5,3),(4,2)`).

23. **Count Triplets with Sum ≤ Target (sorted array)**
* Input: `[1,2,3,4,5], target=8` → Output: `6`.

24. **Find Subarray with Given Sum (non-negative numbers)**
* Input: `[1,4,20,3,10,5], sum=33` → Output: `[20,3,10]`.

25. **Check if Subsequence Exists**
* Input: `"abc"`, `"ahbgdc"` → Output: `True`.
* Input: `"axc"`, `"ahbgdc"` → Output: `False`.

---

## 6. Advanced but Still Beginner-Friendly

These combine techniques but remain approachable.

26. **Minimum Window Substring (simplified)**
* Input: `s="ADOBECODEBANC", t="ABC"` → Output: `"BANC"`.

27. **Longest Ones after Replacing at Most K Zeroes**
* Input: `[1,1,1,0,0,0,1,1,1,1,0], k=2` → Output: `6`.

28. **Find Duplicate Number (Floyd’s Tortoise & Hare)**
* Input: `[1,3,4,2,2]` → Output: `2`.
* Uses cycle detection style.

29. **Trapping Rain Water (classic two-pointer)**
* Input: `[0,1,0,2,1,0,1,3,2,1,2,1]` → Output: `6`.

30. **Minimum Size Subarray Sum (variant)**
* Input: `[1,2,3,4,5], target=11` → Output: `3` (`[3,4,5]`).

---

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
