# Prefix Sum exercises

## 🔰 Easy (1–5): Basic Prefix Sum Practice

**1. Basic Prefix Sum Construction**
✅ Given an array A, construct its prefix sum array P such that P[i] = A[0] + A[1] + ... + A[i].

**2. Range Sum Query – Static Array**  
✅ Precompute prefix sums and answer Q queries of the form: sum(i, j) = sum of elements from i to j.

✅ **3. Running Total Log**  
Given a list of timestamps and user visit counts, compute cumulative visits over time.

**4. Is Subarray Sum Divisible by K?**
Given array A and integer K, check if any subarray sum is divisible by K.

**5. Find Equilibrium Index**  
An index i where the sum of elements before i equals the sum after i. Return all such indices.

## ⚙️ Medium (6–14): Applied Patterns and 2D Variants

**6. Update and Query – Using Difference Array** 
Given an array of size n, and m operations of the form add x to all elements in range [l, r], efficiently process them and return the final array.

**7. Daily Pageviews Analytics**  
Given daily view counts and queries like "total views between day i and j", answer using prefix sums.

**8. 2D Prefix Sum: Region Sum in a Matrix**  
Given a matrix of integers, preprocess it with 2D prefix sums and answer queries like:
sum(x1, y1, x2, y2) — total sum of submatrix from top-left (x1, y1) to bottom-right (x2, y2).

**9. Max Subarray Sum (Kadane + Prefix Sum)**  
Implement both the brute-force and optimized (Kadane’s) approaches and compare performance.

**10. Subarray with Given Sum (Prefix Map)**  
Given array A and target S, find the number of subarrays where sum = S. (Use prefix sum + hashmap)

**11. Binary Array – Count Subarrays with Equal 0s and 1s**  
Transform 0 to -1 and use prefix sum and hashmap to count subarrays with sum = 0.

**12. Range XOR Queries using Prefix XOR**  
Given an array, precompute prefix XOR and answer XOR(i, j) in O(1).

**13. 2D Difference Array – Range Update in Matrix**  
Perform multiple range additions on submatrices and return the final matrix.

**14. Inversion Count using Prefix Sum Binary Indexed Tree**
Count number of inversions in an array using Fenwick Tree and prefix sums.


## 🔥 Hard (15–20): Systems Thinking, Real-World Inspired

⏳ **15. Log Aggregation System Simulation**
You're building a log processing system. Given logs like [timestamp, request_count], support:
- add_log(t, c)
- query_logs(t1, t2) → total count between t1 and t2.
- Use prefix sums or time-binned map structure.

**16. Sliding Window Maximum Sum of Fixed Size k**
Given an array and k, find the maximum sum of any contiguous subarray of size k. (Use prefix sums to compute window sums in O(1))

**17. Prefix Min/Max with Sparse Table or Segment Tree**
Build an enhanced prefix structure that not only stores sums but also min/max in range.

**18. Detect Anomalies in Web Traffic**
Given traffic per minute, identify windows where the sum crosses a threshold (burst detection). Optimize for multiple overlapping queries.

**19. Difference Array with Wrap-around Updates (Circular Buffer)**
Given a circular buffer, implement range addition efficiently with a difference array. Handle wrap-around carefully.

**20. Multi-dimensional Metrics Tracker (Real Use-Case)**  
You're tracking system metrics like CPU/mem usage per service. Design a prefix sum based engine to answer queries like:
"Total CPU consumed by service X from time t1 to t2".