# 150 Best Fundamental Problems on Array/String techniques

In all, we have 380 problems. The problems are from the following topics:

- Two Pointers (including Sliding Window) (30)
- Hashtable (40)
- Prefix Sum (20)
- Binary Search (30)
- Recursion / Backtracking (70)
- Math (number theory, combinatorics, modular arithmetic) (40)
- Stack / Monotonic Stack (30)
- Queue (30)
- Greedy Logic (30)
- Bit Manipulation (30)
- Sorting & Partitioning (30)


### Two Pointers

Two-pointers mastery requires coverage of all variants:

* opposite ends
* fast–slow (for cycle detection, window shrinking)
* variable window (sliding window logic)
* fixed window
* partitioning and merging
* in-place rearrangements

#### Opposite Ends – Basic Pair Finding

1. [0167] Find two numbers in a sorted array that sum to a target. ✅
2. [0125] Find if a string is a palindrome ignoring non-alphanumeric characters. ✅
3. [0088] Merge two sorted arrays into one sorted array in place. ✅
4. [0026] Remove all duplicates from a sorted array (return length). ✅
5. [0027] Remove a given value in place from array. ✅
6. [0977] Square each element in a sorted array and return sorted squares. ✅
7. [0283] Move all zeros to the end while maintaining order. ✅
8. [0151] Reverse words in a string in place (no split/extra array). ✅
9. Partition array into negatives and non-negatives in place. ✅
10. [0011] Find the container with most water (max area between two lines). ✅

#### Fast–Slow Pointers – Movement and Detection

11. [0141] Detect cycle in linked list. ✅
12. [0142] Find start node of cycle in linked list. 🔄
13. [0876] Find the middle node of linked list. ✅
14. [0019] Remove the nth node from end of linked list in one pass. ✅
15. [0005] Find length of longest palindrome substring using expand-around-center (two pointers growing). 🔄
16. [0160] Find intersection node of two linked lists (if exists). 🔄

#### Sliding Window – Fixed and Variable

17. Find max sum of subarray of length *k*. ✅
    17.1. [2461] Maximum Sum of Distinct Subarrays With Length K 🔄
    17.2. [2841] Maximum Sum of Almost Unique Subarray 🔄
18. [0209] Find smallest subarray with sum ≥ target. ✅
19. [0340] Find longest substring with at most *k* distinct characters.
20. [0003] Find longest substring without repeating characters.
    20.1. [0395] Longest Substring with At Least K Repeating Characters
21. [0076] Minimum window substring containing all characters of another string.
22. [2609] Longest substring with equal number of 0s and 1s (convert then use prefix+two pointers).
23. [0424] Longest substring with same letter after ≤k replacements.
24. [3325] Count number of substrings containing at most *k* distinct characters.

#### Two-Pointer Partitioning / In-Place Rearrangement

25. [0075] Sort colors (Dutch National Flag).
26. [0080] Remove duplicates allowing at most two occurrences.
27. [0056] Merge intervals (requires sorting + scanning with overlapping checks).
28. [0905] Sort array by parity (evens before odds).
29. Move all positive numbers before negative numbers preserving order (stable partition).

#### Complex / Mixed Pattern

30. [0015] 3Sum – find all unique triplets summing to zero.
    (Contains sorting + opposite-end + skip-duplicate control—tests entire mastery.)
    30.1. [0016] 3Sum Closest

!!! note
    When you can implement all 30 with no hesitation and reason about variant edge cases verbally, your two-pointer reflex is complete.

---


### Hash Table

Hashtable mastery means pattern fluency in:

* counting 
* mapping 
* grouping 
* frequency control 
* caching 
* prefix tracking
* collision with logic


#### Frequency Counting (Fundamentals)

1. Count character frequencies in a string.
    1.1. [0451] Sort Characters By Frequency
2. Count word frequencies in a paragraph (ignore punctuation/case).
3. Find the first non-repeating character in a string.
4. Check if two strings are anagrams.
5. Check if two strings are isomorphic (pattern mapping).
6. Group anagrams together.
7. Find the majority element (appears > n/2).
8. Find all elements appearing more than ⌊n/3⌋ times.
9. Check if one array is a permutation of another.
10. Find the intersection of two arrays (distinct elements only).

#### Counting + Window / Two Pointers

