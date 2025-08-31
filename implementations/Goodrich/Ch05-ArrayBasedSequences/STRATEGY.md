# 🔁 Core Techniques in Array-Based Sequences

## Sliding Window

Use: Fixed-size or variable-size window on array/string.
Applications: Maximum sum subarray, longest substring without repeating characters.
Leetcode:
1. Maximum sum subarray of size K (fixed window)
2. Longest substring without repeating characters
3. Longest substring with at most K distinct characters
4. Minimum window substring (hard but golden)
5. Find all anagrams in a string
6. Longest repeating character replacement
7. Fruits into baskets (variation of at most 2 distinct)


## Two Pointers

Use: Sorted array problems, subarray searching, partitioning logic.
Variants: Fast-slow pointer, shrinking/growing window.
Applications: Merge intervals, removing duplicates, palindrome checking.
Leetcode:
1. Two sum (sorted array version with pointers)
2. 3Sum problem
3. 4Sum problem
4. Trapping rainwater
5. Container with most water
6. Remove duplicates from sorted array
7. Move zeroes
8. Sort colors (Dutch flag problem)


## Prefix Sum

Use: Range sum queries, subarray calculations.
Variants: 1D Prefix Sum, 2D Prefix Sum, Difference Array (for range updates).
Applications: Subarray sum equals K, imos method in optimization.
Leetcode:
1. Subarray sum equals K
2. Continuous subarray sum (check if multiple of K)
3. Longest subarray with sum 0
4. Maximum subarray (Kadane’s algorithm)
5. Product of array except self
6. Maximum product subarray


## Binary Search on Arrays

Use: Find element, boundaries (first/last occurrence), custom conditions.
Variants: Left-bound/right-bound binary search, binary search on answer.
Applications: Peak element, capacity to ship packages within D days.
Leetcode:
1. Search in rotated sorted array
2. Find minimum in rotated sorted array
3. Find first and last position in sorted array
4. Median of two sorted arrays
5. Minimum in rotated sorted array II (with duplicates)


## In-place Shifting and Swapping

Use: Rotating array, reversing, cyclic replacements.
Applications: Move zeroes, rotate array, in-place merge.


## Difference Arrays (Range Updates)

Use: Efficient range updates using difference and prefix logic.
Applications: Range addition, interval overlapping.


## Kadane’s Algorithm

Use: Max subarray sum in O(n).
Applications: Real-time log monitoring, temperature drop detection.


## Dutch National Flag Partitioning

Use: Multi-way partitioning, 3-way quicksort, color sorting.
Applications: Sorting 0s, 1s, and 2s; bucket separation.


## Reservoir Sampling

Use: Pick random element from a stream.
Application: System monitoring tools (e.g., Redis sampling).


## Prefix XOR / Bitmask Patterns

Use: Subarrays with certain XOR conditions.
Applications: Security, encoding, segment checksum tools.