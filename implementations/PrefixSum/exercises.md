# Prefix Sum exercises

## 🔰 Easy (1–5): Basic Prefix Sum Practice

**1. Basic Prefix Sum Construction**
✅ Given an array A, construct its prefix sum array P such that P[i] = A[0] + A[1] + ... + A[i].

**2. Range Sum Query – Static Array**  
✅ Precompute prefix sums and answer Q queries of the form: sum(i, j) = sum of elements from i to j.

✅ **3. Running Total Log**  
Given a list of timestamps and user visit counts, compute cumulative visits over time.

---

## 15 Prefix Sum Exercises

Let's get your brain used to the template. The pattern is always:
1.  **Initialize** a `prefix_sum` array (often with an extra 0 at the front).
2.  **Build** the prefix array with a simple loop.
3.  **Use** the prefix array to answer queries or find answers in constant or linear time.

**1. Basic Prefix Array Construction**
**Task:** Given an array `nums`, build and return a prefix sum array.
**Example:** `nums = [2, 1, 5, 3]` → Output: `[0, 2, 3, 8, 11]` (The sum up to index 0 is 0, up to index 1 is 2, etc.)
**Focus:** Pure implementation of the pre-computation step.
`prefix[0] = 0`
`for i in range(len(nums)): prefix[i+1] = prefix[i] + nums[i]`

**2. Range Sum Query - Immutable**
**Task:** Given an array, design a class to handle multiple queries of the form: "What is the sum of elements between indices `i` and `j`?"
**Example:** `nums = [-2, 0, 3, -5, 2, -1]`, `sumRange(0, 2)` -> `1`, `sumRange(2, 5)` -> `-1`
**Focus:** The classic use case. The answer is `prefix[j+1] - prefix[i]`.

**3. Find the Pivot Index**
**Task:** Find the index where the sum of all elements to the left equals the sum of all elements to the right. Return -1 if no such index.
**Example:** `nums = [1, 7, 3, 6, 5, 6]` → Output: `3` (Left: `1+7+3=11`, Right: `5+6=11`)
**Focus:** The sum to the left of `i` is `prefix[i]`. The sum to the right is `prefix[n] - prefix[i+1]`. Check if they are equal.