11. Find smallest substring containing all characters of another string (needs hash counting).
12. Longest substring with at most *k* distinct characters.
13. Longest substring without repeating characters.
14. Find all starting indices of anagrams in a string.
15. Check if a permutation of one string is a substring of another.

#### Prefix Sum + Hash Mapping

16. Subarray sum equals *k* (count all).
17. Find maximum length subarray with sum = 0.
18. Count subarrays with equal number of 0s and 1s.
19. Count subarrays with equal number of 1s, 2s, and 3s.
20. Longest substring with equal number of letters and digits.

#### Hashing for Existence / Lookups

21. Two sum problem.
22. 3Sum using hash complement instead of sorting.
23. Find if array contains duplicates within distance *k*.
24. Find missing number from range [0, n].
25. Find first repeating element in array.
26. Determine if array has pair with given difference *k*.
27. Find pairs of elements with sum divisible by *k*.

#### Mapping / Grouping by Custom Key

28. Group words by sorted letters (anagrams by canonical key).
29. Group strings by shift pattern (“abc”, “bcd” same group).
30. Group integers by same remainder mod *k*.
31. Group coordinates by slope (use rational normalization).
32. Find all words that share at least one letter with another (bitmask + hash hybrid).

#### Advanced Hash Applications

33. Implement LRU Cache (hashmap + doubly linked list).
34. Implement LFU Cache (hashmap + frequency map).
35. RandomizedSet (insert/delete/getRandom O(1)).
36. Count number of submatrices summing to target (2D prefix + hash).
37. Detect cycle in sequence generated by function (hash visited states).
38. Check if linked list has a cycle using hashset (non two-pointer variant).
39. Find longest consecutive sequence in unsorted array.
40. Implement simple in-memory key-value store with TTL (expiration simulation).

!!! note
    When these become natural, every higher algorithm using hash tables (DP memoization, graph adjacency maps, caching layers, symbol tables) will feel like direct extensions, not new learning.

---


### Prefix Sum

Prefix sum is an **orthogonal additive technique** that becomes powerful **when combined with hashmaps** to remember cumulative states.
Pure prefix sum handles contiguous-sum reasoning in `O(n)` time; adding hash enables counting or non-fixed-length subarrays.

Concepts:

* additive range
* conditional counting
* dimensional lifting
* hashmap fusion

#### Basic 1D Prefix Sum

1. Compute prefix sum array and answer range-sum queries in O(1).
2. Given array and many updates of form (l, r, +val), apply all efficiently (difference array).
3. Given array, compute sum of all subarrays (analytical formula).
4. Find equilibrium index (prefix sum left == right).
5. Find pivot index (same as above but multiple possible).

#### Subarray Sums Using Prefix Differences

6. Count subarrays with sum = *k* (using hashmap on prefix).
7. Longest subarray with sum = 0.
8. Count subarrays with equal number of 0s and 1s (convert 0→−1).
9. Find number of subarrays with sum divisible by *k*.
10. Find subarray with maximum sum (Kadane’s logic derived from prefix deltas).

#### Variants on Conditions

11. Find smallest subarray with sum ≥ target (two-pointer + prefix).
12. Find subarray with given average *k* (transform and reduce to sum=0).
13. Count subarrays with equal number of vowels and consonants.
14. Longest subarray with equal number of positive and negative numbers.
15. Longest substring with equal number of letters and digits.

#### Prefix Sum in Multi-Dimensions

16. 2D matrix prefix sum – answer sum of any submatrix in O(1).
17. Given many submatrix increment operations, apply efficiently (2D difference array).
18. Count submatrices summing to target (2D prefix + hashmap).
19. Find maximum submatrix sum no larger than *k*.
20. Given binary matrix, count submatrices with all 1s (prefix sum + combinatorial counting).

!!! note
    Mastering all 20 gives complete prefix-sum reflex — linear-time reasoning over additive structures in any dimension.

---


### Binary Search

Binary search mastery means control over **search space, invariants, monotonic predicates, integer boundaries, and hybrid applications** (search on answer, floating domains, and function domains).
This set covers every possible reasoning domain: 

* discrete
* continuous
* rotated
* predicate-based 
* optimization

---

#### Core Array Search Patterns

1. Standard binary search (iterative and recursive).
2. Find first occurrence of target in sorted array (lower bound).
3. Find last occurrence of target (upper bound).
4. Find insertion index (bisect_left).
5. Count occurrences of a number in sorted array using bounds.
6. Find smallest element greater than target (successor).
7. Find floor and ceiling of target in sorted array.
8. Find element in rotated sorted array.
9. Find minimum in rotated sorted array.
10. Find target in rotated sorted array with duplicates.

