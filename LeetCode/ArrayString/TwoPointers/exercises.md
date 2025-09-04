# Two Pointers Exercises

The Two Pointers technique is incredibly versatile. Here are 25 problems categorized by the specific pattern they use, starting from easiest to most complex.

### Category 1: Opposite Ends (The Classic Pattern)
*Ideal for sorted arrays. One pointer at the start, one at the end. They move towards each other based on a condition.*

1.  **Two Sum II (Input Array is Sorted):** Find two numbers that add up to a target.
2.  **Reverse String:** Reverse the array of characters in-place.
3.  **Valid Palindrome:** Check if a string reads the same forwards and backwards, ignoring non-alphanumeric chars.
4.  **Squares of a Sorted Array:** Given sorted ints (negative & positive), return squares sorted in non-decreasing order.
5.  **3Sum:** Find all unique triplets that add up to zero. (Uses a fixed pointer and then two pointers for the remainder).
6.  **3Sum Closest:** Find three integers whose sum is closest to a target.
7.  **4Sum:** Find all unique quadruplets that add up to a target.
8.  **Container With Most Water:** Find two lines that together with the x-axis form a container that holds the most water.

### Category 2: Same Direction (Fast & Slow Pointers)
*Often used to detect cycles or find a specific node in a linked list.*

9.  **Linked List Cycle:** Determine if a linked list has a cycle.
10. **Linked List Cycle II:** Find the node where the cycle begins.
11. **Middle of the Linked List:** Return the middle node.
12. **Remove Duplicates from Sorted Array:** Do it in-place with O(1) extra space.
13. **Remove Duplicates from Sorted List:** Delete all duplicates such that each element appears only once.
14. **Remove Element:** Remove all instances of a value in-place and return the new length.

### Category 3: Same Direction (Sliding Window)
*You've been practicing this! It's a subset of Two Pointers.*

15. **Minimum Size Subarray Sum:** (Reviewed) Find the minimal length of a subarray sum ≥ target.
16. **Longest Substring Without Repeating Characters:** (Reviewed) Find the length of the longest substring w/o repeating chars.
17. **Permutation in String:** (Reviewed) Check if `s2` contains a permutation of `s1`.
18. **Find All Anagrams in a String:** (Reviewed) Find all start indices of `p`'s anagrams in `s`.
19. **Longest Repeating Character Replacement:** (Reviewed) Find the longest substring after performing at most `k` changes.

### Category 4: Read/Write Pointers (In-place Operations)
*One pointer reads the data, another writes the output in the same array.*

20. **Remove Duplicates from Sorted Array II:** Allow duplicates to appear at most *twice* and return the new length.
21. **Move Zeroes:** Move all 0's to the end while maintaining the relative order of non-zero elements.
22. **Sort Colors (Dutch National Flag):** Sort an array of 0s, 1s, and 2s in-place.

### Category 5: Multi-Sequence Pointers
*Pointers start at the beginning of different arrays or strings.*

23. **Merge Sorted Array:** Merge `nums2` into `nums1` in-place, which has extra space.
24. **Interval List Intersections:** Given two lists of intervals, find their intersection.
25. **Backspace String Compare:** Given two strings `s` and `t`, return `true` if they are equal when both are typed into empty text editors. `'#'` means a backspace character.

This list provides a comprehensive tour of the Two Pointers technique. Start with Category 1 to build the fundamental intuition of pointers moving from opposite ends, then move through the others. Happy coding