**4. Subarray Sum Equals K (The Absolute Classic)**
**Task:** Given an array of integers and an integer `k`, find the total number of contiguous subarrays whose sum equals `k`. *(This is where Prefix Sum shines! Sliding window doesn't work with negative numbers.)*
**Example:** `nums = [1, 1, 1], k = 2` → Output: `2` (`[1,1]` and `[1,1]`)
**Focus:** The core insight: `sum(i, j) = k` is the same as `prefix[j] - prefix[i] = k`. This can be rearranged to `prefix[i] = prefix[j] - k`. Use a dictionary to count how many times each prefix sum has been seen.

**5. Continuous Subarray Sum (Check for Multiple of K)**
**Task:** Check if the array has a contiguous subarray of size >= 2 whose sum is a multiple of `k`.
**Example:** `nums = [23, 2, 4, 6, 7], k = 6` → Output: `True` (because `[2, 4]` sums to 6).
**Focus:** This uses the modulo property of prefix sums. If `prefix[j] % k == prefix[i] % k` and `j - i >= 2`, then the subarray sum `(i, j)` is a multiple of `k`.

**6. Find the Highest Altitude**
**Task:** A biker goes on a road trip. `gain[i]` is the net gain in altitude between points `i` and `i+1`. Return the highest altitude they reach.
**Example:** `gain = [-5, 1, 5, 0, -7]` → Output: `1` (Altitudes: [0, -5, -4, 1, 1, -6])
**Focus:** The altitude at each point is a prefix sum! The highest is just the `max(prefix)`.

**7. Product of Array Except Self (Prefix "Product")**
**Task:** Given an array `nums`, return an array `answer` where `answer[i]` is the product of all elements except `nums[i]`.
**Example:** `nums = [1, 2, 3, 4]` → Output: `[24, 12, 8, 6]`
**Focus:** This uses the same idea but with multiplication. Build a `prefix_product` and a `suffix_product` array.

**8. Corporate Flight Bookings**
**Task:** There are `n` flights booked with entries `[first, last, seats]`. Return an array `answer` of length `n`, where `answer[i]` is the total seats booked for flight `i`.
**Example:** `bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5` → Output: `[10, 55, 45, 25, 25]`
**Focus:** This introduces the powerful **Difference Array** technique, built using prefix sums.
1.  Initialize an array `diff` of zeros of length `n`.
2.  For each booking `[i, j, s]`: `diff[i-1] += s`, and if `j < n`: `diff[j] -= s`.
3.  The final answer is the *prefix sum* of the `diff` array.

**9. Plates Between Candles**
**Task:** Given a string `s` representing a row of items (`'*'` = plate, `'|'` = candle) and a list of queries `[left, right]`, return the number of plates *between candles* for each query.
**Example:** `s = "**|**|***|"`, `queries = [[2,5]]` → Output: `2` (substring is "|**|", so 2 plates between two candles).
**Focus:** This requires building multiple prefix arrays: one for the cumulative count of plates, and others to find the *next* candle to the right and the *previous* candle to the left of an index.

**10. Number of Ways to Split Array**
**Task:** Find the number of ways to split the array into two non-empty parts such that the sum of the left part is >= the sum of the right part.
**Example:** `nums = [10, 4, -8, 7]` → Output: `2`
**Focus:** The total sum is `prefix[n]`. For a split at index `i`, the left sum is `prefix[i+1]`. Check if `prefix[i+1] >= total_sum - prefix[i+1]`.

**11. Maximum Sum of Two Non-Overlapping Subarrays**
**Task:** Given an array and two integers `firstLen` and `secondLen`, find the maximum sum of two non-overlapping subarrays of lengths `firstLen` and `secondLen`.
**Example:** `nums = [0,6,5,2,2,5,1,9,4], firstLen = 1, secondLen = 2` → Output: `20` (One subarray is `[9]` (sum=9), the other is `[5,2]` (sum=7) -> 16? Wait, let's calculate: `[9]` and `[5,2]` are not contiguous. The answer is choosing `[9]` (sum=9) and `[6,5]` (sum=11) for a total of 20.)
**Focus:** Uses prefix sum to get window sums quickly. Then, for each possible position of the second array, you know the best possible first array that doesn't overlap with it.

**12. Count Number of Nice Subarrays**
**Task:** Given an array of integers and an integer `k`, return the number of "nice" subarrays. A subarray is "nice" if it contains exactly `k` odd numbers.
**Example:** `nums = [1,1,2,1,1], k = 3` → Output: `2` (`[1,1,2,1]` and `[1,2,1,1]`)
**Focus:** Similar to "Subarray Sum Equals K". Convert odds to `1` and evens to `0`. Now the problem becomes "find number of subarrays with sum exactly `k`".

**13. Minimum Value to Get Positive Step by Step Sum**
**Task:** Choose a start value. Then calculate the step-by-step sum. Return the minimum positive start value such that the step-by-step sum is never less than 1.
**Example:** `nums = [-3,2,-3,4,2]` → Output: `5` (If you start with 5, the sums are: 5+(-3)=2, 2+2=4, 4+(-3)=1, 1+4=5, 5+2=7. All >=1.)
**Focus:** The step-by-step sums are the prefix sums! Find the minimum prefix sum. The required start value is `1 - min_prefix_sum` (if it's negative), but never less than 1.

**14. Find the Longest Awesome Substring**
**Task:** A string is "awesome" if it can be made a palindrome by rearranging it. Find the length of the longest awesome substring.
**Example:** `s = "3242415"` → Output: `5` ("24241" can be rearranged to "24142", a palindrome).
**Focus:** Uses a *bitmask prefix*. Each bit in an integer represents the parity (even/odd count) of a digit. A substring is awesome if its bitmask has at most one bit set (one digit with an odd count).

**15. Count Triplets That Can Form Two Arrays of Equal XOR**
**Task:** Given an array, count the number of triplets `(i, j, k)` such that the XOR of elements from `i` to `j-1` equals the XOR from `j` to `k`.
**Example:** `arr = [2,3,1,6,7]` → Output: `4`
**Focus:** This uses a **Prefix XOR** array. The condition `XOR(i, j-1) == XOR(j, k)` is equivalent to `XOR(i, k) = 0`. Find all pairs `(i, k)` where the prefix XOR is the same, and for each such pair, any `j` in `(i+1, k)` will work.

This list covers the fundamental uses of prefix sums, from simple range queries to more advanced applications with hashing, bitmasking, and the difference array technique.