#### Search-on-Answer (Monotonic Predicate)

11. Find smallest positive integer *x* such that f(x) ≥ target (generic monotone function).
12. Find smallest divisor given threshold (minimize max load).
13. Find smallest ship capacity to ship packages within *D* days.
14. Allocate minimum number of pages among students (classic partition minimization).
15. Koko eating bananas – find minimum eating speed.
16. Minimum days to make *m* bouquets (search over days).
17. Magnetic force between two balls – maximize minimum distance.
18. Split array largest sum – minimize largest partition sum.

#### Numerical / Floating Search

19. Find square root of a number using binary search (floating precision).
20. Find cube root using binary search.
21. Find root of monotonic function f(x) = 0 within epsilon tolerance.
22. Find maximum average subarray of length ≥ *k* (binary search on double answer).

#### Application in Sorting / Greedy / Arrays

23. Search insert position for element while maintaining sorted order (bisect concept).
24. Find length of LIS using patience sorting (binary search in tails array).
25. Count number of pairs with absolute difference ≤ *k*.
26. Find median of two sorted arrays (partition binary search).
27. Find peak element in array (unimodal function).
28. Find minimum in “mountain array” (bitonic).

#### 5. Binary Search on Index / Boundaries

29. Find smallest index *i* such that prefix[i] ≥ target (search on prefix array).
30. Find maximum length subarray satisfying some constraint using binary search on length (e.g., longest subarray with sum ≤ *k*).


!!! note
    Once you can derive the monotone condition and boundaries without confusion, you have full binary-search reflex.

---


### Recursion & Backtracking

Recursion and backtracking are the true mental load-bearers of algorithmic thinking. They expose call-stack mechanics, decision trees, and combinatorial state management. Mastery comes not from syntax, but from recursive *decomposition* reflex — the ability to identify the “base + choice + recurse + undo” cycle immediately.

#### Foundational Recursion Mechanics

1. Print numbers from 1 to N recursively (forward and backward order).
2. Sum of array elements recursively.
3. Reverse an array in place using recursion.
4. Reverse a string recursively.
5. Find maximum element in array recursively.
6. Check if a string is palindrome recursively.
7. Compute factorial recursively.
8. Compute Fibonacci recursively (then optimize via memoization).
9. Compute power(x, n) recursively (fast exponentiation).
10. Compute GCD recursively (Euclidean algorithm).

#### Divide & Conquer on Arrays

11. Binary search (recursive version).
12. Merge sort (split + merge recursion).
13. Quick sort (partition + recursive subarray sorting).
14. Count inversions in array using merge recursion.
15. Find Kth smallest element using quickselect recursion.
16. Find peak element recursively.
17. Find majority element using divide & conquer.
18. Rotate array by k using recursive reversal method.
19. Recursive array flattening (nested arrays).
20. Compute all possible sums of subsets.

#### Recursion on Strings

21. Generate all substrings of a string.
22. Generate all subsequences of a string.
23. Generate all permutations of a string (distinct).
24. Generate all permutations with possible duplicates (use set/visited).
25. Count subsequences equal to a given pattern.
26. Replace all occurrences of a character recursively.
27. Remove consecutive duplicates recursively.
28. Remove a given substring recursively from string.
29. Insert '*' between identical consecutive letters recursively.
30. Generate all case permutations of string (“a1b” → “A1B”, “a1B”…).
31. Generate all valid IP addresses from string of digits.
32. Decode ways (A=1…Z=26) recursively.
33. Restore string from pattern with wildcards (‘?’ and ‘*’).
34. Generate all balanced parentheses of n pairs.
35. Letter combinations of phone number (recursive generation).

#### Backtracking on Arrays

36. Generate all subsets (power set).
37. Generate all combinations of size k.
38. Combination sum (each number can be reused).
39. Combination sum II (no reuse, handle duplicates).
40. Subset sum equal to target.
41. Partition array into two subsets with equal sum.
42. Permutations of array elements.
43. Unique permutations with duplicates.
44. Next permutation (recursive understanding).
45. Restore array from given sum constraints (inverse recursion).
46. Generate all binary arrays of length n.
47. Generate all permutations of digits that form valid numbers (lexicographic).
48. Generate all k-length permutations of n numbers.
49. Find all increasing subsequences (handle duplicates).
50. Generate all arrays where sum ≤ target (prune branches).

