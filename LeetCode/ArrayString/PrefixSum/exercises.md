## 2. Prefix Sum (Arrays)

Prefix sum is a powerful technique for solving problems that involve finding the sum of subarrays or ranges in an array. By pre-calculating the cumulative sum, we can answer any range sum query in `O(1)` time.

* **Easy:**
    1.  [1480] Running Sum of 1D Array
    2.  [303] Range Sum Query - Immutable
    3.  [1732] Find the Highest Altitude
    4.  [1588] Sum of All Odd Length Subarrays
    5.  [2486] Append Characters to String to Make Subsequence (Can be solved with two-pointers, but prefix/suffix sum logic is related)
    6.  [1991] Find the Middle Index in Array

* **Medium:**
    7.  [560] Subarray Sum Equals K (also a hashtable problem, but the prefix sum is the key)
    8.  [304] Range Sum Query 2D - Immutable
    9.  [523] Continuous Subarray Sum
    10. [974] Subarray Sums Divisible by K
    11. [209] Minimum Size Subarray Sum (Sliding Window/Prefix Sum)
    12. [2270] Count Number of Ways to Split a String
    13. [1413] Minimum Value to Get Positive Step by Step Sum
    14. [1442] Count Triplets That Can Form Two Arrays of Equal XOR (Prefix XOR is the equivalent)
    15. [238] Product of Array Except Self

### **4. Dynamic Programming (Arrays/Strings)**

DP problems often involve an optimal substructure and overlapping subproblems. The solutions build up from smaller, solved subproblems to the final answer. Arrays are a natural fit for DP because they provide a simple way to store computed states.

* **Easy:**
    1.  [53] Maximum Subarray (Kadane's Algorithm, a classic DP approach)
    2.  [70] Climbing Stairs
    3.  [121] Best Time to Buy and Sell Stock
    4.  [118] Pascal's Triangle
    5.  [303] Range Sum Query - Immutable (Can also be solved with DP, where `dp[i] = nums[i] + dp[i-1]`)
    6.  [645] Set Mismatch

* **Medium:**
    7.  [64] Minimum Path Sum
    8.  [139] Word Break
    9.  [300] Longest Increasing Subsequence
    10. [5] Longest Palindromic Substring
    11. [152] Maximum Product Subarray
    12. [91] Decode Ways
    13. [198] House Robber
    14. [213] House Robber II
    15. [718] Maximum Length of Repeated Subarray