# Two Pointers Approach: 50 LeetCode Problems by Category

Here is a list of 50 LeetCode problems, categorized by the specific two-pointer technique used to solve them. This approach will help you build your intuition and recognize the patterns associated with each type.

## 1. Opposite Ends (Converging Pointers)

This is the most common two-pointer pattern. Pointers start at opposite ends of a sorted array or a similar data structure and move towards each other, typically to find a pair of elements that satisfy a condition.

* **Easy:**
    1.  [167] Two Sum II - Input array is sorted
    2.  [344] Reverse String
    3.  [125] Valid Palindrome
    4.  [905] Sort Array By Parity
    5.  [88] Merge Sorted Array
    6.  [977] Squares of a Sorted Array
    7.  [26] Remove Duplicates from Sorted Array
    8.  [283] Move Zeroes
    9.  [1099] Two Sum Less Than K 📌
    10. [11] Container With Most Water
    11. [15] 3Sum
    12. [16] 3Sum Closest
    13. [42] Trapping Rain Water
    14. [680] Valid Palindrome II
    15. [189] Rotate Array

* **Medium:**
    16. [26] Remove Duplicates from Sorted Array II
    17. [82] Remove Duplicates from Sorted List II
    18. [392] Is Subsequence
    19. [881] Boats to Save People
    20. [986] Interval List Intersections

## 2. Same Direction (Fast-Slow Pointers)

This technique is often used in linked lists and arrays to detect cycles, find the middle of the list, or solve problems where one pointer needs to "look ahead" of the other.

* **Easy:**
    21. [141] Linked List Cycle
    22. [876] Middle of the Linked List
    23. [234] Palindrome Linked List
    24. [202] Happy Number
    25. [206] Reverse Linked List
    26. [19] Remove Nth Node From End of List
    27. [83] Remove Duplicates from Sorted List
    28. [160] Intersection of Two Linked Lists
    29. [21] Merge Two Sorted Lists

* **Medium:**
    30. [142] Linked List Cycle II
    31. [287] Find the Duplicate Number
    32. [1721] Swapping Nodes in a Linked List
    33. [143] Reorder List

## 3. Same Direction (Sliding Window)

This pattern uses two pointers (typically `left` and `right`) to define a "window" over an array or string. The pointers move in the same direction, expanding and contracting the window to find a subarray or substring that satisfies a certain condition.

* **Easy:**
    34. [209] Minimum Size Subarray Sum
    35. [1004] Max Consecutive Ones III

* **Medium:**
    36. [3] Longest Substring Without Repeating Characters
    37. [424] Longest Repeating Character Replacement
    38. [567] Permutation in String
    39. [713] Subarray Product Less Than K
    40. [795] Number of Subarrays with Bounded Maximum
    41. [76] Minimum Window Substring
    42. [340] Longest Substring with At Most K Distinct Characters
    43. [438] Find All Anagrams in a String
    44. [1456] Maximum Number of Vowels in a Substring of Given Length

## 4. Read-Write Pointers (In-place operations)

This specialized pattern uses two pointers that move at different rates to modify an array in-place, often to remove or rearrange elements without using extra space. One pointer "reads" from the original position, while the other "writes" to a new, compressed position.

* **Easy:**
    45. [26] Remove Duplicates from Sorted Array
    46. [27] Remove Element
    47. [283] Move Zeroes
    48. [905] Sort Array By Parity

* **Medium:**
    49. [75] Sort Colors
    50. [80] Remove Duplicates from Sorted Array II