#### Backtracking with Strings

51. Word break problem (return all valid segmentations).
52. Generate all valid palindrome partitions.
53. Restore valid equations by inserting '+', '-', '*' (expression add operators).
54. Generate all binary strings without consecutive 1s.
55. Generate all strings of balanced “AB” pattern (count A ≥ B always).
56. Generate all strings of length n over given charset.
57. Generate all rearrangements of digits that form palindromes.
58. Generate all valid encodings (1–26 mapping).
59. Generate all subsets of characters with lexicographic order constraint.
60. Generate all strings under pattern constraint (e.g., "1?0?" → replace ?).

#### Linked List Recursion

61. Reverse a linked list recursively.
62. Merge two sorted linked lists recursively.
63. Compare two linked lists recursively for equality.
64. Delete Nth node from end recursively.
65. Find middle node recursively.
66. Print linked list in reverse order recursively.
67. Detect palindrome linked list recursively.
68. Add two numbers represented as linked lists recursively.
69. Flatten a multi-level linked list recursively.
70. Deep clone a linked list with random pointers recursively.

!!! note
    When these become intuitive, recursion stops feeling like “magic.”
    You will see every dynamic programming or DFS later as a trivial memoized extension of these same recursive archetypes.

---


### Math: Number Theory, Combinatorics

Mathematical foundations for algorithms come down to mastering: 

* integer properties
* combinatorial reasoning
* modular arithmetic
* counting
* constructive number logic

#### Number Properties & Primes

1. Check if a number is prime (trial division).
2. Generate all primes up to *n* (Sieve of Eratosthenes).
3. Count primes up to *n* efficiently.
4. Find prime factorization of *n*.
5. Find all divisors of *n*.
6. Find GCD and LCM of two numbers.
7. Compute GCD of array elements.
8. Check if two numbers are coprime.
9. Find all pairs (i, j) in array with GCD > 1.
10. Compute Euler’s Totient φ(n).

#### Modular Arithmetic

11. Compute (a × b) % m safely for large a, b.
12. Compute (a^b) % m using fast modular exponentiation.
13. Compute modular inverse of a under prime m.
14. Solve modular linear equation ax ≡ b (mod m).
15. Compute n! % m efficiently.
16. Compute nCr % m using precomputed factorial and modular inverse.
17. Compute (a/b) % m correctly (modular division).
18. Apply modular arithmetic to large Fibonacci (mod 1e9+7).
19. Find last digit of large power (a^b).
20. Check if modular exponentiation satisfies Fermat’s little theorem.

#### Counting and Combinatorics

21. Compute nCr (recursive and DP).
22. Compute permutations count P(n, r).
23. Count number of ways to climb n stairs (Fibonacci variant).
24. Count subsets of array with even sum.
25. Count number of binary strings of length n with no consecutive 1s.
26. Count ways to arrange n people in circle (circular permutations).
27. Count ways to choose k elements such that no two are adjacent.
28. Count distinct permutations of string with duplicates.
29. Compute multinomial coefficient (n! / (n1! * n2! * ...)).
30. Compute number of combinations modulo large prime (using modular arithmetic).

#### Number Transformations & Properties

31. Reverse digits of integer recursively.
32. Check if number is Armstrong (sum of powers of digits = number).
33. Check if number is perfect (sum of proper divisors = number).
34. Convert decimal to binary recursively (and back).
35. Compute digital root (iterative reduction to one digit).

#### Mathematical Algorithms in Arrays/Strings

36. Given array of integers, find number of pairs with sum divisible by k.
37. Given large string number, compute modulo m manually (no bigint).
38. Count number of subarrays with sum divisible by k (prefix sum + modular logic).
39. Given n, find number of trailing zeros in n!
40. Compute binomial coefficient large-n small-r using Pascal’s identity recursively.

!!! note
    This set ensures total fluency in the core mathematical reasoning every algorithm depends on: factorization, modular arithmetic, counting, and number combinatorics — the quantitative muscle behind all advanced structures.

---


### Stack & Monotonic Stack

* **Stacks** → LIFO structure. Core uses: expression parsing, backtracking, DFS, bracket validation, monotonic patterns, undo systems.
* **Monotonic Stack** → specialized form that maintains increasing/decreasing order to solve “next greater/smaller element” class problems in O(n).

#### Basic Stack Logic (Implementation & Simulation)

1. Implement stack using array and linked list.
2. Implement stack using queues.
3. Evaluate postfix expression.
4. Evaluate prefix expression.
5. Convert infix expression to postfix.
6. Check for balanced parentheses/brackets/braces.
7. Simplify a Unix-style path (e.g., “/a/./b/../../c/”).
8. Decode string patterns (“3[a2[c]]” → “accaccacc”).
9. Implement min stack (O(1) getMin).
10. Implement stack supporting getMax in O(1).

#### Monotonic Stack — Next Greater/Smaller Patterns

11. Next Greater Element I (basic).
12. Next Greater Element II (circular).
13. Next Smaller Element.
14. Daily Temperatures.
15. Stock Span Problem.
16. Trapping Rain Water.
17. Largest Rectangle in Histogram.
18. Sum of Subarray Minimums.
19. Sum of Subarray Maximums.
20. 132 Pattern Detection.

#### Stack in String and Array Manipulation

21. Remove adjacent duplicates in string (stack-based).
22. Basic Calculator II (without parentheses).
23. Basic Calculator III (with parentheses).
24. Remove K digits to form smallest number.
25. Score of Parentheses.
26. Minimum Remove to Make Valid Parentheses.
27. Asteroid Collision.
28. Validate Stack Sequences.
29. Remove all adjacent duplicates in string II (with k repeats).
30. Shortest Subarray to be Removed to Make Sorted (monotonic hybrid).

---

### Queues

Goal: internalize FIFO behavior, sliding windows, monotonic queues, BFS-style traversal on 1D/2D data, and design patterns that later appear in trees/graphs.

#### Implementation & Simulation (fundamentals)

1. Implement queue using array
2. Implement queue using linked list
3. Implement circular queue (fixed size)
4. Implement queue using two stacks
5. Implement stack using two queues
6. Design a deque (double-ended queue)
7. Implement LRU cache (linked list + hashmap + queue logic)
8. Implement Hit Counter (count events in last N seconds)
9. Implement Moving Average from data stream
10. Implement Front-Middle-Back queue

#### Sliding Window (core real-world applications)
11. Sliding Window Maximum (monotonic queue)
12. Sliding Window Minimum
13. First Negative Integer in Every Window
14. Longest Subarray with Sum ≤ K (sliding window)
15. Minimum Size Subarray Sum ≥ Target
16. Longest Substring with At Most K Distinct Characters
17. Longest Repeating Character Replacement
18. Minimum Window Substring
19. Max Consecutive Ones III (allowing flips)
20. Shortest Subarray with Sum ≥ K

#### BFS-Like Patterns (queue mechanics on sequences/grids)
21. Rotting Oranges (BFS spread logic)
22. Shortest Path in Binary Matrix
23. Walls and Gates
24. Open the Lock (string BFS)
25. Word Ladder (string transformation BFS)
26. Number of Islands (queue flood fill)
27. Flood Fill (BFS version)
28. Matrix 01 (multi-source BFS)
29. Jump Game II (minimum jumps using BFS queue)
30. Minimum Operations to Convert One Number to Another (BFS over integer space)

---


### Greedy Logic

Goal: train the intuition of local optimal → global optimal; recognize when sorting or heap pairing leads to optimal global outcome.

#### Sorting-Based Greedy

1. Assign Cookies
2. Non-Overlapping Intervals
3. Merge Intervals
4. Minimum Number of Arrows to Burst Balloons
5. Queue Reconstruction by Height
6. Meeting Rooms II
7. Two City Scheduling
8. Task Scheduler
9. Reorganize String
10. Candy Distribution

#### Selection-Based Greedy
11. Jump Game I
12. Jump Game II
13. Gas Station
14. Best Time to Buy and Sell Stock I
15. Best Time to Buy and Sell Stock II
16. Partition Labels
17. Lemonade Change
18. Maximum Units on a Truck
19. Minimum Platforms (train arrival/departure)
20. Maximum Product Subarray

#### Heap/Interval/Decision Greedy
21. Huffman Encoding (build min-cost tree)
22. Activity Selection Problem
23. Job Sequencing with Deadlines
24. Fractional Knapsack
25. Remove K Digits
26. Largest Number (arrange to form biggest integer)
27. Split Array into Consecutive Subsequences
28. Minimum Cost to Connect Sticks
29. Hand of Straights
30. Jump Game — minimum steps (hybrid BFS + greedy edge case)

---


### Bit Manipulation

Goal: master XOR patterns, masking, shifting, bit counting, subsets generation, and common bit-level transformations.

#### Fundamentals (masking, parity, toggling)

1. Count number of 1 bits (Hamming Weight)
2. Check if number is power of two
3. Find single number (all appear twice except one)
4. Find two unique numbers (all appear twice except two)
5. Find single number (all appear thrice except one)
6. Reverse bits of 32-bit integer
7. Get ith bit
8. Set ith bit
9. Clear ith bit
10. Toggle ith bit

#### XOR & Arithmetic Patterns

11. Missing number (0…n range)
12. Subsets generation using bitmask
13. Gray code generation
14. XOR of all subarrays
15. XOR from 1 to n (pattern recognition)
16. Sum of two integers without `+` or `-`
17. Swap two numbers without temp variable
18. Check if two integers have opposite signs
19. Find the differing bit between two numbers
20. Compute bitwise AND of range [m, n]

#### Advanced Applications

21. Maximum XOR of two numbers in an array (Trie-based)
22. Subarray XOR equals K
23. Count of subarrays with XOR less than K
24. Maximum subset XOR
25. Minimum XOR value pair
26. Single number II (every number appears thrice except one)
27. Single number III (two unique numbers)
28. Decode XORed array
29. Total Hamming Distance among all pairs
30. Find duplicate number using bit operations (no extra space)

---


### Sorting & Partitioning

Sorting & partitioning isn’t just about calling `sort()`.
It’s the **mechanics** behind order transformations — the physical reorganization of data.
The core ideas:

* Sorting = establishing global order by local comparisons.
* Partitioning = locally separating elements based on a rule (pivot, parity, sign, etc.).
  Together, they form the *skeleton* of many algorithms: quicksort, mergesort, Dutch flag, selection problems, rearrangements, and order-statistics.
  You master this by learning to reason about *invariants* and *boundaries* in-place.

#### Basic Sorting Logic

1. Implement bubble sort manually.
2. Implement insertion sort manually.
3. Implement selection sort manually.
4. Implement merge sort (top-down recursion).
5. Implement merge sort (bottom-up iterative).
6. Implement quicksort (choose first element as pivot).
7. Implement quicksort (random pivot).
8. Implement counting sort (non-comparison integer sort).
9. Implement radix sort (for integers and strings).
10. Implement bucket sort for floats in range [0, 1).

*Goal:* build raw sorting reflex and memory of invariants (left ≤ pivot ≤ right, etc.).

#### Partitioning

11. Partition array into <pivot | pivot | >pivot (core quicksort step).
12. Partition array into negatives and non-negatives (two pointers).
13. Partition array into evens and odds.
14. Partition array by value k (less than k first).
15. Sort colors (Dutch National Flag: 0s, 1s, 2s).
16. Stable partition array by parity (preserve order).
17. Segregate 0s and 1s in binary array.
18. Move all zeros to the end, keeping order.
19. Partition array so that all elements ≤ pivot appear before pivot, others after, in place.
20. Partition array into elements <, =, > median using two pointers.

*Goal:* understand local reordering, boundary maintenance, pointer movement logic.

#### Sorting + Partition Hybrid Applications

21. Find Kth smallest element using quickselect (partition + recursion).
22. Find Kth largest element (variation).
23. Sort array by absolute value.
24. Sort array by frequency of elements.
25. Sort array by number of set bits in binary representation.

*Goal:* manipulate sorting criteria; internalize “custom comparator” thinking.

#### Partial Sorting & Reordering Patterns

26. Merge two sorted arrays in place without extra space.
27. Rearrange positive and negative numbers alternately (maintaining relative order).
28. Sort array of 0s, 1s, and 2s in one pass (optimized Dutch flag).
29. Sort array by distance from a given value x.
30. Find smallest k elements in array (partial heap + partition hybrid).

*Goal:* learn controlled reordering — not full sorting, but localized rearrangement.

!!! note
    Partitioning teaches *movement invariants*; sorting teaches *comparison invariants.*
    Together, they underpin binary search ordering, two-pointer rearrangements, selection problems, and memory-efficient data manipulation — everything from quicksort internals to load balancing.

